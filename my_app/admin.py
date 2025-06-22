from django.contrib import admin
from .models import News, Kurs, Category , Dash , Projects

admin.site.register(News)
admin.site.register(Kurs)
admin.site.register(Category)
admin.site.register(Dash)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner_name', 'owner_last_name', 'datetime')
    search_fields = ('title', 'owner_name')
    list_filter = ('datetime',)
