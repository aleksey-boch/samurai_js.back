import datetime
from typing import Union

from api.models import User
from api.serializer import AuthMeSerializer
from rest_framework import permissions, status, views
from rest_framework.response import Response

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


class AuthMeResponse(Response):
    def __init__(self, result_code: int = 0, messages: Union[list[str], str] = None, data: dict = None, **kwargs):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(data={'resultCode': result_code, 'messages': messages, 'data': data}, **kwargs)


class AuthMeResponseAuthorizedError(AuthMeResponse):
    def __init__(self, messages, **kwargs):
        super().__init__(
            resultCode=status.HTTP_401_UNAUTHORIZED,
            messages=messages,
            status=status.HTTP_401_UNAUTHORIZED,
            **kwargs,
        )


class AuthMeAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)

        return AuthMeResponse(data=serializer.data)

    def post(self, request):
        email = request.data.get('email')
        if email is None:
            return AuthMeResponseAuthorizedError(messages='email not found')

        user = User.objects.filter(email=email).first()  #

        if user is None:
            return AuthMeResponseAuthorizedError(messages='user not found')

        serializer = AuthMeSerializer(user, many=False)

        data = {'userId': serializer.data.get('id')}
        response = AuthMeResponse(data=data)
        set_cookie(response, key='authorization', value=hash((8769856, str(data))))

        return response

    def delete(self, request):
        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)
        # todo
        data = {}

        response = AuthMeResponse(data=data)
        set_cookie(response, key='authorization', value='')

        return response
