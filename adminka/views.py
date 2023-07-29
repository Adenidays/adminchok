from django.shortcuts import render, get_object_or_404, redirect
from adminka.models import Product
from django.forms.models import modelform_factory
from adminka.forms import ProductModelForm
from django.urls import reverse

# Create your views here.
def start_page(request):
    products = Product.objects.all()
    if request.method == "POST":
        product_id = request.POST.get('inp')
        prod = Product.objects.get(pk=product_id)
        prod.delete()
    return render(request, 'admin_start_page.html', context={'products':products})

def add_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():        
            form.save()
            return redirect(reverse('adminka:start_page'))
    else:
        form = ProductModelForm()
    context = {'form':form}
    return render(request, 'addproduct.html', context=context)

def edit_product(request,product_id):
    product = Product.objects.get(pk=product_id)
    old_name = product.name
    old_category = product.category
    old_price = product.price
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            return redirect(reverse('adminka:start_page'))
    else:
        
        initial_data = {
        'name' : old_name,
        'category' : old_category,
        'price' : old_price,
    } 
        form = ProductModelForm(initial=initial_data)
    context = {'form':form}
    return render(request, 'editproduct.html', context=context)
                