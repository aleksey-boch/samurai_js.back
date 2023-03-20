from django.http import Http404
from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response

from api.models import User, Profile
from api.serializer import UserSerializer, ProfileSerializer, AuthMeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer

    def list(self, request):
        data = {
            'resultCode': 0,
            'messages': [],
            'data': None,
        }

        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)
        data.update({'data': serializer.data, })

        return Response(data)


class AuthMeViewSet(viewsets.ViewSet):
    # queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    # serializer_class = AuthMeSerializer
    pagination_class = None

    def list(self, request):
        data = {
            'resultCode': 0,
            'messages': [],
            'data': None,
        }

        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)
        data.update({'data': serializer.data, })

        return Response(data)
