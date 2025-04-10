from .models import Config
from django.urls import resolve, reverse


def config(request):
    # Dohvati prvog klijenta sa is_default=True
    config = Config.objects.all().first()
    return {'config': config}


def breadcrumbs(request):
    """Generiše breadcrumbs na osnovu trenutnog URL-a."""
    url_name = resolve(request.path_info).url_name  # Dobijamo ime rute
    kwargs = request.resolver_match.kwargs
    breadcrumbs = [("Početna", "/")]

    if url_name == "all_products":
        breadcrumbs.append(("Svi proizvodi", "/products/"))
    elif url_name == "new_products":
        breadcrumbs.append(("Svi proizvodi", "/products/"))
        breadcrumbs.append(("Novi proizvodi", "/products/new/"))
    elif url_name == "used_products":
        breadcrumbs.append(("Svi proizvodi", "/products/"))
        breadcrumbs.append(("Polovni proizvodi", "/products/used/"))
    elif url_name == "product_details":
        product_slug = kwargs.get("slug", "")  # Uzmi slug iz URL-a
        breadcrumbs.append(("Svi proizvodi", reverse("all_products")))
        breadcrumbs.append((product_slug.replace("-", " ").title(), request.path))  # Prikazivanje lepog naziva
    elif url_name == "services":
        product_slug = kwargs.get("slug", "")  # Uzmi slug iz URL-a
        breadcrumbs.append(("Sve usluge", reverse("services")))
        breadcrumbs.append((product_slug.replace("-", " ").title(), request.path))  # Prikazivanje lepog naziva

    return {"breadcrumbs": breadcrumbs}