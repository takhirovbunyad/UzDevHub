from django.urls import path
from . import views
from . import accounts_views
app_name = 'projects'

urlpatterns = [
    path('', views.first, name='first_page'),
    path('news/', views.news_view, name='news'),
    path('learn/', views.learn_view, name='learn_page'),
    path('load_more_cards/', views.load_more_cards, name='load_more_cards'),
    path('projects/', views.project_list, name='project_list'),
    path('add-project/', views.add_project, name='add_project'),
    path('load-more-projects/', views.load_more_projects, name='load_more_projects'),
    path('projects/<slug:slug>/', views.project_list, name='project_detail_modal'),

    path('api/projects/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.project_detail, name='project_detail_api'),

    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.projects_view_with_modal, name='project_detail_page'),

    path('signup/', accounts_views.signup_view, name='signup'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('home/', accounts_views.home_view, name='home'),
    path('activate/<uidb64>/<token>/', accounts_views.activate_account, name='activate'),
]