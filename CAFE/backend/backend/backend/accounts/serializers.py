from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','role']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','role','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'customer')
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self,data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError('Incorrect Email or password.')
        # email = data.get('email')
        # password = data.get('password')

        # if email and password:
        #     user = authenticate(request=self.context.get('request'), email=email, password=password)
        #     if not user:
        #         raise serializers.ValidationError('Incorrect Email or password.', code='authorization')
        # else:
        #     raise serializers.ValidationError('Must include "email" and "password".', code='authorization')

        # data['user'] = user
        # return data