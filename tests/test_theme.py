import unittest

from models import Ball, Theme


class TestTheme(unittest.TestCase):

	def setUp(self):
		self.ball1 = Ball((1, 1, 1), 1)
		self.ball2 = Ball((90, 90, 90), 20)
		self.ball3 = Ball((100, 100, 100), 20)
		self.point1 = (110, 110, 110)
		self.point2 = (95, 95, 95)
		self.point3 = (200, 200, 200)

	def test_theme(self):
		# Create the theme
		theme = Theme("test")
		# Assert that the name is created correctly
		self.assertEqual(theme.name, "test")

		# Assert that adding a ball is done correctly
		theme.add(self.ball1)
		self.assertEqual(theme.balls, {self.ball1})

		# Assert that removing a ball is done correctly
		theme.add(self.ball2)
		theme.add(self.ball3)
		theme.remove(self.ball1)
		self.assertEqual(theme.balls, {self.ball2, self.ball3})

		# Assert that themes accurately check points
		# A point contained within exactly one ball should return True
		self.assertTrue(theme.contains(self.point1))
		# A point contained within more than one ball should return True
		self.assertTrue(theme.contains(self.point2))
		# A point contained within no balls should return False
		self.assertFalse(theme.contains(self.point3))


if __name__ == "__main__":
	unittest.main()