from django.urls import path, include
from rest_framework import routers

from .views.address import AddressViewSet
from .views.contact import ContactViewSet
from .views.dealership import DealershipViewSet
from .views.distributor import DistributorViewSet
from .views.entrepreneur import EntrepreneurViewSet
from .views.factory import FactoryViewSet
from .views.product import ProductViewSet
from .views.retail import RetailViewSet

address_router = routers.SimpleRouter()
address_router.register("address", AddressViewSet)

contact_router = routers.SimpleRouter()
contact_router.register("contact", ContactViewSet)

product_router = routers.SimpleRouter()
product_router.register("product", ProductViewSet)

factory_router = routers.SimpleRouter()
factory_router.register("factory", FactoryViewSet)

dealership_router = routers.SimpleRouter()
dealership_router.register("dealership", DealershipViewSet)

distributor_router = routers.SimpleRouter()
distributor_router.register("distributor", DistributorViewSet)

entrepreneur_router = routers.SimpleRouter()
entrepreneur_router.register("entrepreneur", EntrepreneurViewSet)

retail_router = routers.SimpleRouter()
retail_router.register("retail", RetailViewSet)


urlpatterns = [
    path("", include(address_router.urls)),
    path("", include(contact_router.urls)),
    path("", include(product_router.urls)),
    path("", include(factory_router.urls)),
    path("", include(dealership_router.urls)),
    path("", include(distributor_router.urls)),
    path("", include(entrepreneur_router.urls)),
    path("", include(retail_router.urls)),
]
