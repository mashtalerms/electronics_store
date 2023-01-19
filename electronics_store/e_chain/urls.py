from rest_framework import routers

from .views import FactoryViewSet

factory_router = routers.SimpleRouter()
factory_router.register('factory', FactoryViewSet)

urlpatterns = []


urlpatterns += factory_router.urls
