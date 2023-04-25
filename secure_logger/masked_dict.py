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
    "aws_access_key_id",
    "aws_secret_access_key",
]


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


def masked_dict(obj, sensitive_keys: list = DEFAULT_SENSITIVE_KEYS) -> dict:
    """
    Mask sensitive key / value in log entries.

    Masks the value of specified key.
    obj: a dict or a string representation of a dict, or None
    """
    if type(obj) == str:
        obj = json.loads(obj)

    if type(obj) != dict:
        raise TypeError("obj must be a dict or a json serializable string")

    to_mask = {}
    for key in obj:
        value = obj[key]
        if type(value) == dict:
            value = masked_dict(value, sensitive_keys)
        to_mask[key] = value

    def redact(key: str, obj: dict) -> dict:
        if key in obj:
            obj[key] = "*** -- REDACTED -- ***"
        return obj

    for key in sensitive_keys:
        to_mask = redact(key, to_mask)
    return to_mask


def serialized_masked_dict(obj: dict, sensitive_keys: list = DEFAULT_SENSITIVE_KEYS, indent: int = 4) -> str:
    """Return a JSON encoded string representation of a masked dict."""
    to_serialize = {}
    for key in obj:
        value = obj[key]
        if type(value) == dict:
            value = masked_dict(value, sensitive_keys)
        to_serialize[key] = value

    return json.dumps(masked_dict(to_serialize, sensitive_keys=sensitive_keys), cls=_JSONEncoder, indent=indent)
