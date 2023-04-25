# -*- coding: utf-8 -*-
"""
Simple test bank.

Test the three use cases that we care about.
"""
import logging

from secure_logger.decorators import secure_logger

logging.basicConfig(level=logging.DEBUG)

MY_SENSITIVE_KEYS = [
    "client_id",
    "client_secret",
    "aws_access_key_id",
    "aws_secret_access_key",
]


@secure_logger(sensitive_keys=MY_SENSITIVE_KEYS, indent=4)
def test_1(msg):
    """Test 1: a simple module function."""
    print("test 1: " + msg)  # noqa: T201


class TestClass(object):
    """Test class method logging."""

    @secure_logger()
    def test_2(self, test_dict, test_list):
        """Test class input parameter as objects."""
        pass


@secure_logger()
class Test3:
    """Test 3: decorate a class."""

    pass


if __name__ == "__main__":
    # test 1
    test_1("hello world")

    # test 2
    test_dict = {
        "insensitive_key": "you-can-see-me",
        "aws_access_key_id": "i-am-hidden",
        "aws_secret_access_key": "so-am-i",
    }
    test_list = ["foo", "bar"]
    o = TestClass()
    o.test_2(test_dict=test_dict, test_list=test_list)

    # test 3
    o = Test3()
