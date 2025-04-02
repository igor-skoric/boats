from django.contrib import admin
from .models import Yacht, Config



admin.site.register(Config)

@admin.register(Yacht)
class YachtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'year', 'yacht_type', 'created_at')
    list_filter = ('yacht_type', 'year')
    search_fields = ('name', 'description')
