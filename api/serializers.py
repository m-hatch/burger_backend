from rest_framework import serializers

from api.models import Burger, Topping


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name',)


class BurgerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    has_bun = serializers.BooleanField()
    has_patty = serializers.BooleanField()
    toppings = ToppingSerializer(many=True, read_only=True)

    class Meta:
        model = Burger
        fields = ('id', 'name', 'has_bun', 'has_patty', 'toppings')

    def _get_toppings(self, toppings):
        topping_objects = []
        if toppings:
            for topping in toppings:
                topping_objects.append(Topping.objects.get(name=topping.get('name')))
        return topping_objects

    def save(self, *args, **kwargs):
        toppings = self._get_toppings(self.initial_data.get('toppings'))
        super(BurgerSerializer, self).save(**kwargs)
        for topping in toppings:
            self.instance.toppings.add(topping)
        self.instance.save()
