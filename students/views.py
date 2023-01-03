from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets, permissions
from .models import Student

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer

