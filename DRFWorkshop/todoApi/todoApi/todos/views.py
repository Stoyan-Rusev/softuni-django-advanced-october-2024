from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from todoApi.todos.models import Todo
from todoApi.todos.serializers import TodoSerializer, TodoDetailSerializer


class TodosListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()

        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category)

        is_done = self.request.query_params.get('is_done', None)
        if is_done is not None:
            queryset = queryset.filter(state=is_done)

        return queryset


class TodoDetailAPIView(RetrieveAPIView):
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()
