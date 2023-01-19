from django.contrib import admin

from .models import Factory, Distributor, Dealership, Retail, Entrepreneur


class BaseAdmin(admin.ModelAdmin):
    search_fields = ("address.city",)


admin.site.register(Factory)
admin.site.register(Distributor)
admin.site.register(Dealership)
admin.site.register(Retail)
admin.site.register(Entrepreneur)

