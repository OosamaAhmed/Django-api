import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from productapp.api.serializers import ProductSerializer 
from django.views.decorators.csrf import csrf_exempt
from productapp.api.serializers import ProductModelSerializer
from productapp.models import Product


@csrf_exempt
def products_api(request):
    if request.method == 'GET':
        myproducts = Product.objects.all()
        serialized_product= []
        for i in myproducts:
            # serialized_product.append(ProductSerializer(i).data)
            serialized_product.append(ProductModelSerializer(i).data)


        return JsonResponse(serialized_product, safe=False)
    elif request.method == 'POST':
        # json.load
        productData = json.loads(request.body)
        products = Product.objects.create(**productData)
        # return JsonResponse(ProductSerializer(products).data)
        return JsonResponse(ProductModelSerializer(products).data)

    

@csrf_exempt
def product_api(request, id):
    # get object
    product = get_object_or_404(Product , pk=id)
    if request.method == 'GET':
        # return JsonResponse(ProductSerializer(product).data) # serializer 
        return JsonResponse(ProductModelSerializer(product).data)  # serializer

# -===========================================================
    elif request.method == 'PUT':
        updated_data = json.loads(request.body)
        product.name = updated_data["name"]
        product.price = updated_data["price"]
        product.description = updated_data["description"]
        product.save()
        # return JsonResponse(ProductSerializer(product).data)
        return JsonResponse(ProductModelSerializer(product).data)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({"delete": 1})



# =============================================================
