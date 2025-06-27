
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Kurs, Dash , Projects , Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import Pro_form
from django.http import HttpResponse, JsonResponse
def first(request):
    all_dash = Dash.objects.all().order_by('-id')
    paginator = Paginator(all_dash, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {'page_obj': page_obj})

def news_view(request):
    yangiliklar = News.objects.all().order_by('-created')
    return render(request, 'news.html', {'yangiliklar': yangiliklar})

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

def dash_view(request):
    initial_cards = Dash.objects.all().order_by('-id')[:6]
    return render(request, 'dash.html', {'initial_cards': initial_cards})


@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        form = Pro_form(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            data = {
                'success': True,
                'project': {
                    'id': project.id,
                    'title': project.title,
                    'description': project.description,
                    'ism': project.owner_name,
                    'familya': project.owner_last_name,
                    'url': project.url,
                    'file': project.file.url if project.file else '',
                    'category': project.category.name if project.category else ''
                }

            }
            return JsonResponse(data)
        else:
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
    return JsonResponse({'success': False, 'error': 'Noto‘g‘ri metod'})
def project_list(request):
    projects = Projects.objects.order_by('-datetime')
    categories = Category.objects.all()

    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # JSON uchun faqat kerakli maydonlar
    projects_json = [
        {
            'id': p.id,
            'slug': p.slug,
            'title': p.title,
            'description': p.description,
            'owner_name': p.owner_name,
            'owner_last_name': p.owner_last_name,
            'file': p.file.url if p.file else '',
            'url': p.url,
        } for p in page_obj.object_list
    ]

    # context ichida projects_json qo‘shilgan
    context = {
        'projects': page_obj,
        'categories': categories,
        'has_next': page_obj.has_next(),
        'projects_json': projects_json  # faqat bitta marta qo‘shiladi
    }

    return render(request, 'projects.html', context)

def load_more_projects(request):
    page = request.GET.get('page')
    projects = Projects.objects.order_by('-datetime')
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
        <div class="project-card" onclick="openModal('{item.id}')">
            {category}
            <h3>{item.title}</h3>
            <p>{description}</p>
            <div class="owner">👤 {item.owner_name} {item.owner_last_name}</div>
            <div class="owner">📅 {item.datetime.strftime('%d.%m.%Y %H:%M')}</div>
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

def project_detail(request, year, month, day, slug):
    project = get_object_or_404(
        Projects,
        slug=slug,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'projects/detail.html', {'project': project})