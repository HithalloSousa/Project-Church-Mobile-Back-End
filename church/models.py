from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Carousel(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.name} {self.category}'


class Posts(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    name = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.name} {self.category}'


class PhotosGalery(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.name}'


class PdfDocuments(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return self.titulo
