# -*- coding: utf-8 -*-
"""Simple test bank."""
import json
import unittest

from secure_logger.conf import settings
from secure_logger.masked_dict import masked_dict, masked_dict2str


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
        "aws_access_key_id": settings.redaction_message,
        "aws_secret_access_key": settings.redaction_message,
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
