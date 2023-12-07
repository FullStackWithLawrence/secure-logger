# -*- coding: utf-8 -*-
"""Simple test bank."""
import unittest

from secure_logger.conf import settings
from secure_logger.decorators import secure_logger
from secure_logger.exceptions import SecureLoggerConfigurationError


###############################################################################
#                                 TEST BANK
###############################################################################


class TestClassMethodDecorator(unittest.TestCase):
    """Test class method logging."""

    class MockClass:
        """Test class method logging."""

        @secure_logger()
        def decorator_with_defaults(self, test_dict, test_list):
            """Test class input parameter as objects."""

        @secure_logger(
            log_level="INFO",
            sensitive_keys=["aws_secret_access_key"],
            indent=10,
            message="-- Forbidden! --",
        )
        def decorator_with_custom_params(self, test_dict, test_list):
            """Test class input parameter as objects."""

    test_dict = {
        "insensitive_key": "you-can-see-me",
        "aws_access_key_id": "i-am-hidden",
        "aws_secret_access_key": "so-am-i",
    }
    test_list = ["foo", "bar"]
    mock_class = MockClass()

    def test_class_method_with_default_params(self):
        """Test class method with default parameters."""
        expected_output = (
            settings.logging_level
            + ":decorator_logger:secure_logger: test_class_method_decorator.decorator_with_defaults() "
            "['<test_class_method_decorator.TestClassMethodDecorator.MockClass"
        )

        with self.assertLogs(logger=settings.logger_name, level=settings.logging_level_int) as cm:
            self.mock_class.decorator_with_defaults(self.test_dict, self.test_list)

        self.assertEqual(cm.output[0][0:100], expected_output[0:100])

    def test_class_method_with_custom_params(self):
        """Test class method with default parameters."""
        expected_output = (
            "INFO:decorator_logger:secure_logger: test_class_method_decorator.decorator_with_custom_params() "
            "['<test_class_method_decorator.TestClassMethodDecorator.MockClass"
        )
        with self.assertLogs(logger=settings.logger_name) as cm:
            self.mock_class.decorator_with_custom_params(self.test_dict, self.test_list)

        self.assertEqual(cm.output[0][0:100], expected_output[0:100])

    def test_method_with_illegal_decorator_input(self):
        """Test class method with illegal decorator input."""

        def create_mock_class():
            """Create a mock class with illegal decorator input."""

            class MockClass:
                """Mock class with illegal decorator input."""

                @secure_logger(indent=-1)
                def decorator_with_invalid_params(self):
                    """Test class input parameter as objects."""

            return MockClass()

        self.assertRaises(
            SecureLoggerConfigurationError,
            create_mock_class,
        )
