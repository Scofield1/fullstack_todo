from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from project.models import *


class ListTodo(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class UpdateTodo(generics.RetrieveUpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class CreateTodo(generics.CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class DeleteTodo(generics.DestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers
