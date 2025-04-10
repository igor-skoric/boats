from django.shortcuts import render, get_object_or_404
from .models import Yacht


def home(request):
    context = {}
    return render(request, 'website/pages/index.html', context)


def products(request, product_type):
    used = []
    new = []

    if product_type == "new":
        new = Yacht.objects.filter(yacht_type=product_type, published=True)  # Pretpostavljam da imaš 'condition' polje
        title = "Nova Plovila"
    elif product_type == "used":
        used = Yacht.objects.filter(yacht_type=product_type, published=True)
        title = "Polovna Plovila"
    else:
        title = "Sva Plovila"
        used = Yacht.objects.filter(yacht_type='used', published=True)
        new = Yacht.objects.filter(yacht_type='new', published=True)

    context = {'product_type': product_type, 'new': new, 'used': used, 'title':title}

    return render(request, 'website/pages/products.html', context)


def product_details(request, slug):
    yacht = Yacht.objects.get(slug=slug)
    characteristic = yacht.characteristics.all()
    context = {'yacht': yacht, 'characteristic': characteristic}

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

