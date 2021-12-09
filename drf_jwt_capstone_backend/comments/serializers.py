from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ['url', 'id', 'user', 'comment', 'date_created']  
        fields = ['comment']