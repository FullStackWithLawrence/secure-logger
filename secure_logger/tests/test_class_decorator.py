# -*- coding: utf-8 -*-
"""Simple test bank."""
import unittest

from secure_logger.conf import settings
from secure_logger.decorators import secure_logger


###############################################################################
#                                 TEST BANK
###############################################################################


class TestClassDecorator(unittest.TestCase):
    """Test class logging."""

    def test_class_with_default_params(self):
        """Test class with default parameters."""

        @secure_logger()
        class MockDecoratedClass:
            """Test 3: decorate a class."""

        expected_output = (
            settings.logging_level + ":decorator_logger:secure_logger: test_class_decorator.MockDecoratedClass.  "
        )

        with self.assertLogs(level=settings.logging_level_int) as cm:
            MockDecoratedClass()

        self.assertEqual(cm.output[0][0:100], expected_output[0:100])
