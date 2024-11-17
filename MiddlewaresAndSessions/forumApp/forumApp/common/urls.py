from django.urls import path

from forumApp.common.views import SetTimeCookie

urlpatterns = [
    path('last-visit/', SetTimeCookie.as_view(), name='set-time'),
]
