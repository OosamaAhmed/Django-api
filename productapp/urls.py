from django.urls import path ,include
from productapp.views import homepage, contactus, aboutus, showproduct, deleteproduct, createNewProduct, editProduct


urlpatterns = [ 
    path('home', homepage, name='home'),
    path('contact', contactus, name='contactus'),
    path('about', aboutus, name='aboutus'),
    path('show/<int:id>', showproduct, name='show'),
    path('delete/<int:id>', deleteproduct, name='delete'),
    path('create', createNewProduct, name='create'),
    path('edit/<int:id>', editProduct, name='edit'),
    path('api/', include('productapp.api.urls'))
    ]

