
import unittest
import subprocess
import sys
from pathlib import Path

# Get the main project folder
project_folder = Path(__file__).resolve().parent.parent


class TestCodeMood(unittest.TestCase):

    def test_program_runs(self):
        # Run CodeMood on the sample Python file
        result = subprocess.run(
            [
                sys.executable,
                str(project_folder / "codemood.py"),
                str(project_folder / "sample.py")
            ],
            capture_output=True,
            text=True
        )

        # Make sure the program runs without errors
        self.assertEqual(result.returncode, 0)

        # Check that CodeMood prints its name
        self.assertIn("CodeMood", result.stdout)


if __name__ == "__main__":
    unittest.main()
