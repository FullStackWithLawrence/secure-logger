# -*- coding: utf-8 -*-
"""Module conf.py"""

import logging

from pydantic import BaseModel, Field, ValidationError, constr, validator

from secure_logger.exceptions import SecureLoggerConfigurationError


LOGGER_NAME = "decorator_logger"

_logger = logging.getLogger(LOGGER_NAME)


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
_SECURE_LOGGER_LOG_LEVEL = "DEBUG"

# pylint: disable=protected-access
_SECURE_LOGGER_LOG_LEVELS = [level for level in logging._nameToLevel if level != "NOTSET"]


class Settings(BaseModel):
    """Settings for secure_logger"""

    secure_logger_sensitive_keys: list = Field(_SECURE_LOGGER_SENSITIVE_KEYS, env="SECURE_LOGGER_SENSITIVE_KEYS")
    secure_logger_redaction_message: str = Field(
        _SECURE_LOGGER_REDACTION_MESSAGE, env="SECURE_LOGGER_REDACTION_MESSAGE"
    )
    secure_logger_indent: int = Field(_SECURE_LOGGER_INDENT, env="SECURE_LOGGER_INDENT")
    secure_logger_logging_level: constr(min_length=4, max_length=8) = Field(
        _SECURE_LOGGER_LOG_LEVEL, env="SECURE_LOGGER_LOG_LEVEL"
    )

    @validator("secure_logger_logging_level")
    @classmethod
    def must_be_valid_log_level(cls, v):
        """Validate the log level"""
        if v not in _SECURE_LOGGER_LOG_LEVELS:
            raise ValueError("invalid log level")
        return v

    @property
    def logger(self):
        """Returns the logger function for the specified logging level"""
        log_levels = {
            "DEBUG": _logger.debug,
            "INFO": _logger.info,
            "WARNING": _logger.warning,
            "ERROR": _logger.error,
            "CRITICAL": _logger.critical,
        }
        return log_levels.get(self.secure_logger_logging_level, logging.debug)

    @property
    def logger_level(self) -> int:
        """Returns the logger level for the specified logging level"""
        # pylint: disable=protected-access
        return logging._nameToLevel.get(self.secure_logger_logging_level, logging.DEBUG)


settings = None
try:
    settings = Settings()
except ValidationError as e:
    raise SecureLoggerConfigurationError("Invalid configuration: " + str(e)) from e

_logger.debug("SECURE_LOGGER_SENSITIVE_KEYS: %s", settings.secure_logger_sensitive_keys)
_logger.debug("SECURE_LOGGER_REDACTION_MESSAGE: %s", settings.secure_logger_redaction_message)
_logger.debug("SECURE_LOGGER_INDENT: %s", settings.secure_logger_indent)
_logger.debug("SECURE_LOGGER_LOG_LEVEL: %s", settings.secure_logger_logging_level)
