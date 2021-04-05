import unittest

import calcuration


class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = calcuration.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        cal = calcuration.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double(5, '5')
