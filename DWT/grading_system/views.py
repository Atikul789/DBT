from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from django.http import HttpResponse
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic.base import TemplateView
import hashlib
from rest_framework.generics import *


class UserCreate(APIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, format=None):
        email = request.data.get('email', None)
        username = request.data.get('username', None)
        str_password = request.data.get('password', None)
        password = hashlib.sha256(str_password.encode())
        password = password.hexdigest()
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        user_type = request.data.get('user_type', None)
        data = {'email': email, 'username': username, 'password': password, 'first_name': first_name,
                'last_name': last_name, 'user_type': user_type}
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id', None)
        str_password = request.data.get('password', None)
        password = hashlib.sha256(str_password.encode())
        password = password.hexdigest()
        data = {'user_id': user_id, 'password': password}
        serializer_class = UserLoginSerializer(data=data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class UserLogout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetreive(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk):
        user_instance = User.objects.get(user_id=pk)
        if str(user_instance.user_type) == "pupil" or str(user_instance.user_type) == "admin":
            user_instance.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_304_NOT_MODIFIED)


class ClassCreate(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassList(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassUpdate(UpdateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDestroy(DestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class SubjectCreate(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectList(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectUpdate(UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDestroy(DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TestCreate(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestList(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestUpdate(UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDestroy(DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class AssignedPupilCreate(CreateAPIView):
    queryset = AssignedPupil.objects.all()
    serializer_class = AssignedPupilSerializer


class AssignedPupilList(ListAPIView):
    queryset = AssignedPupil.objects.all()
    serializer_class = AssignedPupilSerializer


class AssignedPupilUpdate(UpdateAPIView):
    queryset = AssignedPupil.objects.all()
    serializer_class = AssignedPupilSerializer


class AssignedPupilDestroy(DestroyAPIView):
    queryset = AssignedPupil.objects.all()
    serializer_class = AssignedPupilSerializer


class HomePageView(TemplateView):
    template_name = "home.html"
