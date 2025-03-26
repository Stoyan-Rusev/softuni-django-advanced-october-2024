from rest_framework import serializers

from todoApi.accounts.serializers import UserSerializer
from todoApi.todos.models import Todo, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['id']


class TodoDetailSerializer(serializers.ModelSerializer):
    assignees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['id', 'assignees']
