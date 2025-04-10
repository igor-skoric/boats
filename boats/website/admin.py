from django.contrib import admin
from .models import Yacht, Config, Image, YachtCharacteristic, SectionTemplate, SubSectionTemplate, DetailTemplate, Section, SubSection, Detail
import nested_admin


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


# Inline formset za YachtCharacteristic
class YachtCharacteristicInline(admin.TabularInline):
    model = YachtCharacteristic
    extra = 1  # Broj praznih formi koji će biti prikazani za unos novih karakteristika
    fields = ('name', 'value')


@admin.register(Yacht)
class YachtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'yacht_type', 'created_at')
    list_filter = ['yacht_type']
    search_fields = ('name',)
    inlines = [ImageInline, YachtCharacteristicInline]



admin.site.register(Config)
admin.site.register(YachtCharacteristic)

# admin.site.register(YachtDetail)
# admin.site.register(YachtSubSection)
# admin.site.register(YachtSection)


class YachtDetailAdmin(nested_admin.NestedStackedInline):
    model = Detail
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "detail_template":
            if hasattr(request, "_subsection_") and request._subsection_:
                subsection = request._subsection_
                # Dodaj proveru da li subsection_template postoji
                if subsection.subsection_template_id:
                    print(db_field.name)
                    kwargs["queryset"] = DetailTemplate.objects.filter(
                        subsection_template=subsection.subsection_template
                    )
                else:
                    kwargs["queryset"] = DetailTemplate.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_formset(self, request, obj=None, **kwargs):
        request._subsection_ = obj  # čuvamo trenutni SubSection u request
        return super().get_formset(request, obj, **kwargs)



class YachtSubSectionInline(nested_admin.NestedStackedInline):
    model = SubSection
    extra = 1
    inlines = [YachtDetailAdmin]

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "subsection_template":
            if hasattr(request, "_obj_") and request._obj_ is not None:
                # Filtriramo samo podsekcije koje pripadaju trenutnom template-u
                kwargs["queryset"] = SubSectionTemplate.objects.filter(
                    section_template=request._obj_.section_template
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_formset(self, request, obj=None, **kwargs):
        request._obj_ = obj  # ovo koristimo kasnije u formfield_for_foreignkey
        return super().get_formset(request, obj, **kwargs)


@admin.register(Section)
class YachtSectionAdmin(nested_admin.NestedModelAdmin):
    inlines = [YachtSubSectionInline]


class DetailTemplateInline(nested_admin.NestedTabularInline):
    model = DetailTemplate
    extra = 1


class SubSectionTemplateInline(nested_admin.NestedStackedInline):
    model = SubSectionTemplate
    extra = 1
    inlines = [DetailTemplateInline]


@admin.register(SectionTemplate)
class SectionTemplateAdmin(nested_admin.NestedModelAdmin):
    inlines = [SubSectionTemplateInline]
    list_display = ('title',)