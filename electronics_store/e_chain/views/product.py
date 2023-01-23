from rest_framework.viewsets import ModelViewSet

from ..models.product import Product
from ..permissions import IsActiveUser
from ..serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
