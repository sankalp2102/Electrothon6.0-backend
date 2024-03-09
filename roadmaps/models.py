from django.db import models


class SubPage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
    
class ImageforRoadmap(models.Model):
    subpage = models.ForeignKey(SubPage, on_delete=models.DO_NOTHING)
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return self.image
    
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    details = models.TextField()
    reports = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title
    
class TeamData(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.URLField(max_length=1000)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkdin = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name