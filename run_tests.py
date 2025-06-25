import os
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

unittest.TextTestRunner(verbosity=2).run(
    unittest.defaultTestLoader.discover("tests", pattern="test_*.py")
)
