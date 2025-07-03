from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import News, Kurs, Category, Dash, Projects, CustomUser

# Soddalashtirilgan ro‘yxatdan o‘tkazish
admin.site.register(News)
admin.site.register(Kurs)
admin.site.register(Category)
admin.site.register(Dash)


# Loyihalar uchun chiroyli admin ko‘rinishi
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'owner_name',
        'owner_last_name',
        'status',
        'category_display',
        'publish',
        'created'
    )
    search_fields = ('title', 'owner_name', 'owner_last_name', 'description')
    list_filter = ('status', 'category', 'publish', 'created')
    list_per_page = 20
    ordering = ['-publish']
    readonly_fields = ('created', 'updated', 'datetime')
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('📌 Loyiha haqida', {
            'fields': (
                'title',
                'slug',
                'description',
                'code',
                'url',
                'file',
                'category',
                'status'
            )
        }),
        ('👤 Muallif ma’lumotlari', {
            'fields': ('owner_name', 'owner_last_name')
        }),
        ('⏱ Sana va vaqt', {
            'fields': ('publish', 'created', 'updated', 'datetime'),
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
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Ruxsatlar', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Muvofiqlik', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)