from django.db import models
from django.conf import settings 
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True) 
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['complete'] 