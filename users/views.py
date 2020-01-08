from rest_framework import generics

from . import models
from . import serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters, generics, mixins, routers, viewsets, permissions
from rest_framework.response import Response




class UserListView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer



class StudentSignUpView(generics.CreateAPIView):
    serializer_class = serializers.SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            User = models.User.objects.create(username=serializer.data['username'],email=serializer.data['email'])
            User.set_password(serializer.data['password1'])
            User.is_studentt = True
            User.save()
            return Response({'status': 201}, status=201)
        return Response(serializer.errors, status=401)

class TeacherSignUpView(generics.CreateAPIView):
    serializer_class = serializers.SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            User = models.User.objects.create(username=serializer.data['username'],email=serializer.data['email'])
            User.set_password(serializer.data['password1'])
            User.is_instructor = True
            User.save()
            return Response({'status': 201}, status=201)
        return Response(serializer.errors, status=401)


