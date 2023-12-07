# -*- coding: utf-8 -*-
"""Simple test bank."""
import json
import unittest

from secure_logger.conf import settings
from secure_logger.masked_dict import masked_dict, masked_dict2str


###############################################################################
#                                 TEST BANK
###############################################################################


class TestMaskedDictCaseSensitivity(unittest.TestCase):
    """Test the masked_dict function with case sensitivity."""

    test_dict = {
        "insensitive_key": "you-can-see-me",
        "AWs_AcCEss_KeY_iD": "i-am-very-hidden",
        "AWS_SECRET_ACCESS_KEY": "so-am-i",
    }
    expected_dict = {
        "insensitive_key": "you-can-see-me",
        "AWs_AcCEss_KeY_iD": settings.redaction_message,
        "AWS_SECRET_ACCESS_KEY": settings.redaction_message,
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
