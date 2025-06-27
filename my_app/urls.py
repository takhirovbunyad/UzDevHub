from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.first, name='first_page'),
    path('news/', views.news_view, name='news'),
    path('learn/', views.learn_view, name='learn_page'),
    path('load_more_cards/', views.load_more_cards, name='load_more_cards'),  # agar kerak bo'lsa Dash uchun
    path('projects/', views.project_list, name='project_list'),
    path('add-project/', views.add_project, name='add_project') ,
    path('load-more-projects/', views.load_more_projects, name='load_more_projects'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.project_detail, name='project_detail'),
]
