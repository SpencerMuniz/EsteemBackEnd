from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(null=True, blank=True, max_length=100)