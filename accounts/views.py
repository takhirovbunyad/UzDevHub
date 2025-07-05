from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages

from my_app.forms import CustomUserCreationForm
from my_app.models import CustomUser

from django.shortcuts import render, redirect
from django.urls import reverse  # 🆕 kerak bo‘ladi
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.conf import settings

from my_app.forms import CustomUserCreationForm
from my_app.models import CustomUser


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
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
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
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username yoki parol noto‘g‘ri yoki hisob faollashtirilmagan.')
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def home_view(request):
    return render(request, 'dashboard.html')
