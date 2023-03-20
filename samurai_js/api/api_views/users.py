from copy import copy

from api.models import User
from api.serializer import UserSerializer
from rest_framework import permissions, views
from rest_framework.response import Response


class UsersAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            'error': 0,
            'totalCount': [],
            'items': None,
        }

        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        s_data = copy(serializer.data)
        for d in s_data:
            d.update({'photos': ''})

        data.update({'items': s_data, 'totalCount': len(s_data)})

        return Response(data)
