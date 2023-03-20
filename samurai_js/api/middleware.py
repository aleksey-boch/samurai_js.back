from rest_framework import status
from rest_framework.response import Response


def authorization_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        data = {}

        if (
            request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be'
            and request.COOKIES.get('authorization') is None
        ):
            data.update({'error': 401})
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
