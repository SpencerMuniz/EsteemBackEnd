from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(null=True, blank=True, max_length=100)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    