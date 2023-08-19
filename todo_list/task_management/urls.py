from django.urls import path
from task_management.views import manage_task, show_tasks, edit_tasks, delete_tasks, completed_tasks, complete
urlpatterns = [
    path('', manage_task, name='ManageTask'),
    path('show_tasks/', show_tasks, name='ShowTask'),
    path('edit_tasks/<int:id>', edit_tasks, name='EditTask'),
    path('delete_tasks/<int:id>', delete_tasks, name='DeleteTask'),
    path('completed_tasks/<int:id>', completed_tasks, name='CompletedTask'),
    path('complete/', complete, name='Completed'),
]