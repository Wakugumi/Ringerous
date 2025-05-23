import unittest
from modules.ring import Ring
from modules.checker import check_all_properties

class TestRingProperties(unittest.TestCase):

    def test_modulo_ring_properties(self):
        r = Ring(modulo=4)
        results = check_all_properties(r)

        self.assertTrue(results['Additive Associativity']['result'])
        self.assertTrue(results['Multiplicative Associativity']['result'])
        self.assertTrue(results['Additive Identity']['result'])
        self.assertTrue(results['Additive Inverse']['result'])
        self.assertTrue(results['Distributivity']['result'])

        # Modulo rings are not guaranteed to have multiplicative identity unless modulo is prime
        self.assertEqual(results['Multiplicative Identity']['result'], True)

    def test_custom_ring_properties(self):
        elements = ['0', '1', '2']
        add_table = [
            ['0', '1', '2'],
            ['1', '2', '0'],
            ['2', '0', '1']
        ]
        mul_table = [
            ['0', '0', '0'],
            ['0', '1', '2'],
            ['0', '2', '1']
        ]
        r = Ring(elements=elements, add_table=add_table, mul_table=mul_table)
        results = check_all_properties(r)

        self.assertTrue(results['Additive Associativity']['result'])
        self.assertTrue(results['Multiplicative Associativity']['result'])
        self.assertTrue(results['Additive Identity']['result'])
        self.assertTrue(results['Additive Inverse']['result'])
        self.assertTrue(results['Distributivity']['result'])

        # This custom ring has '1' as multiplicative identity
        self.assertTrue(results['Multiplicative Identity']['result'])

if __name__ == '__main__':
    unittest.main()

