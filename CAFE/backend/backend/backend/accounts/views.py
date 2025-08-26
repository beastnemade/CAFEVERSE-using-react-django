from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import UserSerializer,LoginSerializer,SignupSerializer

from rest_framework.permissions import AllowAny

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key,'user':UserSerializer(user).data},status=201)
        return Response(serializer.errors,status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token,created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key,'User':UserSerializer(user).data},status=201)
        return Response(serializer.errors,status=400)