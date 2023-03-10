

from django.urls import path ,include
from accounts.views import *


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='accounts.register'),
    path('profile/', ProfileView.as_view(), name='accounts.profile'),

]
