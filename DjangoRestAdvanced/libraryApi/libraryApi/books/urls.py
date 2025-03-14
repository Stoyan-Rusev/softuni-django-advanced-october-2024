from django.urls import path, include
from rest_framework.routers import DefaultRouter

from libraryApi.books import views
from libraryApi.books.views import PublisherViewSet

router = DefaultRouter()   # Used for generating urls dynamically
router.register('', PublisherViewSet)

urlpatterns = [
    path('', views.ListBooksApiView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_view_set'),
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-links'),
    path('publishers/', include(router.urls))

]
