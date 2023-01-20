from django.urls import path
from rest_framework import routers

from .views import FactoryCreateView

# factory_router = routers.SimpleRouter()
# factory_router.register('factory', FactoryCreateView)

urlpatterns = [
    path("factory/create/", FactoryCreateView.as_view())
]


# urlpatterns += factory_router.urls
