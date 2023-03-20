from copy import copy

from django.http import Http404
from rest_framework import views, permissions, mixins, status
from rest_framework.response import Response

from api.models import User, Profile
from api.serializer import UserSerializer, ProfileSerializer, AuthMeSerializer


class UsersAPIView(views.APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        data = {
            'error': 0,
            'totalCount': [],
            'items': None,
        }

        # if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
        if not request.COOKIES.get('authorization'):
            data.update({'error': 401, })
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        s_data = copy(serializer.data)
        for d in s_data:
            d.update({'photos': ''})

        data.update({
            'items': s_data,
            'totalCount': len(s_data),
        })

        return Response(data)
