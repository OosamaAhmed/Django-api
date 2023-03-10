from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from productapp.models import Product
from productapp.forms import ProductModelForm
from django.contrib.auth.decorators import login_required



def homepage(request):
    myproducts = Product.objects.all()
    return render(request, 'main.html' , context={"myproducts":myproducts})

def showproduct(request,id):
    myproducts = get_object_or_404(Product, pk=id)
    return render(request, 'showproduct.html', context={"myproducts": myproducts})

def deleteproduct(request, id):
    myproducts = get_object_or_404(Product, pk=id)
    myproducts.delete()
    return redirect('home')

def contactus(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'about.html')


def createNewProduct(request):
    if request.method == 'GET':
        productform = ProductModelForm()
        return render(request, 'create.html', context={'form': productform})

    elif request.method=='POST':
        productform = ProductModelForm(request.POST, request.FILES)
        if productform.is_valid():
            productform.save()
        return redirect('home')
    return redirect('create')

@login_required
def editProduct(request,id):
    myproducts = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        Productform = ProductModelForm(instance=myproducts)
        return render(request, 'edit.html', context={'form': Productform})
    if request.method == 'POST':
        Productform = ProductModelForm(
            request.POST, request.FILES, instance=myproducts)
        if Productform.is_valid():
            Productform.save()
            return render(request, 'showproduct.html', context={"myproducts": myproducts})

        return redirect('create')
