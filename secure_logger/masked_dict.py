# -*- coding: utf-8 -*-
"""Recursively masks the values of sensitive keys in a Dict."""

# python stuff
import json
from unittest.mock import MagicMock

from secure_logger.conf import (
    DEFAULT_INDENT,
    DEFAULT_REDACTION_MESSAGE,
    DEFAULT_SENSITIVE_KEYS,
)


class _JSONEncoder(json.JSONEncoder):
    """encode json object for serialization."""

    def default(self, o):
        """Handle unit test, unicode, and anything else that might throw a wrench in things."""
        if isinstance(o, bytes):
            return str(o, encoding="utf-8")
        if isinstance(o, MagicMock):
            return ""
        try:
            return json.JSONEncoder.default(self, o)
        except Exception:  # pylint: disable=broad-except
            # o probably is not json serializable.
            return ""


def masked_dict(
    source_dict, sensitive_keys: list = DEFAULT_SENSITIVE_KEYS, message: str = DEFAULT_REDACTION_MESSAGE
) -> dict:
    """
    Mask sensitive key / value in log entries.

    Masks the value of specified key.
    obj: a dict or a string representation of a dict, or None
    """
    if isinstance(source_dict, str):
        source_dict = json.loads(source_dict)

    if not isinstance(source_dict, dict):
        raise TypeError("source_dict must be a dict or a json serializable string")

    recursed_dict = {}
    for key in source_dict:
        value = source_dict[key]
        if isinstance(value, dict):
            value = masked_dict(source_dict=value, sensitive_keys=sensitive_keys, message=message)
        recursed_dict[key] = value

    for lower_case_sensitive_key in [x.lower() for x in sensitive_keys]:
        if lower_case_sensitive_key in [x.lower() for x in recursed_dict]:
            for original_key in recursed_dict:
                if original_key.lower() == lower_case_sensitive_key:
                    recursed_dict[original_key] = message
    return recursed_dict


def masked_dict2str(
    obj: dict,
    sensitive_keys: list = DEFAULT_SENSITIVE_KEYS,
    indent: int = DEFAULT_INDENT,
    message: str = DEFAULT_REDACTION_MESSAGE,
) -> str:
    """Return a JSON encoded string representation of a masked dict."""
    return json.dumps(masked_dict(obj, sensitive_keys, message=message), cls=_JSONEncoder, indent=indent)


def serialized_masked_dict(
    obj: dict, sensitive_keys: list = DEFAULT_SENSITIVE_KEYS, indent: int = DEFAULT_INDENT
) -> str:
    """Backwards compatibility to 0.1.2 and prior."""
    return masked_dict2str(obj, sensitive_keys=sensitive_keys, indent=indent)
