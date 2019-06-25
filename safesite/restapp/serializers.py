from rest_framework import serializers

from .models import Group
from .models import User


class GroupSerializer(serializers.Serializer):
    group_name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.group_name = validated_data.get('group_name', instance.group_name)

        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        group_data = [{'group_name': 'Admin'}, {'group_name': 'Officer'}]
        
        for group_data in groups: Group.objects.create(user=user, **group_data)

        return user

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        
        instance.save()
        return instance
