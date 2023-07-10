import unittest
from calculator_package.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        # Setting up an instance of the calculator
        self.calc = Calculator()
        
    def test_addition(self) -> None:
        # Testing the addition function
        self.calc.add(2)
        self.assertEqual(self.calc.memory, 2, 'Should be 2')

    def test_subtraction(self) -> None:
        # Testing the subtraction function
        self.calc.subtract(2)
        self.assertEqual(self.calc.memory, -2, 'Should be -2')

    def test_multiplication(self) -> None:
        # Testing the mulitplcation function
        self.calc.add(2)
        self.calc.multiply(3)
        self.assertEqual(self.calc.memory, 6, 'Should be 6')

    def test_division(self) -> None:
        # Testing the division function
        self.calc.add(10)
        self.calc.divide(2)
        self.assertEqual(self.calc.memory, 5, 'Should be 5')

    def test_root(self) -> None:
        # Testing the root function
        self.calc.add(16)
        self.calc.root(2)
        self.assertEqual(self.calc.memory, 4, 'Should be 4')

    def test_reset(self) -> None:
        # Testing the reset function
        self.calc.add(10)
        self.calc.reset()
        self.assertEqual(self.calc.memory, 0, 'Should be 10')

if __name__ == '__main__':
    unittest.main()