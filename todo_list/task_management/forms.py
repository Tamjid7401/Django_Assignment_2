from django import forms
from task_management.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['id', 'taskTitle', 'taskDescription']
        exclude = ['id']
        labels = {
            'taskTitle' : 'Title',
            'taskDescription' : 'Description'
        }
           
        
            
            
        