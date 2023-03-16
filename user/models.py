from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profilr_pictures/', blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    registered_on = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    



    def __str__(self):
        return self.username
    
    def __str__(self):
        return self.email


