import unittest
import chapter06_02 as calc


class ModuleTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 5), 10)


if __name__ == '__main__':
    unittest.main()
