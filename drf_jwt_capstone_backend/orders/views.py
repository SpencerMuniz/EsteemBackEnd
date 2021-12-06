from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])    
def post_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)