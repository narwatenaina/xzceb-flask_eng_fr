import unittest
#from machinetranslation.translator import english_to_french,french_to_english
from translator import english_to_french, french_to_english


class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #self(english_to_french('Hello')) is not None

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #self(french_to_english('Hello')) is not None

 unittest.main()
 