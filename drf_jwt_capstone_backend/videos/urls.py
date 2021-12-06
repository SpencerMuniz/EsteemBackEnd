from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_video),
    path('', views.post_video)
]