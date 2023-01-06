import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(2, 2) == 4

    def test_adding_unsuccess(self):
        assert self.calc.adding(2, 2) != 5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')