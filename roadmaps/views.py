from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.db import IntegrityError
from .models import *
from .serializers import *

class SubPageListView(ListAPIView):
    queryset = SubPage.objects.all()
    serializer_class = SubPageSerializer
    


class ImageViews(APIView):
    
    def get( self,request, subpage_name, format=None):
        images = ImageforRoadmap.objects.filter(subpage = subpage_name)
        serializer = ImageForRoadmapSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class searchfunction(APIView):
    
    def get(self, request, format = None):
        search_query = self.request.query_params.get('search', None)
        if not search_query:
            return Response({'error': 'Search query is required'}, status=status.HTTP_400_BAD_REQUEST)

        subpages = SubPage.objects.filter(name__icontains=search_query)
        serializer = SubPageSerializer(subpages, many=True)
        return Response(serializer.data)
    
    
class blogViews(APIView):
    
    
    
    
    
    
    def post(self, request, format=None):
        try:
            serializer = blogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
    
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = blogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    
class TeamView(APIView):
    
    def get(self, request, format = None):
        team_members = TeamData.objects.all()
        serializer = Teamserializer(team_members, many=True)
        return Response(serializer.data)