from rest_framework import serializers
from .models import Category, Carousel, Posts, PhotosGalery, PdfDocuments


# Serializer para Categoria
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Serializer para o Carousel


class CarouselSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Carousel
        fields = ['id', 'name', 'picture', 'show',
                  'created_date', 'owner', 'category']


# Serializer para os Posts
class PostsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Posts
        fields = ['id', 'name', 'picture', 'show',
                  'created_date', 'owner', 'category']


# Serializer para a Galeria de Fotos
class PhotosGalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotosGalery
        fields = ['id', 'name', 'picture', 'show', 'created_date', 'owner']


# Serializer para os Documentos PDF
class PdfDocumentsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = PdfDocuments
        fields = ['id', 'titulo', 'arquivo',
                  'created_date', 'owner', 'category']
