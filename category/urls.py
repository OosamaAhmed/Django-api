

from django.urls import path
from category.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('show/<int:pk>', CategoryDetailedView.as_view(), name='category.show'),
    path('listall/', CategoryListView.as_view(), name='category.listall'),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name='category.delete'),
    path('create/', CategoryCreateView.as_view(), name='category.create'),
    path('edit/<int:pk>', login_required(CategoryUpdateView.as_view()),
         name='category.edit')
]
