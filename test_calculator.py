#test_calculator.py
import unittest
import calculator

class calculaotrTest(unittest.TestCase):

	def test_mul(self):
		t_mul = calculator.mul(30, 20)
		self.assertEqual(t_mul, 600)

	if __name__ == '__main__':
		unittest.main()
