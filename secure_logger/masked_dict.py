# -*- coding: utf-8 -*-
"""Recursively masks the values of sensitive keys in a Dict."""

# python stuff
import json
from unittest.mock import MagicMock

# our stuff
DEFAULT_SENSITIVE_KEYS = [
    "password",
    "token",
    "client_id",
    "client_secret",
    "Authorization",
    "secret",
    "access_key_id",
    "secret_access_key",
    "access-key-id",
    "secret-access-key",
    "aws_access_key_id",
    "aws_secret_access_key",
    "aws-access-key-id",
    "aws-secret-access-key",
]
DEFAULT_REDACTION_MESSAGE = "*** -- REDACTED -- ***"
DEFAULT_INDENT = 4


class _JSONEncoder(json.JSONEncoder):
    """encode json object for serialization."""

    def default(self, obj):
        """Handle unit test, unicode, and anything else that might throw a wrench in things."""
        if isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        if isinstance(obj, MagicMock):
            return ""
        try:
            return json.JSONEncoder.default(self, obj)
        except Exception:  # noqa: B902
            # obj probably is not json serializable.
            return ""


def masked_dict(
    source_dict, sensitive_keys: list = DEFAULT_SENSITIVE_KEYS, message: str = DEFAULT_REDACTION_MESSAGE
) -> dict:
    """
    Mask sensitive key / value in log entries.

    Masks the value of specified key.
    obj: a dict or a string representation of a dict, or None
    """
    if type(source_dict) == str:
        source_dict = json.loads(source_dict)

    if type(source_dict) != dict:
        raise TypeError("source_dict must be a dict or a json serializable string")

    recursed_dict = {}
    for key in source_dict:
        value = source_dict[key]
        if type(value) == dict:
            value = masked_dict(source_dict=value, sensitive_keys=sensitive_keys, message=message)
        recursed_dict[key] = value

    for lower_case_sensitive_key in [x.lower() for x in sensitive_keys]:
        if lower_case_sensitive_key in [x.lower() for x in recursed_dict.keys()]:
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
