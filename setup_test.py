# -*- coding: utf-8 -*-
import subprocess
import pytest


def test_setup_py():
    """Test that setup.py runs without errors."""
    try:
        subprocess.check_call(["python", "setup.py"])
    except subprocess.CalledProcessError as e:
        pytest.fail(f"setup.py failed with error code {e.returncode}")
