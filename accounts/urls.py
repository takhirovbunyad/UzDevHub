from django.urls import path
from . import views, account_view
from my_app.views import user_profile
from .api_views import  user_info_api

app_name = 'accounts'

urlpatterns = [

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),

    path('profile/', account_view.profile_view, name='profile'),

    path('user-info/<int:user_id>/', user_profile, name='user_info'),

    path('user-info/<int:user_id>/', user_info_api, name='user_info_api'),
]
