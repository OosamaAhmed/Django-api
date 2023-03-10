from category.models import Category
from productapp.api.serializers import ProductModelSerializer
from productapp.models import Product
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView,  RetrieveUpdateDestroyAPIView

# class Productlist(APIView) :
#     def get(self, request):
#         myproducts = Product.objects.all()
#         seralize_product = ProductSerializer(myproducts, many=True)
#         return Response(seralize_product.data, status=status.HTTP_200_OK)

# way two
# class productlist(ListAPIView):
#     serializer_class = ProductModelSerializer
#     queryset = Product.objects.all()
    
# way three


class productlist(ListCreateAPIView):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()


#
# RetrieveUpdateDestroyAPIView

class productRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()

