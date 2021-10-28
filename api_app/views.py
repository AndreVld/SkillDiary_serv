from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework.views import APIView

from api_app.serializers import PersonSerializer, CourseSerializer, TaskSerializer, ProfessionSerializer, \
    CourseWithOutTaskSerializer, PersonDetailsSerializer
from courseapp.models import Profession, AdditionalInfo, Course
from task_app.models import File, Task, Comment
from users_app.models import Person

UserModel = get_user_model()


class ProfessionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class PersonViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CourseList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = CourseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the course
        for the currently username.
        """
        username = self.kwargs['username']
        return Course.objects.filter(person__username=username)


class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the course
        for the currently authenticated user.
        """
        user = self.request.user
        return Course.objects.filter(person=user)


class CourseWithOutTaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseWithOutTaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the course
        for the currently authenticated user.
        """
        user = self.request.user
        return Course.objects.filter(person=user)


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the tasks
        for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(user=user)


class PersonDetailsView(viewsets.ModelViewSet):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.
    """
    serializer_class = PersonDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        """
        return Person.objects.filter(id=self.request.user.id)
