#from rest_framework import status
#from rest_framework.mixins import CreateModeMixin
#from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
