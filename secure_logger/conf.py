# -*- coding: utf-8 -*-
"""Module conf.py"""

import logging

from decouple import config

from secure_logger.exceptions import ConfigurationError


_DEFAULT_SENSITIVE_KEYS = [
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
_DEFAULT_REDACTION_MESSAGE = "*** -- secure_logger() -- ***"
_DEFAULT_INDENT = 4

DEFAULT_SENSITIVE_KEYS = config("DEFAULT_SENSITIVE_KEYS", default=_DEFAULT_SENSITIVE_KEYS, cast=list)
DEFAULT_REDACTION_MESSAGE = config("DEFAULT_REDACTION_MESSAGE", default=_DEFAULT_REDACTION_MESSAGE)
DEFAULT_INDENT = config("DEFAULT_INDENT", default=_DEFAULT_INDENT, cast=int)

if not isinstance(DEFAULT_SENSITIVE_KEYS, list):
    raise ConfigurationError("DEFAULT_SENSITIVE_KEYS must be a list")
if not isinstance(DEFAULT_REDACTION_MESSAGE, str):
    raise ConfigurationError("DEFAULT_REDACTION_MESSAGE must be a string")
if not isinstance(DEFAULT_INDENT, int):
    raise ConfigurationError("DEFAULT_INDENT must be an integer")

logging.debug("DEFAULT_SENSITIVE_KEYS: %s", DEFAULT_SENSITIVE_KEYS)
logging.debug("DEFAULT_REDACTION_MESSAGE: %s", DEFAULT_REDACTION_MESSAGE)
logging.debug("DEFAULT_INDENT: %s", DEFAULT_INDENT)
