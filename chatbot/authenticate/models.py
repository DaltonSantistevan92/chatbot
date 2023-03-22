from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name
