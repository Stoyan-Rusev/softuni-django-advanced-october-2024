from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from todoApi.accounts.views import RegisterUserView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
