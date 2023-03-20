import datetime

from django.http import Http404
from rest_framework import views, permissions, mixins, status
from rest_framework.response import Response

from api.models import User, Profile
from api.serializer import UserSerializer, ProfileSerializer, AuthMeSerializer
from samurai_js import settings


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        # max_age=max_age,
        # expires=expires,
        # domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
        samesite='None',
    )


class AuthMeAPIView(views.APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        data = {
            'resultCode': 0,
            'messages': [],
            'data': None,
        }

        # if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
        if not request.COOKIES.get('authorization'):
            data.update({'resultCode': 401, })
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)
        data.update({'data': serializer.data, })

        return Response(data)

    def post(self, request):
        data = {
            'resultCode': 0,
            'messages': [],
            'data': None,
        }

        # if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
        #     data.update({'resultCode': 401, })
        #     return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        # print(request.data)

        email = request.data.get('email')
        if email is None:
            data.update({'resultCode': 401, 'messages': ['email not found', ]})
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(email=email).first()  #
        # print(user.email)
        if user is None:
            data.update({'resultCode': 401, 'messages': ['user not found', ]})
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        serializer = AuthMeSerializer(user, many=False)

        data.update({'data': {'userId': serializer.data.get('id'), }})

        response = Response(data)
        set_cookie(response, key='authorization', value=hash((8769856, str(data))))

        return response

    def delete(self, request):
        data = {
            'resultCode': 0,
            'messages': [],
            'data': None,
        }

        # if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
        #     data.update({'resultCode': 401, })
        #     return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)
        # print(serializer.data)
        data.update({'data': {}})

        response = Response(data)
        set_cookie(response, key='authorization', value='')

        return response
