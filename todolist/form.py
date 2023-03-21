from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = ["user_id", "title", "content", "complete", "date_created"]