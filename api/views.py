from django.core.mail import send_mail

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Hero, ContactMessage, Project
from .serializers import HeroSerializer, ContactMessageSerializer, ProjectSerializer


class HeroViewset(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = 'slug'
    # permission_classes = [IsAdminUser]


class ContactMessageViewset(viewsets.ModelViewSet):
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()
    # permission_classes = [IsAdminUser]

    # May eventually send emails with Amazon SES wit this code:
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     send_mail(
    #         'Message from Contact Form',
    #         f"Email: {request.data.get('email')}\
    #         \nName: {request.data.get('name')}\
    #         \n\nMessage:\n{request.data.get('message')}\n",
    #         '"Kenny\'s Contact Form" <kennylepping@kennylepping.com>',
    #         ['kennylepping@gmail.com']
    #     )
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     # Can send custom responses to the frontend here
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    # permission_classes = [IsAdminUser]
