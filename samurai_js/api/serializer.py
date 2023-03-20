from rest_framework import serializers
from .models import User, Profile, Contacts, Photo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'login', 'status')


class AuthMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login', 'email',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
