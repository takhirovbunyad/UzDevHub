from django.urls import path
from .views import first, news_view, learn_view, load_more_cards, project_list , add_project , load_more_projects

urlpatterns = [
    path('', first, name='first_page'),
    path('news/', news_view, name='news'),
    path('learn/', learn_view, name='learn_page'),
    path('load_more_cards/', load_more_cards, name='load_more_cards'),  # agar kerak bo'lsa Dash uchun
    path('projects/', project_list, name='project_list'),
    path('add-project/', add_project, name='add_project') ,
    path('load-more-projects/', load_more_projects, name='load_more_projects'),
]

