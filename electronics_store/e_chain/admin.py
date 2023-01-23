from django.contrib import admin

from .models.address import Address
from .models.contact import Contact
from .models.dealership import Dealership
from .models.distributor import Distributor
from .models.entrepreneur import Entrepreneur
from .models.factory import Factory
from .models.product import Product
from .models.retail import Retail


@admin.action(description='Clear the debt to the supplier for the selected objects.')
def clear_the_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class BaseAdmin(admin.ModelAdmin):
    list_filter = ('contacts__address__city',)
    ordering = ['title']
    actions = [clear_the_debt]


admin.site.register(Factory, BaseAdmin)
admin.site.register(Distributor, BaseAdmin)
admin.site.register(Dealership, BaseAdmin)
admin.site.register(Retail, BaseAdmin)
admin.site.register(Entrepreneur, BaseAdmin)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Product)
