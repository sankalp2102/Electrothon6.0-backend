from rest_framework import serializers
from .models import *

class SubPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPage
        fields = '__all__'
        

class ImageForRoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageforRoadmap
        fields = '__all__'
        
        
class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        

class Teamserializer(serializers.ModelSerializer):
    class Meta:
        model = TeamData
        fields = '__all__'