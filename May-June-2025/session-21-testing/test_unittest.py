from calculator import add, sub
import unittest
class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1),2)
    
    def test_sub(self):
        self.assertEqual(sub(1,1),0)