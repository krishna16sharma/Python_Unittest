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

print(current, parent)

from main import add

class TestAdd(unittest.TestCase):
    def runTest(self):
        sum = add(2, 3)
        self.assertEqual(sum, 5, "incorrect sum")

# run the test
if __name__ == '__main__':
    unittest.main()