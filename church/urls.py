from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import api

# Configurando o router
router = DefaultRouter()
router.register('categories', api.CategoryViewSet)
router.register('posts', api.PostViewSet, basename='posts')
router.register('ultima_edb', api.PostUltimasEdb, basename='ultimaedb')
router.register('pdf', api.PdfFirstItem, basename='pdf_first')
router.register('carousel', api.CarouselShow, basename='carousel_show')

urlpatterns = [
    path('', include(router.urls)),
]
