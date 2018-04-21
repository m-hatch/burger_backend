from rest_framework import viewsets

from rest_framework.response import Response

from api.models import Topping, Burger
from api.serializers import BurgerSerializer, ToppingSerializer
from api.filters import ToppingFilter

class BurgerViewset(viewsets.ModelViewSet):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer
    filter_backends = (ToppingFilter,)
    lookup_field = 'id'


class ToppingViewset(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
