# -*- coding: utf-8 -*-
import subprocess
import unittest


class TestSetup(unittest.TestCase):
    """Test setup.py."""

    def test_setup_syntax():
        """Test setup.py syntax."""
        result = subprocess.run(["python", "setup.py"], capture_output=True)
        assert (
            result.returncode == 0
        ), f"setup.py failed with output:\n{result.stdout.decode()}\n{result.stderr.decode()}"
        assert "MockDecoratedClass" in result.stdout.decode(), "Expected 'MockDecoratedClass' in output"


if __name__ == "__main__":
    unittest.main()
