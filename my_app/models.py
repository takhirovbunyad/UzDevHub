from random import random
from django.contrib.auth.models import AbstractUser
import random
import string

from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.views.generic import ListView
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class News(models.Model):
    name = models.CharField("Sarlavha", max_length=50)
    desc = models.TextField("Izoh", max_length=200)
    link = models.URLField("Havola" , blank=True , null=True)
    created = models.DateTimeField("Qo‘shilgan vaqti", auto_now_add=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField('Dasturlash tili', max_length=30)

    def __str__(self):
        return self.name


class Kurs(models.Model):
    title = models.CharField('Sarlavha', max_length=50)
    url = models.URLField('Havola', unique=True)
    description = models.TextField("Izoh", max_length=200)
    owner = models.CharField('Owner', max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    owner_img = models.ImageField('Eskiz' , upload_to='images/' , blank=True , null=True)

    def __str__(self):
        return self.title


class Dash(models.Model):
    title = models.CharField('Sarlavha', max_length=70)
    url = models.URLField('Havola', unique=True)
    preview = models.ImageField('Eskiz', upload_to='images/')
    description = models.TextField("Izoh", max_length=200)
    source = models.CharField('Owner', max_length=30)



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Projects(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    owner_name = models.CharField('Ismingiz', max_length=20)
    owner_last_name = models.CharField('Familyangiz', max_length=20)
    title = models.CharField('Sarlavha', max_length=70)
    code = models.TextField('Kodingizni joylashtiring', blank=True, null=True)
    url = models.URLField('Batafsil', blank=True, null=True)
    description = models.CharField("Izoh", max_length=200)
    datetime = models.DateTimeField("Qo‘shilgan vaqti", auto_now_add=True)
    file = models.FileField(upload_to='code_files/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique_for_date="publish", blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:project_detail", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.publish:
            self.publish = timezone.now()
        if not self.status:
            self.status = 'draft'
        super().save(*args, **kwargs)

def generate_verification_code():
    return ''.join(random.choices(string.digits, k=6))

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.verification_code:
            self.verification_code = generate_verification_code()
        super().save(*args, **kwargs)