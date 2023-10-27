from rest_framework.serializers import ModelSerializer

from website.models import Message, Category, User, Response

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ResponseSerializer(ModelSerializer):
    class Meta:
        model = Response
        fields = ['id' ,'content', 'author']
    author = AuthorSerializer()
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
       # depth = 1

    category = CategorySerializer()
    author = AuthorSerializer()
    responses = ResponseSerializer(many=True)
