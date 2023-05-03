import unittest
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from main import add

from main import sub

class TestAdd(unittest.TestCase):
    def runTest(self):
        diff = sub(2, 3)
        self.assertEqual(diff, -1, "incorrect difference")

if __name__ == '__main__':
    unittest.main()