from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import NewUserForm

class Register(CreateView):
    model = User
    template_name = 'register.html'
    form_class = NewUserForm
    success_url = '/category/listall'


class ProfileView(View):
    def get(self, request):
        # return HttpResponse('--- Welcome to your profile ----')
        return redirect('category.listall')


