from rest_framework.filters import BaseFilterBackend
from django.core.exceptions import ObjectDoesNotExist

from api.models import Burger, Topping


class ToppingFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # print request.META('topping')
        topping = request.META.get('topping')
        if topping:
            try:
                topping_obj = Topping.objects.get(name=topping)
                queryset = queryset.filter(toppings=topping_obj)
            except ObjectDoesNotExist:
                return Burger.objects.none()

        return queryset
