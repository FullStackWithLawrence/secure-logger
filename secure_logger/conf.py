# -*- coding: utf-8 -*-
# pylint: disable=no-member
"""Configuration for secure_logger"""

import logging

from pydantic import BaseModel, Field, ValidationError, validator

from secure_logger.exceptions import SecureLoggerConfigurationError


LOGGER_NAME = "decorator_logger"
DEFAULT_SECURE_LOGGER_SENSITIVE_KEYS = [
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
DEFAULT_SECURE_LOGGER_REDACTION_MESSAGE = "*** -- secure_logger() -- ***"
DEFAULT_SECURE_LOGGER_INDENTATION = 4
DEFAULT_SECURE_LOGGER_LOG_LEVEL = "DEBUG"

# pylint: disable=protected-access
DEFAULT_SECURE_LOGGER_LOG_LEVELS = [level.upper() for level in logging._nameToLevel if level != "NOTSET"]


class Settings(BaseModel):
    """Settings for secure_logger"""

    class Config:
        """Pydantic configuration"""

        # necessary to allow logging.Logger
        arbitrary_types_allowed = True

    logger_name: str = Field(LOGGER_NAME.lower())
    logging_logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(LOGGER_NAME.lower()))
    sensitive_keys: list = Field(DEFAULT_SECURE_LOGGER_SENSITIVE_KEYS, env="SECURE_LOGGER_SENSITIVE_KEYS")
    redaction_message: str = Field(DEFAULT_SECURE_LOGGER_REDACTION_MESSAGE, env="SECURE_LOGGER_REDACTION_MESSAGE")
    indentation: int = Field(DEFAULT_SECURE_LOGGER_INDENTATION, gt=0, env="SECURE_LOGGER_INDENTATION")
    logging_level: str = Field(DEFAULT_SECURE_LOGGER_LOG_LEVEL, env="SECURE_LOGGER_LOG_LEVEL")

    @validator("logging_level")
    @classmethod
    def must_be_valid_log_level(cls, v):
        """Validate the log level"""
        if v not in DEFAULT_SECURE_LOGGER_LOG_LEVELS:
            raise ValueError("invalid log level")
        return v

    @property
    def logger(self):
        """Returns the logger function for the specified logging level"""
        return self.get_logger(self.logging_level)

    @property
    def logger_level_int(self) -> int:
        """Returns the logger level for the specified logging level"""
        # pylint: disable=protected-access
        return logging._nameToLevel.get(self.logging_level, logging.DEBUG)

    def get_logger(self, log_level):
        """Returns the logger function for the specified logging level"""
        log_levels = {
            "DEBUG": self.logging_logger.debug,
            "INFO": self.logging_logger.info,
            "WARNING": self.logging_logger.warning,
            "ERROR": self.logging_logger.error,
            "CRITICAL": self.logging_logger.critical,
        }
        return log_levels.get(log_level, logging.debug)


settings = None
try:
    settings = Settings()
except ValidationError as e:
    raise SecureLoggerConfigurationError("Invalid configuration: " + str(e)) from e

logger = logging.getLogger(LOGGER_NAME)
logger.debug("SECURE_LOGGER_SENSITIVE_KEYS: %s", settings.sensitive_keys)
logger.debug("SECURE_LOGGER_REDACTION_MESSAGE: %s", settings.redaction_message)
logger.debug("SECURE_LOGGER_INDENTATION: %s", settings.indentation)
logger.debug("SECURE_LOGGER_LOG_LEVEL: %s", settings.logging_level)
