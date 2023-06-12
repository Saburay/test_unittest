import unittest
import upper


class TestUpper(unittest.TestCase):
	"""docstring for TestUpper"""
	def test_one_word(self):
		text = 'hello!'
		result = upper.upper_text(text)
		self.assertEqual(result,'Hello!')

	def test_multyple_word(self):
		text = 'hello world!'
		result = upper.upper_text(text)
		self.assertEqual(result,'Hello World!')


if __name__ == '__main__':
    unittest.main()