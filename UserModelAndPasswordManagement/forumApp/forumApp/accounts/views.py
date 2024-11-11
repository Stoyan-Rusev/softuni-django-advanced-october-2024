from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forumApp.accounts.forms import UserCreateForm


class UserRegisterView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
