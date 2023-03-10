from django.shortcuts import render
from category.models import Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from category.forms import CategoryModelForm

# Create your views here.

# generic views
# Generic views

# list all objects


class CategoryListView(ListView):
    model = Category
    template_name = 'listall.html'
    # object_list---> use it in the template

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'create.html'
    form_class = CategoryModelForm
    success_url = '/category/listall'


class CategoryDetailedView(DetailView):
    model = Category
    template_name = 'show.html'


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'edit.html'
    form_class = CategoryModelForm
    success_url = '/category/listall'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = '/category/listall'
