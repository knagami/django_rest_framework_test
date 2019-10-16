# coding: utf-8

from rest_framework import serializers

from .models import User, Entry, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書き
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('filepath','created_at', 'updated_at')