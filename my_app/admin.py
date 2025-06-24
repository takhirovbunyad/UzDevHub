from django.contrib import admin
from .models import News, Kurs, Category, Dash, Projects

# Soddalashtirilgan ro‘yxatdan o‘tkazish
admin.site.register(News)
admin.site.register(Kurs)
admin.site.register(Category)
admin.site.register(Dash)

# Loyihalar uchun chiroyli admin ko‘rinishi
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner_name', 'owner_last_name', 'category_display', 'datetime')
    search_fields = ('title', 'owner_name', 'owner_last_name')
    list_filter = ('datetime', 'category')
    list_per_page = 20
    ordering = ['-datetime']
    readonly_fields = ('datetime',)

    fieldsets = (
        ('📌 Loyiha haqida', {
            'fields': ('title', 'description', 'url', 'category')
        }),
        ('👤 Muallif ma’lumotlari', {
            'fields': ('owner_name', 'owner_last_name')
        }),
        ('⏱ Sana va vaqt', {
            'fields': ('datetime',),
            'classes': ('collapse',)
        }),
    )

    def category_display(self, obj):
        return obj.category.name if obj.category else "-"
    category_display.short_description = 'Kategoriya'

    class Media:
        css = {
            'all': ('css/admin_custom.css',)  # static/css/admin_custom.css joyidan yuklanadi
        }


# Admin sayt sarlavhalari (title & header)
admin.site.site_header = "UzDevHub Admin Paneli"
admin.site.site_title = "UzDevHub Boshqaruvi"
admin.site.index_title = "Boshqaruv Paneliga Xush Kelibsiz"
