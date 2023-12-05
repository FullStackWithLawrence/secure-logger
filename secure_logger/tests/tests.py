# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Simple test bank."""
import json
import logging
import sys
import unittest


sys.path.append("../")  # noqa: E402

from secure_logger.decorators import (  # noqa: E402, pylint: disable=wrong-import-position
    secure_logger,
)
from secure_logger.masked_dict import (  # noqa: E402, pylint: disable=wrong-import-position
    DEFAULT_REDACTION_MESSAGE,
    masked_dict,
    masked_dict2str,
)


###############################################################################
#                                 TEST BANK
###############################################################################
class TestMaskedDict(unittest.TestCase):
    """Test the masked_dict function."""

    test_dict = {
        "insensitive_key": "you-can-see-me",
        "aws_access_key_id": "i-am-hidden",
        "aws_secret_access_key": "so-am-i",
    }
    expected_dict = {
        "insensitive_key": "you-can-see-me",
        "aws_access_key_id": DEFAULT_REDACTION_MESSAGE,
        "aws_secret_access_key": DEFAULT_REDACTION_MESSAGE,
    }

    def test_masked_dict(self):
        """Test the masked_dict function."""
        md = masked_dict(self.test_dict)
        self.assertDictEqual(md, self.expected_dict)

    def test_masked_dict2str(self):
        """Test the masked_dict2str function."""
        md2s = masked_dict2str(self.test_dict)
        md2s_to_json = json.loads(md2s)
        self.assertDictEqual(md2s_to_json, self.expected_dict)


class TestMaskedDictCaseSensitivity(unittest.TestCase):
    """Test the masked_dict function with case sensitivity."""

    test_dict = {
        "insensitive_key": "you-can-see-me",
        "AWs_AcCEss_KeY_iD": "i-am-very-hidden",
        "AWS_SECRET_ACCESS_KEY": "so-am-i",
    }
    expected_dict = {
        "insensitive_key": "you-can-see-me",
        "AWs_AcCEss_KeY_iD": DEFAULT_REDACTION_MESSAGE,
        "AWS_SECRET_ACCESS_KEY": DEFAULT_REDACTION_MESSAGE,
    }

    def test_masked_dict(self):
        """Test the masked_dict function."""
        md = masked_dict(self.test_dict)
        self.assertDictEqual(md, self.expected_dict)

    def test_masked_dict2str(self):
        """Test the masked_dict2str function."""
        md2s = masked_dict2str(self.test_dict)
        md2s_to_json = json.loads(md2s)
        self.assertDictEqual(md2s_to_json, self.expected_dict)


class TestCustomParams(unittest.TestCase):
    """Test the masked_dict function with custom parameters."""

    visible_value = "i should be visible"
    custom_keys = ["foo", "bar"]
    custom_message = "--REDACTED--"
    test_dict = {"foo": "i should be hidden", "bar": "me too", "visible_key": visible_value}

    def test_custom_keys(self):
        """Test the masked_dict function with custom keys."""
        expected_result = {
            "foo": DEFAULT_REDACTION_MESSAGE,
            "bar": DEFAULT_REDACTION_MESSAGE,
            "visible_key": self.visible_value,
        }
        masked_test_dict = masked_dict(self.test_dict, self.custom_keys)
        self.assertDictEqual(masked_test_dict, expected_result)

    def test_custom_keys_and_message(self):
        """Test the masked_dict function with custom keys and message."""
        expected_result = {"foo": self.custom_message, "bar": self.custom_message, "visible_key": self.visible_value}
        masked_test_dict = masked_dict(self.test_dict, self.custom_keys, self.custom_message)
        self.assertDictEqual(masked_test_dict, expected_result)


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
            "INFO:secure_logger.decorators:secure_logger: tests.tests.mock_decorated_def() "
            "['<tests.tests.TestModuleDefDecorator testMethod=test_decorator_output>', " + hello_world
        )
        with self.assertLogs(level=logging.DEBUG) as cm:
            self.mock_decorated_def("hello world")

        self.assertEqual(cm.output[0][0:100], expected_output[0:100])


class TestClassMethodDecorator(unittest.TestCase):
    """Test class method logging."""

    class MockClass:
        """Test class method logging."""

        @secure_logger()
        def decorator_with_defaults(self, test_dict, test_list):
            """Test class input parameter as objects."""

        @secure_logger(sensitive_keys=["aws_secret_access_key"], indent=10, message="-- Forbidden! --")
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
            "INFO:secure_logger.decorators:secure_logger: tests.tests.decorator_with_defaults() "
            "['<tests.tests.TestClassMethodDecorator.MockClass"
        )

        with self.assertLogs(level=logging.DEBUG) as cm:
            self.mock_class.decorator_with_defaults(self.test_dict, self.test_list)

        self.assertEqual(cm.output[0][0:100], expected_output[0:100])


class TestClassDecorator(unittest.TestCase):
    """Test class logging."""

    def test_class_with_default_params(self):
        """Test class with default parameters."""

        @secure_logger()
        class MockDecoratedClass:
            """Test 3: decorate a class."""

        expected_output = "INFO:secure_logger.decorators:secure_logger: tests.tests.MockDecoratedClass.  "

        with self.assertLogs(level=logging.DEBUG) as cm:
            MockDecoratedClass()

        self.assertEqual(cm.output[0][0:100], expected_output[0:100])


if __name__ == "__main__":
    unittest.main()
