from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.db import IntegrityError
from .models import *
from .serializers import *

class SubPageListView(APIView):
    def post(self, request, format=None):
        serializer = SubPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        blogs = SubPage.objects.all()
        serializer = SubPageSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, formart = None):
        SubPage.objects.all().delete()
        return Response({'message': 'All data deleted successfully'}, status=status.HTTP_200_OK)
    

class ImageViews(APIView):
    

    def post(self, request, subpage_name, format=None):
        try:
            subpage = SubPage.objects.get(name=subpage_name)
        except SubPage.DoesNotExist:
            return Response({'error': 'SubPage not found'}, status=status.HTTP_404_NOT_FOUND)
        request.data['subpage'] = subpage.id
        serializer = ImageForRoadmapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, subpage_name, format=None):
        try:
            subpage = SubPage.objects.get(name=subpage_name)
            images = ImageforRoadmap.objects.filter(subpage=subpage)
            serializer = ImageForRoadmapSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SubPage.DoesNotExist:
            return Response({'error': 'SubPage not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
    def delete(self, request, formart = None):
        ImageforRoadmap.objects.all().delete()
        return Response({'message': 'All data deleted successfully'}, status=status.HTTP_200_OK)


    
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, formart = None):
        Blog.objects.all().delete()
        return Response({'message': 'All data deleted successfully'}, status=status.HTTP_200_OK)
    
    
class ReportblogViews(APIView):
    
    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(id = blog_id)
            blog.reports += 1
            
            if blog.reports >=5:
                blog.delete()
                return Response({"message": "Blog deleted due to multiple reports."}, status=status.HTTP_204_NO_CONTENT)
            
            blog.save()
            
            serializer = blogSerializer(blog)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Blog.DoesNotExist:
            return Response({"message": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)




class TeamView(APIView):
    
    def get(self, request, format = None):
        team_members = TeamData.objects.all()
        serializer = Teamserializer(team_members, many=True)
        return Response(serializer.data)
    
    def delete(self, request, formart = None):
        TeamData.objects.all().delete()
        return Response({'message': 'All data deleted successfully'}, status=status.HTTP_200_OK)
    
    def post(self, request,format = None):
        serializer = Teamserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    