import unittest
from task1.task1_hashmap import HashmapStructure


class TestHashmapStructure(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashmapStructure(1)
        self.vm_data_1 = {'Total Sales': 100, 'Items Sold': 50, 'Revenue Generated': 500}
        self.vm_data_2 = {'Total Sales': 200, 'Items Sold': 100, 'Revenue Generated': 1000}

    def test_put_and_get(self):
        self.hash_table.put('VM001', self.vm_data_1)
        self.assertEqual(self.hash_table.get('VM001'), self.vm_data_1)

    def test_put_collision(self):
        self.hash_table.put('VM001', self.vm_data_1)
        self.hash_table.put('VM002', self.vm_data_2)
        self.assertEqual(self.hash_table.get('VM001'), self.vm_data_1)
        self.assertEqual(self.hash_table.get('VM002'), self.vm_data_2)

    def test_remove(self):
        self.hash_table.put('VM001', self.vm_data_1)
        self.hash_table.remove('VM001')
        self.assertIsNone(self.hash_table.get('VM001'))

    def test_keys(self):
        self.hash_table.put('VM001', self.vm_data_1)
        self.hash_table.put('VM002', self.vm_data_2)
        keys = self.hash_table.keys()
        self.assertIn('VM001', keys)
        self.assertIn('VM002', keys)

    def test_values(self):
        self.hash_table.put('VM001', self.vm_data_1)
        self.hash_table.put('VM002', self.vm_data_2)
        values = self.hash_table.values()
        self.assertIn(self.vm_data_1, values)
        self.assertIn(self.vm_data_2, values)

    def test_size(self):
        self.assertEqual(self.hash_table.count(), 0)
        self.hash_table.put('VM001', self.vm_data_1)
        self.assertEqual(self.hash_table.count(), 1)
        self.hash_table.put('VM002', self.vm_data_2)
        self.assertEqual(self.hash_table.count(), 2)
        self.hash_table.remove('VM001')
        self.assertEqual(self.hash_table.count(), 1)


if __name__ == '__main__':
    unittest.main()
