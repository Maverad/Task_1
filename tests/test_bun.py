import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize('name', ['Bulochka', 'булочка', 'б', '', '123', 'bU Лочка 2'])
    def test_get_name(self, name):
        bun = Bun(name, 52)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [0, 0.1, -1, 1, 99, 100, 999, 1000, 9999, 10000])
    def test_get_price(self, price):
        bun = Bun('test', price)
        
        assert bun.get_price() == price

  