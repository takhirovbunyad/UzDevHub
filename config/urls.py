from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.account_view import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('auth/', include('accounts.urls', namespace='accounts')),
    path('profile/', profile_view, name='profile'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
