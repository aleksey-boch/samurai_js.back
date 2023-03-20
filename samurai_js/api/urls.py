from api.api_views import auth, profile, users
from django.urls import path

urlpatterns = [
    # path('auth', auth.AuthMeAPIView.as_view(), name='api-oot'),
    path('auth/me/', auth.AuthMeAPIView.as_view(), name='auth-me'),
    path('auth/login', auth.AuthMeAPIView.as_view(), name='auth-me'),
    path('users', users.UsersAPIView.as_view(), name='users'),
    path('profile/<int:user_id>', profile.ProfileAPIView.as_view(), name='profile'),
    path('profile/status/', profile.StatusAPIView.as_view(), name='status'),
    path('profile/status/<int:user_id>', profile.StatusAPIView.as_view(), name='status-view'),
]
