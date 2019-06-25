from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Group
from .serializers import GroupSerializer
from .models import User
from .serializers import UserSerializer

# Create your views here.

class GroupView(APIView):
    def get(self, request, pk=None):
        if pk:
            group = get_object_or_404(Group.objects.all(), pk=pk)
            serializer = GroupSerializer(group)
            return Response({"group": serializer.data})
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response({"groups": serializer.data})

    def post(self, request):
        group = request.data.get('group')

        # Create an group from the above data
        serializer = GroupSerializer(data=group)
        if serializer.is_valid(raise_exception=True):
            group_saved = serializer.save()
        return Response({"success": "Group '{}' created successfully".format(group_saved.group_name)})

    def put(self, request, pk):
        saved_group = get_object_or_404(Group.objects.all(), pk=pk)
        data = request.data.get('group')
        serializer = GroupSerializer(instance=saved_group, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            group_saved = serializer.save()
        return Response({"success": "Group '{}' updated successfully".format(group_saved.group_name)})


    def delete(self, request, pk):
        # Get object with this pk
        group = get_object_or_404(Group.objects.all(), pk=pk)
        group.delete()
        return Response({"message": "Group with id `{}` has been deleted.".format(pk)},status=204)

class UserView(APIView):
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User.objects.all(), pk=pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data})
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        user = request.data.get('user')

        # Create an user from the above data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.user_id)})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('user')
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' updated successfully".format(user_saved.user_id)})


    def delete(self, request, pk):
        # Get object with this pk
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)},status=204)
