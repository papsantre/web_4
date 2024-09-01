from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    #print(dir(Product()))
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
