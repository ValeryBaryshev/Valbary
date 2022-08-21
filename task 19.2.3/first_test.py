import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 6, 4) == 2

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 1, 4) == 5
