from api.models import User
from api.serializer import ContactsSerializer, PhotoSerializer, ProfileSerializer
from rest_framework import permissions, views
from rest_framework.response import Response


class ProfileAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_id):
        data = {}
        user = User.objects.filter(id=user_id).first()
        profile = user.profile
        contacts = user.contacts
        photo = user.photo
        data.update(
            {
                **ProfileSerializer(profile, many=False).data,
                'userId': user.id,
                'contacts': ContactsSerializer(contacts, many=False).data,
                'photos': PhotoSerializer(photo, many=False).data,
            }
        )

        return Response(data)


class StatusAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_id):
        user = User.objects.filter(id=user_id).first()

        return Response(user.status)

    def put(self, request, user_id=1):
        user = User.objects.filter(id=user_id).first()
        user.status = request.data.get('status')
        user.save()
        data = {'resultCode': 0, 'messages': [], 'data': {}}

        return Response(data)
