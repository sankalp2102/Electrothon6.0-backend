# urls.py
from django.urls import path
from .views import SubPageListView, ImageViews, searchfunction, blogViews, TeamView, ReportblogViews

urlpatterns = [
    path('subpages/', SubPageListView.as_view(), name='subpage-list'),
    path('subpages/<str:subpage_name>/', ImageViews.as_view(), name='image-list'),
    path('subpage/search', searchfunction.as_view(), name='subpage-search'),
    path('blog/',blogViews.as_view(), name= 'blog-list'),
    path('blog/<int:blog_id>/report/', ReportblogViews.as_view(), name = 'report-blog'),
    path('teamdata/', TeamView.as_view(), name = 'team-list'),
]
