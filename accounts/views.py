from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str, force_bytes
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from my_app.forms import CustomUserCreationForm
from .services import get_user_by_username, get_user_by_name, search_users

User = get_user_model()


# -------------------
# Auth views
# -------------------
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            activation_link = request.build_absolute_uri(
                reverse('accounts:activate', args=[uid, token])
            )

            subject = 'Hisobingizni faollashtiring'
            from_email = settings.DEFAULT_FROM_EMAIL
            to = [user.email]
            text_content = 'Hisobingizni faollashtirish uchun havolani bosing.'
            html_content = render_to_string('accounts/activation_email.html', {
                'user': user,
                'activation_link': activation_link
            })

            email = EmailMultiAlternatives(subject, text_content, from_email, to)
            email.attach_alternative(html_content, "text/html")
            email.send()

            messages.success(
                request,
                "Ro‘yxatdan o‘tdingiz! Emailingizga yuborilgan havola orqali hisobingizni faollashtiring."
            )

            return render(request, 'accounts/signup.html', {'form': CustomUserCreationForm()})
        else:
            messages.error(request, "Iltimos, to‘g‘ri ma’lumot kiriting.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()
            messages.success(request, "Hisobingiz faollashtirildi! Endi tizimga kiring.")
        else:
            messages.info(request, "Hisobingiz allaqachon faollashtirilgan.")
        return redirect('accounts:login')
    else:
        messages.error(request, "Faollashtirish havolasi noto‘g‘ri yoki muddati o‘tgan.")
        return redirect('accounts:signup')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('/')
        messages.error(request, 'Username yoki parol noto‘g‘ri yoki hisob faollashtirilmagan.')
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def home_view(request):
    return render(request, 'dashboard.html')


# -------------------
# API / JSON endpoints
# -------------------
def user_info(request, username):
    user = get_user_by_username(username)
    if not user:
        return JsonResponse({"error": "User not found"}, status=404)

    data = _to_public_dict(request, user)
    return JsonResponse(data)


def public_user_info_by_name(request):
    first = request.GET.get('first')
    last = request.GET.get('last')
    if not first or not last:
        return JsonResponse({"error": "first va last kerak"}, status=400)

    user = get_user_by_name(first.strip(), last.strip())
    if not user:
        return JsonResponse({"error": "User topilmadi"}, status=404)

    return JsonResponse(_to_public_dict(request, user))


def public_user_info(request, username):
    user = get_user_by_username(username)
    if not user:
        return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse(_to_public_dict(request, user))


# -------------------
# Helper
# -------------------
def _to_public_dict(request, user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "profession": getattr(user, "profession", None),
        "address": getattr(user, "address", None),
        "bio": getattr(user, "bio", None),
        "workplace": getattr(user, "workplace", None),
        "phone_number": getattr(user, "phone_number", None),
        "telegram": getattr(user, "telegram", None),
        "linkedin": getattr(user, "linkedin", None),
        "github": getattr(user, "github", None),
        "website": getattr(user, "website", None),
        "profile_image": (
            request.build_absolute_uri(user.profile_image.url)
            if getattr(user, "profile_image", None)
            else None
        ),
        "gender": getattr(user, "gender", None),
    }
