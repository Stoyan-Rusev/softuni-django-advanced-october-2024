from django.urls import path

from libraryApi.books import views

urlpatterns = [
    path('', views.ListBooksApiView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_view_set')
]
