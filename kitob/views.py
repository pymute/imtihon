from django.shortcuts import render
from rest_framework.views import APIView
from .models import avtorModel
from .serializers import Serializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework import generics
# Create your views here.
class AllAvtorView(APIView):
    def get(self,request,*args,**kwargs):
        todos = avtorModel.objects.all()
        serializers = Serializer(todos,many=True)
        return Response(serializers.data)
class AllApiView():
    def get(self,request,*args,**kwargs):
        all_task =avtorModel.objects.all()
        serializer = Serializer(all_task,many=True)
        return Response(serializer.data,status=200)

class DetailApiView(generics.RetrieveAPIView):
      queryset = avtorModel.objects.all()
      serializer_class = Serializer

class AllCreateView(generics.ListCreateAPIView):
       queryset = avtorModel.objects.all()
       serializer_class = Serializer

class UpdateApiView(generics.UpdateAPIView):
       queryset = avtorModel.objects.all()
       serializer_class = Serializer

class DeleteApiView(generics.DestroyAPIView):
      queryset = avtorModel.objects.all()
      serializer_class = Serializer
