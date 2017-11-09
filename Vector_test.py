import Vector
import unittest
import math
class Vector_Test(unittest.TestCase):
    def test_angle(self):
        vector = Vector.Vector(12,5)
        print(vector.getAngle())
        self.assertAlmostEqual(math.floor(vector.getAngle()), 22)

    def test_magnitude(self):
        vector = Vector.Vector(12, 5)
        self.assertEqual(math.floor(vector.getMagnitude()), 13)