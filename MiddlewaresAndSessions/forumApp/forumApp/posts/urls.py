from django.urls import path, include
from forumApp.posts import views
from forumApp.posts.views import RedirectHomeView, IndexView, DashboardView, AddPostView, EditPostView, DeletePostView, \
    DetailPostView, approve_post

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dash'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', DeletePostView.as_view(), name='delete-post'),
        path('details-post/', DetailPostView.as_view(), name='details-post'),
        path('edit-post/', EditPostView.as_view(), name='edit-post'),
        path('approve/', approve_post, name='approve'),
    ])),
    path('redirect/', RedirectHomeView.as_view(), name='redirect-home'),
]
