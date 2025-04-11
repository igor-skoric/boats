from django import template

register = template.Library()  # Registracija filtera

@register.filter  # Dekorator koji označava da je ovo filter
def intdot(value):
    try:
        # Pokušaj da konvertuješ vrednost u integer
        value = int(value)
        # Formatiraj broj sa tačkama umesto zareza
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value  # Ako nije broj, vrati originalnu vrednost
