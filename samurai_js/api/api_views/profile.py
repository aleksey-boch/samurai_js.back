from copy import copy

from django.http import Http404
from rest_framework import views, permissions, mixins, status, generics
from rest_framework.response import Response

from api.models import User, Profile, Contacts, Photo
from api.serializer import UserSerializer, ProfileSerializer, AuthMeSerializer, ContactsSerializer, PhotoSerializer


class ProfileAPIView(views.APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, user_id):
        data = {}
        # if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
        if not request.COOKIES.get('authorization'):
            data.update({'error': 401, })
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(id=user_id).first()
        profile = user.profile
        contacts = user.contacts
        photo = user.photo
        data.update({
            **ProfileSerializer(profile, many=False).data,
            'userId': user.id,
            'contacts': ContactsSerializer(contacts, many=False).data,
            'photos': PhotoSerializer(photo, many=False).data,

        })

        return Response(data)


class StatusAPIView(views.APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, user_id):
        data = {}
        # if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
        if not request.COOKIES.get('authorization'):
            data.update({'error': 401, })
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(id=user_id).first()

        return Response(user.status)

    def put(self, request, user_id=1):
        data = {}
        # if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
        if not request.COOKIES.get('authorization'):
            data.update({'error': 401, })
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(id=user_id).first()
        user.status = request.data.get('status')
        user.save()
        data = {
            'resultCode': 0,
            'messages': [],
            'data': {},
        }

        return Response(data)
