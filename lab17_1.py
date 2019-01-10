#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lab6_1 import triangle_square
import unittest

class LabTesting(unittest.TestCase):

    def test_triangle_345_square(self):
        self.assertEqual(triangle_square([3,4,5]), 6.0)
    
    def test_triangle_456_square(self):
        self.assertAlmostEqual(triangle_square([4,5,6]), 9.92156741, 6)

if __name__ == '__main__':
    unittest.main()
