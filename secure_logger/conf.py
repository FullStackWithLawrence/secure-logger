# -*- coding: utf-8 -*-
"""Module conf.py"""

import logging

from pydantic import BaseModel, Field, ValidationError

from secure_logger.exceptions import SecureLoggerConfigurationError


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


class Settings(BaseModel):
    """Settings for secure_logger"""

    secure_logger_sensitive_keys: list = Field(_SECURE_LOGGER_SENSITIVE_KEYS, env="SECURE_LOGGER_SENSITIVE_KEYS")
    secure_logger_redaction_message: str = Field(
        _SECURE_LOGGER_REDACTION_MESSAGE, env="SECURE_LOGGER_REDACTION_MESSAGE"
    )
    secure_logger_indent: int = Field(_SECURE_LOGGER_INDENT, env="SECURE_LOGGER_INDENT")


settings = None
try:
    settings = Settings()
except ValidationError as e:
    raise SecureLoggerConfigurationError("Invalid configuration: " + str(e)) from e

logging.debug("SECURE_LOGGER_SENSITIVE_KEYS: %s", settings.secure_logger_sensitive_keys)
logging.debug("SECURE_LOGGER_REDACTION_MESSAGE: %s", settings.secure_logger_redaction_message)
logging.debug("SECURE_LOGGER_INDENT: %s", settings.secure_logger_indent)
