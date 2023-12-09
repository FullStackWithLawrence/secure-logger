# -*- coding: utf-8 -*-
"""Module exceptions.py"""


class SecureLoggerConfigurationError(Exception):
    """Exception raised for errors in the configuration."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
