from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_comments),
    path('', views.post_comments)
]