from django.forms import ModelForm,Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
# from django.contrib.

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        widgets = {
          'task': Textarea(attrs={'rows':5}),
          'note': Textarea(attrs={'rows':3}),
        }
class RegUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']