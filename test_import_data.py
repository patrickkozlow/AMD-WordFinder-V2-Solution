import unittest

import import_data


class TestCreateList(unittest.TestCase):
    def test_import_list(self):
        actual = import_data.create_list('wordfinder_v2/englishwords.txt')
        self.assertIsNotNone(actual)

    def test_list_len(self):
        actual = import_data.create_list('wordfinder_v2/englishwords.txt')
        self.assertEqual(len(actual), 124006)

    def test_list_aplhabet(self):
        actual = import_data.create_list('wordfinder_v2/englishwords.txt')
        for elem in actual:
            self.assertTrue(elem.isalpha())


class TestCreateGrid(unittest.TestCase):
    def test_grid_import(self):
        actual = import_data.create_grid('wordfinder_v2/grid.txt')
        self.assertIsNotNone(actual)

    def test_grid_content(self):
        actual = import_data.create_grid('wordfinder_v2/grid.txt')
        size = actual.pop(0)
        size = list(map(int, size))
        self.assertIsNotNone(size)

    def test_grid_size_equal(self):
        actual = import_data.create_grid('wordfinder_v2/grid.txt')
        size = actual.pop(0)
        size = list(map(int, size))
        self.assertEqual(size[0], size[1])

    def test_grid_size_row(self):
        actual = import_data.create_grid('wordfinder_v2/grid.txt')
        size = actual.pop(0)
        size = list(map(int, size))
        self.assertEqual(size[0], len(actual))

    def test_grid_size_test_col(self):
        actual = import_data.create_grid('wordfinder_v2/grid.txt')
        size = actual.pop(0)
        size = list(map(int, size))
        self.assertEqual(size[1], len(actual[0]))


if __name__ == '__main__':
    unittest.main()
