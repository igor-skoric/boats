import json
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Config(models.Model):
    contact_phone = models.CharField(max_length=100, blank=True, null=True, default='+381 60 111 111')
    email = models.EmailField(blank=True, null=True, default='contact@yacht.rs')
    instagram_link = models.CharField(max_length=255, blank=True, null=True, default='www.instagram.com')
    address = models.CharField(max_length=255, blank=True, null=True, default='defautl address')


class YachtCharacteristic(models.Model):
    yacht = models.ForeignKey('Yacht', on_delete=models.CASCADE, related_name='characteristics')

    # Tip karakteristike iz liste ispod
    name = models.CharField(max_length=100, choices=[
        ('model', 'MODEL'),
        ('length', 'DUŽINA(m)'),
        ('beam', 'ŠIRINA'),  # širina
        ('draft', 'GAZ (m)'),  # gaz
        ('weight', 'TEŽINA (t)'),
        ('propulsion', 'POGON'),
        ('fuel_tank', 'TANK GORIVA (l)'),
        ('water_tank', 'TANK VODE (l)'),
        ('cabins', 'BROJ KABINA'),
        ('speed', 'BRZINA'),
    ])

    value = models.CharField(max_length=255)
    published = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.get_name_display()}: {self.value}"


class Yacht(models.Model):
    YACHT_TYPE_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    name = models.CharField(max_length=255, verbose_name="Naziv jahte")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Cena (€)")
    yacht_type = models.CharField(max_length=10, choices=YACHT_TYPE_CHOICES, verbose_name="Tip jahte", default="used")
    description = models.TextField(blank=True, verbose_name="Opis jahte")
    image = models.ImageField(upload_to='yachts/', blank=True, null=True, verbose_name="Slika jahte")
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


    def __str__(self):
        return f"{self.name} ({self.get_yacht_type_display()})"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    @property
    def get_image_urls(self):
        image_urls = [self.image.url]  # Include the main image URL
        image_urls.extend(f"{settings.MEDIA_URL}{img.image.name}" for img in self.images.all())
        return json.dumps(image_urls)


class SectionTemplate(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SubSectionTemplate(models.Model):
    section_template = models.ForeignKey(SectionTemplate, on_delete=models.CASCADE, related_name='subsections')
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.section_template.title} > {self.title}"


class DetailTemplate(models.Model):
    subsection_template = models.ForeignKey(SubSectionTemplate, on_delete=models.CASCADE, related_name='details')
    label = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.subsection_template.title} - {self.label}"



class Section(models.Model):
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, related_name='yacht_sections')
    section_template = models.ForeignKey(SectionTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.yacht.name} - {self.section_template.title}"


class SubSection(models.Model):
    yacht_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='yacht_subsections')
    subsection_template = models.ForeignKey(SubSectionTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.yacht_section.yacht.name} > {self.subsection_template.title}"


class Detail(models.Model):
    yacht_subsection = models.ForeignKey(SubSection, on_delete=models.CASCADE, related_name='yacht_details')
    detail_template = models.ForeignKey(DetailTemplate, on_delete=models.CASCADE)
    value = models.TextField(blank=True, null=True)  # konkretna vrednost za tu jahtu

    def __str__(self):
        return f"{self.yacht_subsection.yacht_section.yacht.name} - {self.detail_template.label}: {self.value}"



class Image(models.Model):
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='yacht_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.yacht.name} - {self.id}"
