# -*- coding: utf-8 -*-
"""Simple test bank."""
import json
import unittest

from secure_logger.conf import settings
from secure_logger.decorators import secure_logger


class TestModuleDefDecorator(unittest.TestCase):
    """Test module function logging."""

    @secure_logger()
    def mock_decorated_def(self, msg):
        """Test 1: a simple module function."""

    def test_decorator_output(self):
        """Test 1: a simple module function."""
        hello_world = json.dumps(["'hello world'"])
        hello_world = "'hello world'"

        # noqa: C0301
        expected_output = (
            settings.logging_level + ":decorator_logger:secure_logger: test_function_decorator.mock_decorated_def() "
            "['<test_function_decorator.TestModuleDefDecorator testMethod=test_decorator_output>', " + hello_world
        )
        with self.assertLogs(logger=settings.logger_name, level=settings.logging_level_int) as cm:
            self.mock_decorated_def("hello world")

        self.assertEqual(cm.output[0][0:125], expected_output[0:125])
