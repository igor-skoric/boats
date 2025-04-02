from django.db import models
from django.utils.text import slugify


class Config(models.Model):
    contact_phone = models.CharField(max_length=100, blank=True, null=True, default='+381 60 111 111')
    email = models.EmailField(blank=True, null=True, default='contact@yacht.rs')
    instagram_link = models.CharField(max_length=255, blank=True, null=True, default='www.instagram.com')
    address = models.CharField(max_length=255, blank=True, null=True, default='defautl address')


class Yacht(models.Model):
    YACHT_TYPE_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    name = models.CharField(max_length=255, verbose_name="Naziv jahte")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Cena (€)")
    year = models.IntegerField(verbose_name="Godina proizvodnje", blank=True, null=True)
    length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Dužina (m)")
    yacht_type = models.CharField(max_length=10, choices=YACHT_TYPE_CHOICES, verbose_name="Tip jahte", default="used")
    description = models.TextField(blank=True, verbose_name="Opis jahte")
    image = models.ImageField(upload_to='yachts/', blank=True, null=True, verbose_name="Slika jahte")
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Datum objave")

    def __str__(self):
        return f"{self.name} ({self.get_yacht_type_display()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)