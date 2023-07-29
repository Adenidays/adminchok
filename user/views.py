from django.shortcuts import get_object_or_404, render, redirect

from adminka.models import Product

# Create your views here.
def user_start_page(request):
    products =  Product.objects.filter(status=False)
    if request.method == "POST":
        prod_id = request.POST.get("buy")
        product = Product.objects.get(pk=prod_id)
        product.status = True
        product.save()
    return render(request, 'index.html', context={'products':products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', context={"product":product})