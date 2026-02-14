import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(1, 5), -4)
        self.assertEqual(calculator.subtract(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(0, 5), 0)
    
    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        self.assertEqual(calculator.divide(10, 0), "Ошибка: деление на ноль!")

if __name__ == '__main__':
    unittest.main()
