import unittest
import sys
path = '/home/runner/work/AllInOneMD/AllInOneMD/src'
sys.path.append(path)
from main import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3, msg='add did not bring back 3 when given 1 and 2')