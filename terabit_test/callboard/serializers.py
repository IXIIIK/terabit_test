from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from .models import Advertisment, Category, Requests, Comments


class UserLoginSerializer(serializers.ModelSerializer):
    '''Login serialize'''
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]


class UserRegisterSerializer(serializers.ModelSerializer):
    '''Registration serialize'''
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name",
                  "last_name", "email", "password", "password2"]
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            detail = {
                "detail": "User Already exist!"
            }
            raise ValidationError(detail=detail)
        return username

    def validate(self, instance):
        if instance['password'] != instance['password2']:
            raise ValidationError({"message": "Both password must match"})

        if User.objects.filter(email=instance['email']).exists():
            raise ValidationError({"message": "Email already taken!"})

        return instance

    def create(self, validated_data):
        passowrd = validated_data.pop('password')
        passowrd2 = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(passowrd)
        user.save()
        Token.objects.create(user=user)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    '''Users serialize'''
    class Meta:
        model = User
        fields = ('id', 'username')
    

class AdvertismentSerializer(serializers.ModelSerializer):
    '''Advertisment serialize'''
    class Meta:
        model = Advertisment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    '''Category serialize'''
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    '''Book serializer'''
    user_application = UserSerializer(read_only=True)

    class Meta:
        model = Requests
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    '''Commets serialize'''
    author = UserSerializer(read_only=True)  
  
    class Meta:  
        model = Comments 
        fields = '__all__'

