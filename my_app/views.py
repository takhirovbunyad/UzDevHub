import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from django.utils.text import slugify

from .forms import Pro_form
from . import services


# ------------------- DASHBOARD -------------------
@login_required
def first(request):
    page_number = int(request.GET.get('page', 1))
    page_size = 8
    offset = (page_number - 1) * page_size
    all_dash = services.get_all_dash(page_size, offset)

    paginator = Paginator(all_dash, page_size)
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {'page_obj': page_obj})


@login_required
def news_view(request):
    yangiliklar = services.get_all_news()
    return render(request, 'news.html', {'yangiliklar': yangiliklar})


@login_required
def learn_view(request):
    kurslar = services.get_all_courses()
    return render(request, 'learn.html', {'kurslar': kurslar})


def load_more_cards(request):
    page = int(request.GET.get("page", 1))
    page_size = 6
    offset = (page - 1) * page_size
    cards = services.get_all_dash(page_size, offset)

    data = {
        "cards": [
            {
                "title": obj.title,
                "description": obj.description,
                "url": obj.url,
                "preview": obj.preview.url if obj.preview else '',
                "source": obj.source
            }
            for obj in cards
        ],
        "has_next": len(cards) == page_size
    }
    return JsonResponse(data)


@login_required
def dash_view(request):
    initial_cards = services.get_initial_dash(6)
    return render(request, 'dash.html', {'initial_cards': initial_cards})


# ------------------- PROJECTS -------------------
@login_required
@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        form = Pro_form(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
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
    page_number = int(request.GET.get('page', 1))
    page_size = 6
    offset = (page_number - 1) * page_size

    projects = services.get_published_projects(page_size, offset)
    paginator = Paginator(projects, page_size)
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
        for p in page_obj
    ]

    context = {
        'projects': page_obj,
        'projects_json': json.dumps(projects_json),
        'categories': services.get_all_categories(),
        'has_next': page_obj.has_next(),
        'slug': slug
    }
    return render(request, 'projects.html', context)


@login_required
def project_detail(request, year, month, day, slug):
    project = services.get_project_detail(slug, year, month, day)
    if not project:
        return JsonResponse({'error': 'Project not found'}, status=404)

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
    page = int(request.GET.get('page', 1))
    page_size = 6
    offset = (page - 1) * page_size
    projects = services.get_published_projects(page_size, offset)

    html = ""
    for item in projects:
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
    projects = services.get_all_published_projects()
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
        'projects_json': projects_json,
        'categories': services.get_all_categories(),
        'modal_open_slug': slug,
    }
    return render(request, 'projects.html', context)


# ------------------- USERS -------------------
@login_required
def user_profile(request, user_id):
    user = services.get_user_by_id(user_id)
    if not user:
        return JsonResponse({'error': 'User not found'}, status=404)

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


def user_info_by_name(request):
    first = request.GET.get('first')
    last = request.GET.get('last')
    if not first or not last:
        return JsonResponse({'error': 'first va last bo\'lishi kerak'}, status=400)

    user = services.get_user_by_name(first, last)
    if not user:
        return JsonResponse({'error': 'User not found'}, status=404)

    data = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return JsonResponse(data)
