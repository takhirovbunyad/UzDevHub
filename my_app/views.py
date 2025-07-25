from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from django.utils.text import slugify
from accounts import views
import json
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Kurs, Dash, Projects, Category, CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import Pro_form
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def first(request):
    all_dash = Dash.objects.all().order_by('-id')
    paginator = Paginator(all_dash, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {'page_obj': page_obj})


@login_required
def news_view(request):
    yangiliklar = News.objects.all().order_by('-created')
    return render(request, 'news.html', {'yangiliklar': yangiliklar})

@login_required
def learn_view(request):
    kurslar = Kurs.objects.all()
    return render(request, 'learn.html', {'kurslar': kurslar})

def load_more_cards(request):
    page = int(request.GET.get("page", 1))
    cards = Dash.objects.all().order_by('-id')
    paginator = Paginator(cards, 6)

    current_page = paginator.get_page(page)

    data = {
        "cards": [
            {
                "title": obj.title,
                "description": obj.description,
                "url": obj.url,
                "preview": obj.preview.url if obj.preview else '',
                "source": obj.source
            }
            for obj in current_page
        ],
        "has_next": current_page.has_next()
    }

    return JsonResponse(data)

@login_required
def dash_view(request):
    initial_cards = Dash.objects.all().order_by('-id')[:6]
    return render(request, 'dash.html', {'initial_cards': initial_cards})

@login_required
@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        form = Pro_form(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)

            # ✅ Eng MUHIM qator – egasini belgilaymiz:
            project.owner = request.user

            project.status = 'published'
            if not project.slug:
                project.slug = slugify(project.title)
            if not project.publish:
                project.publish = timezone.now()
            project.save()

            project_data = {
                'id': project.id,
                'slug': project.slug,
                'title': project.title,
                'description': project.description,
                'owner_name': project.owner_name,
                'owner_last_name': project.owner_last_name,
                'file': project.file.url if project.file else '',
                'url': project.url if project.url else '',
                'category': project.category.name if project.category else '',
                'publish': project.publish.isoformat() if project.publish else ''
            }
            return JsonResponse({'success': True, 'project': project_data})
        else:
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
    return JsonResponse({'success': False, 'error': 'Noto‘g‘ri metod'})


@login_required
def project_list(request, slug=None):
    projects = Projects.published.all().order_by('-publish')
    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    projects_json = [
        {
            'id': p.id,
            'slug': p.slug,
            'title': p.title,
            'description': p.description,
            'owner_name': p.owner_name,
            'owner_last_name': p.owner_last_name,
            'file': p.file.url if p.file else '',
            'url': p.url if p.url else '',
            'category': p.category.name if p.category else '',
            'publish': p.publish.isoformat() if p.publish else ''
        }
        for p in page_obj.object_list
    ]

    context = {
        'projects': page_obj,
        'projects_json': json.dumps(projects_json),
        'categories': Category.objects.all(),
        'has_next': page_obj.has_next(),
        'slug': slug  # JS uchun URLdagi slug ni beramiz
    }

    return render(request, 'projects.html', context)

@login_required
def project_detail(request, year, month, day, slug):
    project = get_object_or_404(
        Projects,
        slug=slug,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    data = {
        'id': project.id,
        'title': project.title,
        'owner_name': project.owner_name,
        'owner_last_name': project.owner_last_name,
        'description': project.description,
        'file_url': project.file.url if project.file else '',
        'url': project.url if project.url else '',
        'category': project.category.name if project.category else ''
    }
    return JsonResponse(data)

@login_required
def load_more_projects(request):
    page = request.GET.get('page')
    projects = Projects.published.all().order_by('-publish')
    paginator = Paginator(projects, 6)

    try:
        projects_page = paginator.page(page)
    except:
        return HttpResponse("")

    html = ""
    for item in projects_page:
        category = f'<div class="category-badge">🏷️ {item.category.name}</div>' if item.category else ''
        description = item.description[:100] + ('...' if len(item.description) > 100 else '')
        file_link = f'<a href="{item.file.url}" download>📦 Faylni yuklash</a>' if item.file else ''
        url_link = f'<a href="{item.url}" target="_blank">🔗 Linkga o‘tish</a>' if item.url else ''
        category_detail = f'<p><strong>Kategoriya:</strong> {item.category.name}</p>' if item.category else ''

        html += f"""
        <div class="project-card" onclick="openModal('{item.id}', '{item.slug}', '{item.publish.isoformat()}')">
            {category}
            <h3>{item.title}</h3>
            <p>{description}</p>
            <div class="owner">👤 {item.owner_name} {item.owner_last_name}</div>
            <div class="owner">📅 {item.publish.strftime('%d.%m.%Y %H:%M')}</div>
        </div>

        <div class="modal" id="modal-{item.id}">
            <div class="modal-content">
                <span class="close" onclick="closeModal('{item.id}')">&times;</span>
                <h2>{item.title}</h2>
                <p><strong>Muallif:</strong> {item.owner_name} {item.owner_last_name}</p>
                <p>{item.description}</p>
                {category_detail}
                <div class="modal-buttons">
                    {file_link}
                    {url_link}
                </div>
            </div>
        </div>
        """

    return HttpResponse(html)

@login_required
def projects_view_with_modal(request, year, month, day, slug):
    projects = Projects.published.all().order_by('-publish')

    projects_json = [
        {
            'id': p.id,
            'slug': p.slug,
            'title': p.title,
            'description': p.description,
            'owner_name': p.owner_name,
            'owner_last_name': p.owner_last_name,
            'file': p.file.url if p.file else '',
            'url': p.url if p.url else '',
            'category': p.category.name if p.category else '',
            'publish': p.publish.isoformat() if p.publish else ''
        }
        for p in projects
    ]

    context = {
        'projects': projects,
        'projects_json': projects_json ,

        'categories': Category.objects.all(),
        'modal_open_slug': slug,
    }

    return render(request, 'projects.html', context)



@login_required
def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "profession": getattr(user, "profession", ""),
        "address": getattr(user, "address", ""),
        "email": user.email,
        "telegram": getattr(user, "telegram", ""),
        "linkedin": getattr(user, "linkedin", ""),
        "github": getattr(user, "github", ""),
        "website": getattr(user, "website", ""),
        "bio": getattr(user, "bio", ""),
        "phone_number": getattr(user, "phone_number", ""),
        "gender": getattr(user, "gender", ""),
    }
    return JsonResponse(data)






from django.http import JsonResponse
from .models import CustomUser

def user_info_by_name(request):
    first = request.GET.get('first')
    last = request.GET.get('last')
    if not first or not last:
        return JsonResponse({'error': 'first va last bo\'lishi kerak'}, status=400)
    try:
        user = CustomUser.objects.get(first_name=first, last_name=last)
        data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            # qolgan maydonlar kerak bo'lsa qo'sh
        }
        return JsonResponse(data)
    except CustomUser.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
