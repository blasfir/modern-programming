import unittest
from rot13 import rot_13
class rot13testcase(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(rot_13("hello world"), "uryyb jbeyq")
    def test_uppercase(self):    
        self.assertEqual(rot_13("HELLO WORLD"), "URYYB JBEYQ")
    def test_spaces(self):    
        self.assertEqual(rot_13("  "), "  ")                
    def test_special_characters(self):
        with self.assertRaises(ValueError):
            rot_13("hello world!")
    def test_numbers(self):
        with self.assertRaises(ValueError):
            rot_13("hello world123")
if __name__ == "__main__":
    unittest.main() 