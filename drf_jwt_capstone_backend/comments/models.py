from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Commented {self.comment}"