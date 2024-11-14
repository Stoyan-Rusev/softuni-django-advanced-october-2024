from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forumApp.accounts.forms import CustomUserCreationForm


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
