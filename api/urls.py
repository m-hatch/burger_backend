from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.contrib import admin

from api.views import BurgerViewset, ToppingViewset

# router = DefaultRouter()


router = SimpleRouter()
router.register(r'api/burgers', BurgerViewset, base_name='burgers')
router.register(r'api/toppings', ToppingViewset, base_name='toppings')


urlpatterns = [
    url(r'^', include(router.urls))
]
