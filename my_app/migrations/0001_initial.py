# Generated by Django 5.2.1 on 2025-07-03 06:40

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Dasturlash tili')),
            ],
        ),
        migrations.CreateModel(
            name='Dash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Sarlavha')),
                ('url', models.URLField(unique=True, verbose_name='Havola')),
                ('preview', models.ImageField(upload_to='images/', verbose_name='Eskiz')),
                ('description', models.TextField(max_length=200, verbose_name='Izoh')),
                ('source', models.CharField(max_length=30, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sarlavha')),
                ('desc', models.TextField(max_length=200, verbose_name='Izoh')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Havola')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Qo‘shilgan vaqti')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('verification_code', models.CharField(blank=True, max_length=6, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Sarlavha')),
                ('url', models.URLField(unique=True, verbose_name='Havola')),
                ('description', models.TextField(max_length=200, verbose_name='Izoh')),
                ('owner', models.CharField(max_length=30, verbose_name='Owner')),
                ('owner_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Eskiz')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.category', verbose_name='Kategoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=20, verbose_name='Ismingiz')),
                ('owner_last_name', models.CharField(max_length=20, verbose_name='Familyangiz')),
                ('title', models.CharField(max_length=70, verbose_name='Sarlavha')),
                ('code', models.TextField(blank=True, null=True, verbose_name='Kodingizni joylashtiring')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Batafsil')),
                ('description', models.CharField(max_length=200, verbose_name='Izoh')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Qo‘shilgan vaqti')),
                ('file', models.FileField(blank=True, null=True, upload_to='code_files/')),
                ('slug', models.SlugField(blank=True, max_length=255, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.category')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
