"""Test file for testing the main.py file"""

import unittest # for creating the test case
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file
from pathlib import Path # for getting the path of the main.py file

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
    # add the parent directory to the path in order to run it from the run command in vscode
    main_file_folder = Path(__file__).parents[1].as_posix() # pylint: disable=invalid-name
    sys.path.insert(0, main_file_folder)
    unittest.main()
