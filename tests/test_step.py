import unittest
from Step import *

class TestStep(unittest.TestCase):

  def test_num(self):
      self.assertEqual(step(Expr()))

if __name__ == '__main__':
    unittest.main()