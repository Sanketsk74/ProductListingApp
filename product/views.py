from django.shortcuts import render,redirect
from product.forms import ProductForm
from product.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    if request.method == "GET":
        prod = request.GET.get('productName')
        if prod!=None:
            products = Product.objects.filter(productName__icontains=prod)
    return render(request, 'index.html',{'products':products})

def addProduct(request):
    form = ProductForm()
    product = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    data = {'form':form,'product':product}
    return render(request,'add.html',data)

def UpdateProduct(request,id):
    product = Product.objects.get(id=id)

    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    data ={'form':form}

    return render(request,'update.html',data)

def DeleteProduct(request,id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('/')
    
    data = {'product':product}
    
    return render(request,'delete.html',data)