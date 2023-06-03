import unittest
def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(10, 12), 22)

if __name__ == '__main__':
    unittest.main()
