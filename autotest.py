import unittest
from modprlab1 import decrypt
class decrypttestcase(unittest.TestCase):
    def test_decrypt1(self):
        result = decrypt("uryyb jbeyq")
        self.assertEqual(result, "hello world")
    def test_decrypt2(self):
        result = decrypt("Uryyb Jbeyq")
        self.assertEqual(result, "Hello World")
    def test_decrypt3(self):
        result = decrypt(" ")
        self.assertEqual(result, " ")        

if __name__ == "__main__":
    unittest.main()        