from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Modelserializers):
    class Meta:
        model = Book
        fields = '__all__'