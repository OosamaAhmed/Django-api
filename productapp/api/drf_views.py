from productapp.api.serializers import ProductSerializer
from productapp.models import Product, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def drf_products_api(request):
    if request.method == 'GET':
        myproducts = Product.objects.all()
        seralize_product = ProductSerializer(myproducts, many=True)
        return Response(seralize_product.data ,status=status.HTTP_200_OK)
    elif request.method == 'POST':
         productData = ProductSerializer(data=request.data)
         if productData.is_valid():
            print("valid------------------------")
            productData.save() # go to create function in serializer
            return Response(productData.data, status=status.HTTP_201_CREATED)
         else:
            return Response(seralize_product.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT' , 'DELETE'])
def drf_product_api(request,id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        seralize_product = ProductSerializer(product)
        return Response(seralize_product.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'deleted':1}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        seralize_product = ProductSerializer(instance=product ,data=request.data)
        if seralize_product.is_valid():
            seralize_product.save()
            return Response(seralize_product.data, status=status.HTTP_200_OK)
        else:
            return Response(seralize_product.error,status=status.HTTP_400_BAD_REQUEST)
