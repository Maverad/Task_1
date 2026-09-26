from unittest.mock import Mock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestDatabase:

    def test_available_buns(self):
        bun_1 = Bun('Простая булочка', 5)
        bun_2 = Bun('Загадочная булочка', 10)
        db = Database()
        db.available_buns = Mock(return_value=[bun_1, bun_2])
        result = db.available_buns()

        assert len(result) == 2
        assert result[0] is bun_1
        assert result[1] is bun_2

    def test_available_ingredients(self):
        ingr_1 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='test', price=5)
        ingr_2 = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='test_2', price=10)
        db = Database()
        db.available_ingredients = Mock(return_value=[ingr_1, ingr_2])
        result = db.available_ingredients()

        assert len(result) == 2
        assert result[0] is ingr_1
        assert result[1] is ingr_2