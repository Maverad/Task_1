import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestIngredient:
    possible_types = [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE]

    @pytest.mark.parametrize('name', ['Ingredient', 'ингридиент', 'и', '', '123', 'иН грИдиент 2'])
    def test_name(self, name):
        ingr = Ingredient(ingredient_type= INGREDIENT_TYPE_FILLING, name = name, price=0)

        assert ingr.get_name() == name

    @pytest.mark.parametrize('price', [0, 0.1, 1, 99, 100, 999, 1000, 9999, 10000])
    def test_price(self, price):
        ingr = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='test', price=price)
                
        assert ingr.get_price() == price

    @pytest.mark.parametrize('type_ingr', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_type_presents_in_types(self, type_ingr):
        ingr = Ingredient(ingredient_type=type_ingr, name='test', price=0)

        assert ingr.get_type() in self.possible_types

    @pytest.mark.parametrize('type_ingr', ['some type', 'extra type', 'type'])
    def test_type_not_presents_in_types(self, type_ingr):
        ingr = Ingredient(ingredient_type=type_ingr, name='test', price=0)

        assert ingr.get_type() not in self.possible_types