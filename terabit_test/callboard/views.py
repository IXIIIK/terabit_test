from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

# models
from .models import Advertisment, Category, Requests, Comments
# serilaizer
from .serializers import AdvertismentSerializer, CategorySerializer, UserLoginSerializer, UserRegisterSerializer, BookSerializer, CommentsSerializer
from rest_framework.response import Response


class UserLoginAPIView(APIView):
    '''Login Views'''
    def post(self, request, *args, **kargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "username": {
                    "detail": "User Doesnot exist!"
                }
            }
            if User.objects.filter(username=request.data['username']).exists():
                user = User.objects.get(username=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(APIView):
    '''Register views'''

    @swagger_auto_schema(
        operation_description="Регистрация нового пользователя",
        responses={200: UserLoginSerializer()})
    
    def post(self, request, *args, **kargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'user': serializer.data,
                'token': Token.objects.get(user=User.objects.get(username=serializer.data['username'])).key
            }
            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(
            serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)


class UserLogoutAPIView(APIView):
    '''Logout views'''
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)
    

class AdvertismentCreateView(generics.ListCreateAPIView):
    '''Create advertisment views'''
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer
    permission_classes = [IsAuthenticated]

    
class AdvertismentDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''Detail advertisment views'''
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer  
    #permission_classes = [IsAuthenticated]
    

class BookAdvertismentView(APIView):
    pass



class AdvertismentListView(generics.ListAPIView):
    '''All advertisment views'''
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer
    #permission_classes = [IsAuthenticated]


class AdvertismentUpdateView(generics.RetrieveUpdateAPIView):
    '''Update advertisment views'''
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer
    #permission_classes = [IsAuthenticated] #исправить: редактировать может только автор поста
    partial = True
    


class AdvertismentDeleteView(generics.DestroyAPIView):
    '''Delete advertisment'''
    queryset = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer
    #permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))
    

class CategoryViewSet(generics.ListAPIView):
    '''Category view'''
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BookAdvertismentViews(APIView):
    queryset = Advertisment.objects.all()
    serializer_class = BookSerializer

    def post(self, request, pk=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'user': serializer.data,
            }
        return Response(response, status=status.HTTP_200_OK)
    

class AllRequestsViews(generics.ListAPIView):
    queryset = Requests.objects.all()
    serializer_class = BookSerializer


class ApproveAdvertismentView(APIView):
    def post(self, request, pk):
        try:
            order = Advertisment.objects.get(id=pk)
        except Advertisment.DoesNotExist:
            return Response({"error": "объявление не найдено"}, status=status.HTTP_404_NOT_FOUND)

        if order.status == 'pending':
            order.status = 'accepted'
            order.delete()
            return Response({"message": "Статус изменён на 'Принято'"})
        
        return Response({"message": f"Текущий статус: {order.get_status_display()}"})


class RejectedAdvertismentView(APIView):
    def post(self, request, pk):
        try:
            order = Advertisment.objects.get(id=pk)
        except Advertisment.DoesNotExist:
            return Response({"error": "объявление не найдено"}, status=status.HTTP_404_NOT_FOUND)

        if order.status == 'pending':
            order.status = 'rejected'
            order.delete()
            return Response({"message": "Статус изменён на 'Отклонено'"})
        
        return Response({"message": f"Текущий статус: {order.get_status_display()}"})
    

class CommentView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()  
    serializer_class = CommentsSerializer   
  
    

