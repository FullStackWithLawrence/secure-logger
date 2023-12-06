# -*- coding: utf-8 -*-
"""Module conf.py"""

import logging

from decouple import config

from secure_logger.exceptions import ConfigurationError


_SECURE_LOGGER_SENSITIVE_KEYS = [
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
_SECURE_LOGGER_REDACTION_MESSAGE = "*** -- secure_logger() -- ***"
_SECURE_LOGGER_INDENT = 4

SECURE_LOGGER_SENSITIVE_KEYS = config("SECURE_LOGGER_SENSITIVE_KEYS", default=_SECURE_LOGGER_SENSITIVE_KEYS, cast=list)
SECURE_LOGGER_REDACTION_MESSAGE = config("SECURE_LOGGER_REDACTION_MESSAGE", default=_SECURE_LOGGER_REDACTION_MESSAGE)
SECURE_LOGGER_INDENT = config("SECURE_LOGGER_INDENT", default=_SECURE_LOGGER_INDENT, cast=int)

if not isinstance(SECURE_LOGGER_SENSITIVE_KEYS, list):
    raise ConfigurationError("SECURE_LOGGER_SENSITIVE_KEYS must be a list")
if not isinstance(SECURE_LOGGER_REDACTION_MESSAGE, str):
    raise ConfigurationError("SECURE_LOGGER_REDACTION_MESSAGE must be a string")
if not isinstance(SECURE_LOGGER_INDENT, int):
    raise ConfigurationError("SECURE_LOGGER_INDENT must be an integer")

logging.debug("SECURE_LOGGER_SENSITIVE_KEYS: %s", SECURE_LOGGER_SENSITIVE_KEYS)
logging.debug("SECURE_LOGGER_REDACTION_MESSAGE: %s", SECURE_LOGGER_REDACTION_MESSAGE)
logging.debug("SECURE_LOGGER_INDENT: %s", SECURE_LOGGER_INDENT)
