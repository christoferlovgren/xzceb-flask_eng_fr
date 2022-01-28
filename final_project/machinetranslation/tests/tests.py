import unittest

from translator import englishToFrench
from translator import frenchToEnglish

class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')

unittest.main()