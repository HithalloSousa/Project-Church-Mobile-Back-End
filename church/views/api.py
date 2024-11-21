from rest_framework import viewsets, permissions
from ..models import Category, Posts, PdfDocuments, Carousel, PhotosGalery
from ..serializers import CategorySerializer, PostsSerializer, PdfDocumentsSerializer, CarouselSerializer, PhotosGalerySerializer

# ViewSet para Categoria


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostUltimasEdb(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Posts.objects.filter(show=True, category__name='Ultimas Edb')


class PostsDevocionais(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Posts.objects.filter(show=True, category__name='Devocionais')


class PdfFirstItem(viewsets.ModelViewSet):
    serializer_class = PdfDocumentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return PdfDocuments.objects.filter(
            category__name='Ultimas Edb')


class CarouselShow(viewsets.ModelViewSet):
    serializer_class = CarouselSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Carousel.objects.filter(show=True, category__name='Carousel')


class PhotoGalleryViewSet(viewsets.ModelViewSet):
    serializer_class = PhotosGalerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return PhotosGalery.objects.filter(show=True)
