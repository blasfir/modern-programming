import unittest
from modprlab1 import decrypt
class decrypttestcase(unittest.TestCase):
    def test_decrypt(self):
        result = decrypt("uryyb jbeyq")
        self.assertEqual(result, "hello world")

if __name__ == "__main__":
    unittest.main()        