from django.urls import path
from .views import task, task_detail_view, task_add_view, task_update_view, task_delete_view

app_name = "task"
urlpatterns = [
    path('task_list/', task, name="task-list"),
    path('task-detail-view/<str:pk>', task_detail_view, name="task-detail-view"),
    path('task-add/', task_add_view, name="task-add-view"),
    path('task-update-view/<str:pk>', task_update_view, name="task-update-view"),
    path('task-delete-view/<str:pk>', task_delete_view, name="task-delete-view"),
]


