import unittest

from models import Ball


class TestBall(unittest.TestCase):

	def setUp(self):
		self.ball1 = Ball((125, 125, 125), 2)
		self.ball2 = Ball((125, 125, 125), 2.0)
		self.ball3 = Ball((125, 125, 125), 3.1)
		self.ball4 = Ball((124, 124, 124), 2)
		self.point1 = (125, 124, 125)
		self.point2 = (120, 120, 120)
		self.point3 = (1.1, 200, 200)
		self.point4 = (100, -20, 2)

	def test_create(self):
		# Ball centre coords cannot be floats
		with self.assertRaises(TypeError):
			Ball((0.2, 100, 100), 10)
		# Ball centre must be between 0 and 255
		with self.assertRaises(ValueError):
			Ball((-5, 200, 200), 200)
		# Ball radius must be greater than 0
		with self.assertRaises(ValueError):
			Ball((100, 100, 100), -20)

		# Float radius should be equal to int radius
		self.assertEqual(self.ball1, self.ball2)
		# Balls are unequal if radii differ
		self.assertNotEqual(self.ball1, self.ball3)
		# Balls are unequal if centre differs
		self.assertNotEqual(self.ball1, self.ball4)

	def test_contains(self):
		# Point coords cannot be floats
		with self.assertRaises(TypeError):
			self.ball1.contains(self.point3)

		# Point coords outside 0 and 255 return false
		self.assertFalse(self.ball1.contains(self.point4))

		# Ball should contain point1
		self.assertTrue(self.ball1.contains(self.point1))

		# Ball should not contain point2
		self.assertFalse(self.ball1.contains(self.point2))


if __name__ == "__main__":
	unittest.main()