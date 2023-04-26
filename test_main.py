"""Test file for testing the main.py file"""

import unittest
import io # for capturing the output
import sys # for restoring the stdout
import importlib # for importing the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def test_print_oi_mundo(self):
        """Testa se o programa imprime "oi mundo!" na tela"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertEqual("oi mundo!", captured_output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
