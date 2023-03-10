
from django.urls import path
from productapp.api.drf_modelserializer import productlist, productRetrieveUpdateDestroyAPIView

from productapp.api.views import * 
# from productapp.api.drf_views import drf_products_api, drf_product_api
urlpatterns = [
    # product_api
    # path('productsapi/', products_api, name='products_api'),
    # path('productsapi/<int:id>', product_api, name='product_api'),
    # path('productsapi/', drf_products_api, name='products_api'),
    # path('productsapi/<int:id>', drf_product_api, name='product_api'),
    path('productsapi/', productlist.as_view(), name='products'),
    path('productsapi/<int:pk>', productRetrieveUpdateDestroyAPIView.as_view(), name='products'),


]