from django.contrib import admin
from church.models import Carousel, Category, Posts, PhotosGalery, PdfDocuments

# Register your models here.


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'category', 'show'
    list_editable = 'show',
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'category', 'show'
    list_editable = 'show',


@admin.register(PhotosGalery)
class PhotosAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'show'
    list_editable = 'show',


@admin.register(PdfDocuments)
class PdfDocumentsAdmin(admin.ModelAdmin):
    list_display = 'id', 'titulo',
