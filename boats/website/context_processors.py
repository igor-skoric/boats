from .models import Config


def config(request):
    # Dohvati prvog klijenta sa is_default=True
    config = Config.objects.all().first()
    return {'config': config}
