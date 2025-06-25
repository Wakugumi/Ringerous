import unittest
from modules.ring import Ring
from modules.checker import check_all_properties

class TestRingProperties(unittest.TestCase):

    # Assert testing for set Z_n where 1 <= n <= 99
    def test_modulo_ring_properties(self):

        for n in range(1, 100):
            r = Ring(modulo = n)
            results = check_all_properties(r)

            self.assertTrue(results['Additive Associativity']['result'])
            self.assertTrue(results['Multiplicative Associativity']['result'])
            self.assertTrue(results['Additive Identity']['result'])
            self.assertTrue(results['Additive Inverse']['result'])
            self.assertTrue(results['Distributivity']['result'])
            self.assertEqual(results['Multiplicative Identity']['result'], True)

    # Assert testing for custom ring, given multiplication table and addition table
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


    # Assert test for table that are not N x N for N is the number of elements in set
    def test_different_matrix_size(self):
        elements = ['0', '1']
        addition = [
                ['0', '1']
                ]
        multiplication = [
        ['1', '1'], ['1', '0']
        ]

        r = Ring(elements = elements, add_table = addition, mul_table = multiplication)

        self.assertRaises(Exception, check_all_properties, r)


if __name__ == '__main__':
    unittest.main()

