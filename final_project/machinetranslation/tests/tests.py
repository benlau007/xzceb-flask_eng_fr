import unittest
from translator import english_to_french, french_to_english 

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertNotEqual(english_to_french('yes'), 'bonjour') 
        self.assertEqual(english_to_french('hello'), 'bonjour')   

    def test_f2e(self): 
        self.assertNotEqual(french_to_english('merci'), 'hello') 
        self.assertEqual(french_to_english('bonjour'), 'hello')

if __name__ == '__main__':
    unittest.main()
    