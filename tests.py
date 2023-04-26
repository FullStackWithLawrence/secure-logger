# -*- coding: utf-8 -*-
"""
Simple test bank.

Test the three use cases that we care about.
"""
import logging

from secure_logger.decorators import secure_logger
from secure_logger.masked_dict import masked_dict, masked_dict2str

logging.basicConfig(level=logging.DEBUG)

MY_SENSITIVE_KEYS = [
    "client_id",
    "client_secret",
    "aws_access_key_id",
    "aws_secret_access_key",
]


@secure_logger()
def test_1(msg):
    """Test 1: a simple module function."""
    print("test 1: " + msg)  # noqa: T201


class TestClass(object):
    """Test class method logging."""

    @secure_logger()
    def test_2(self, test_dict, test_list):
        """Test class input parameter as objects."""
        pass

    @secure_logger(sensitive_keys=["aws_secret_access_key"], indent=10, message="-- Forbidden! --")
    def test_4(self, test_dict, test_list):
        """Test class input parameter as objects."""
        pass


@secure_logger()
class Test3:
    """Test 3: decorate a class."""

    pass


if __name__ == "__main__":
    # test 1
    print("test 1 - default parameters on module function")  # noqa: T201
    test_1("hello world")

    # test 2
    print("test 2 - default parameters on class method")  # noqa: T201
    test_dict = {
        "insensitive_key": "you-can-see-me",
        "aws_access_key_id": "i-am-hidden",
        "aws_secret_access_key": "so-am-i",
    }
    test_list = ["foo", "bar"]
    o = TestClass()
    o.test_2(test_dict=test_dict, test_list=test_list)

    # test 3
    print("test 3 - default parameters on class definition")  # noqa: T201
    test3 = Test3()

    # test 4
    print("test 4 - custom parameters")  # noqa: T201
    o.test_4(test_dict=test_dict, test_list=test_list)

    # test 5
    print("test 5 - masked_dict() w defaults")  # noqa: T201
    print(masked_dict(test_dict))  # noqa: T201

    # test 6
    print("test 6 - masked_dict() with custom parameters")  # noqa: T201
    print(masked_dict(test_dict, sensitive_keys=["insensitive_key"], message=" -- SHAME ON YOU -- "))  # noqa: T201

    # test 7
    print("test 7 - masked_dict2str() w defaults")  # noqa: T201
    print(masked_dict2str(test_dict))  # noqa: T201

    # test 8
    print("test 8 - masked_dict2str() w custom parameters")  # noqa: T201
    md = masked_dict2str(test_dict, sensitive_keys=["insensitive_key"], message=" -- SHAME ON YOU -- ", indent=2)
    print(md)  # noqa: T201
