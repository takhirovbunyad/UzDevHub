from django.db import models
from django.db.models import FileField


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



class Projects(models.Model):
    owner_name = models.CharField('Ismingiz', max_length=20)
    owner_last_name = models.CharField('Familyangiz', max_length=20)
    title = models.CharField('Sarlavha', max_length=70)
    code = models.TextField('Kodingizni joylashtiring', blank=True, null=True)
    url = models.URLField('Batafsil', unique=False, blank=True, null=True)
    description = models.CharField("Izoh", max_length=200)
    datetime = models.DateTimeField("Qo‘shilgan vaqti", auto_now_add=True)
    file = models.FileField(upload_to='code_files/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title