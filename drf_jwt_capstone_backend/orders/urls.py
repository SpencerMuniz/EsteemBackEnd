from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_order),
    path('', views.post_order)
]