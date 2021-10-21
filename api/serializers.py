from rest_framework import serializers
from .models import Hero, ContactMessage, Project


class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = [
            'url',
            'slug',
            'name',
            'description'
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage
        fields = [
            'url',
            'name',
            'email',
            'message',
        ]


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'url',
            'name',
            'slug',
            'blurb',
            'project_url',
            'file',
            'image',
            'secondary_image'
        ]
