import unittest
from modules.ring import Ring

class TestRing(unittest.TestCase):

    def test_modulo_addition(self):
        r = Ring(modulo=5)
        self.assertEqual(r.add(2, 3), 0)
        self.assertEqual(r.add(1, 4), 0)
        self.assertEqual(r.add(3, 3), 1)

    def test_modulo_multiplication(self):
        r = Ring(modulo=5)
        self.assertEqual(r.mul(2, 3), 1)
        self.assertEqual(r.mul(4, 2), 3)
        self.assertEqual(r.mul(3, 3), 4)

    def test_custom_addition(self):
        elements = ['a', 'b', 'c']
        add_table = [
            ['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']
        ]
        mul_table = [
            ['a', 'a', 'a'],
            ['a', 'b', 'c'],
            ['a', 'c', 'b']
        ]
        r = Ring(elements=elements, add_table=add_table, mul_table=mul_table)
        self.assertEqual(r.add('a', 'b'), 'b')
        self.assertEqual(r.add('b', 'c'), 'a')
        self.assertEqual(r.add('c', 'a'), 'c')

    def test_custom_multiplication(self):
        elements = ['a', 'b', 'c']
        add_table = [
            ['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']
        ]
        mul_table = [
            ['a', 'a', 'a'],
            ['a', 'b', 'c'],
            ['a', 'c', 'b']
        ]
        r = Ring(elements=elements, add_table=add_table, mul_table=mul_table)
        self.assertEqual(r.mul('a', 'b'), 'a')
        self.assertEqual(r.mul('b', 'b'), 'b')
        self.assertEqual(r.mul('b', 'c'), 'c')
        self.assertEqual(r.mul('c', 'c'), 'b')

if __name__ == '__main__':
    unittest.main()

