from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('self/', views.self, name='self'),
    path('financial/', views.financial, name='financial'),
    path('skills/', views.skills, name='skills'),
    path('guide/', views.guide, name='guide'),

    path('skill/', views.skill, name='skill'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('upload/', views.upload, name='upload_file'),
]
