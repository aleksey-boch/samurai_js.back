import functools

from rest_framework import status
from rest_framework.response import Response


def authorization_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        data = {}

        if (
                request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be'
                and (request.COOKIES and request.COOKIES.get('authorization') is None)
        ):
            data.update({'error': 401})
            response = Response(data, status=status.HTTP_401_UNAUTHORIZED)
            # response.accepted_renderer = JSONRenderer()
            # response.accepted_media_type = "application/json"
            # response.renderer_context = {}
            # response.render()
            return response

        response = get_response(request, *args, **kwargs)

        return response

    return middleware


def requires_auth(function):
    @functools.wraps(function)
    def wrapper(request, *args, **kwargs):
        data = {}

        if (
                request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be'
                and (request.COOKIES and request.COOKIES.get('authorization') is None)
        ):
            data.update({'error': 401})
            response = Response(data, status=status.HTTP_401_UNAUTHORIZED)
            # response.accepted_renderer = JSONRenderer()
            # response.accepted_media_type = "application/json"
            # response.renderer_context = {}
            # response.render()
            return response

        # user = request.user
        # if not user:
        #     return make_response(request, 401, 'User not authenticated', reverse(
        #         'auth:login', args={'next': request.full_path}))
        # if not (user.is_staff or user.is_superuser):
        #     if not user.is_verified:
        #         log.warning('The user is not verified')
        #         return make_response(request, 401, 'User not approved', '/')
        #     # if not user.has_accepted_tos:
        #     #     return make_response(request, 401, 'TOS not accepted', reverse(
        #     #         'auth:accept_terms_of_service'))
        return function(request, *args, **kwargs)

    return wrapper
