from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework.views import APIView

from api_app.serializers import PersonSerializer, CourseSerializer, TaskSerializer, ProfessionSerializer
from courseapp.models import Profession, AdditionalInfo, Course
from task_app.models import File, Task, Comment
from users_app.models import Person, City


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


class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the course
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Course.objects.filter(person=user)


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
