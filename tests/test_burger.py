import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestBurger:

    def test_set_bun(self):
        burger = Burger()
        bun = Bun("Булочка", 5)
    
        burger.set_buns(bun)
    
        assert burger.bun is bun

    @pytest.mark.parametrize('type_ingr', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_add_ingredient(self, type_ingr):
        burger = Burger()
        ingr = Ingredient(ingredient_type=type_ingr, name='test', price=10)
        burger.add_ingredient(ingr)

        assert len(burger.ingredients) == 1
        assert ingr is burger.ingredients[0]

    @pytest.mark.parametrize('type_ingr', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_remove_ingredient(self, type_ingr):
        burger = Burger()
        ingr = Ingredient(ingredient_type=type_ingr, name='test', price=10)
        burger.add_ingredient(ingr)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingr_1 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='test_1', price=10)
        ingr_2 = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='test_2', price=5.5)
        burger.add_ingredient(ingr_1)
        burger.add_ingredient(ingr_2)
        burger.move_ingredient(0, 1)

        assert len(burger.ingredients) == 2
        assert ingr_1 is burger.ingredients[1]
        assert ingr_2 is burger.ingredients[0]

    def test_get_price_one_ingr(self):
        burger = Burger()
        bun = Bun('Булочка', 5)
        burger.set_buns(bun)
        ingr = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='test_1', price=10)
        burger.add_ingredient(ingr)

        assert burger.get_price() == 20
        
    def test_get_price_many_ingr(self):
        burger = Burger()
        bun = Bun('Булочка', 5)
        burger.set_buns(bun)
        ingr_1 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='test_1', price=10)
        ingr_2 = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='test_2', price=20)
        ingr_3 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='test_3', price=30)
        burger.add_ingredient(ingr_1)
        burger.add_ingredient(ingr_2)
        burger.add_ingredient(ingr_3)

        assert burger.get_price() == 70

    @pytest.mark.parametrize('type_ingr', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_get_receipt(self, type_ingr):
        burger = Burger()
        bun = Bun('Булочка', 5)
        burger.set_buns(bun)
        ingr = Ingredient(ingredient_type=type_ingr, name='mustard', price=10)
        burger.add_ingredient(ingr)
        receipt = burger.get_receipt()

        assert burger.ingredients[0].get_name() in receipt
        assert burger.ingredients[0].get_type().lower() in receipt
        assert bun.get_name() in receipt
