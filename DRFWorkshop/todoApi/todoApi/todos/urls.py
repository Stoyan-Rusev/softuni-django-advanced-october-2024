from django.urls import path

from todoApi.todos.views import TodosListCreateAPIView, TodoDetailAPIView

urlpatterns = [
    path('', TodosListCreateAPIView.as_view(), name='todos-list-create'),
    path('<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
]
