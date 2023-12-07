# -*- coding: utf-8 -*-
"""Simple test bank."""
import unittest

from secure_logger.conf import settings
from secure_logger.masked_dict import masked_dict


class TestCustomParams(unittest.TestCase):
    """Test the masked_dict function with custom parameters."""

    visible_value = "i should be visible"
    custom_keys = ["foo", "bar"]
    custom_message = "--REDACTED--"
    test_dict = {"foo": "i should be hidden", "bar": "me too", "visible_key": visible_value}

    def test_custom_keys(self):
        """Test the masked_dict function with custom keys."""
        expected_result = {
            "foo": settings.redaction_message,
            "bar": settings.redaction_message,
            "visible_key": self.visible_value,
        }
        masked_test_dict = masked_dict(self.test_dict, self.custom_keys)
        self.assertDictEqual(masked_test_dict, expected_result)

    def test_custom_keys_and_message(self):
        """Test the masked_dict function with custom keys and message."""
        expected_result = {"foo": self.custom_message, "bar": self.custom_message, "visible_key": self.visible_value}
        masked_test_dict = masked_dict(self.test_dict, self.custom_keys, self.custom_message)
        self.assertDictEqual(masked_test_dict, expected_result)
