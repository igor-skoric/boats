from django.shortcuts import render, get_object_or_404
from .models import Yacht


def home(request):
    context = {}
    return render(request, 'website/pages/index.html', context)


def products(request, product_type):
    yachts = Yacht.objects.filter(yacht_type=product_type, published=True)
    context = {'product_type': product_type, 'yachts': yachts}
    print(context)
    return render(request, 'website/pages/products.html', context)


def product_details(request, slug):
    yacht = Yacht.objects.get(slug=slug)
    context = {'yacht': yacht}
    return render(request, 'website/pages/product_details.html', context)


def about(request):
    context = {}
    return render(request, 'website/pages/about.html', context)


def services(request):
    context = {}
    return render(request, 'website/pages/services.html', context)


def service_details(request):
    context = {}
    return render(request, 'website/pages/service_details.html', context)

