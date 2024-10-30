from rest_framework import serializers

from library.models import Book

from library.models import Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'  ## ['id','title','authors']



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'  ## ['id','title','authors']


