# -*- coding: utf-8 -*-
"""
Lawrence McDaniel https://lawrencemcdaniel.com.

Python Secure Logger
"""
# python stuff
import inspect
from functools import wraps
import logging

# our stuff
from .masked_dict import serialized_masked_dict, DEFAULT_SENSITIVE_KEYS

# module initializations
logger = logging.getLogger(__name__)


def app_logger(sensitive_keys: list = DEFAULT_SENSITIVE_KEYS, indent: int = 4):
    """Top level decorator, for defining input parameters."""

    def decorate(func):
        """
        Decorate a Python a class, a class method, or a function.

        Adds a log entry with the module name, class name and method/function name,
        its positional arguments, and keyword pairs presented as a formatted dict.

        Sample output:
            2022-07-08 19:40:51,085 INFO app_logger: courses.views.CourseListingView().get_queryset()
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            name_of_module = ""
            name_of_class = ""
            name_of_def = ""
            logged_args = args
            kwargs_dict_repr = ""
            positional_args = []

            # case 1: a Class
            if inspect.isclass(func):
                name_of_module = func.__module__
                name_of_class = func.__name__
            else:
                # case 2: a class method
                if inspect.isclass(args[0]):
                    cls = args[0].__class__
                    name_of_module = cls.__module__
                    name_of_class = cls.__name__ + "()"
                    name_of_def = func.__name__
                    # slice off the 'self' positional argument
                    logged_args = args[1:]
                else:
                    # case 3: a function in a module.
                    name_of_module = func.__module__
                    name_of_class = ""
                    name_of_def = func.__name__

                positional_args = [repr(a) for a in logged_args]

            name_spec = name_of_module + "." if name_of_module else ""
            name_spec += name_of_class + "." if name_of_class else ""
            name_spec += name_of_def + "()" if name_of_def else ""

            if len(kwargs.keys()) > 0:
                kwargs_dict_repr = "keyword args: "
                kwargs_dict_repr += serialized_masked_dict(kwargs, sensitive_keys=sensitive_keys, indent=indent)

            logger.info(
                "app_logger: {name_spec} {args} {kwargs}".format(
                    name_spec=name_spec,
                    args=positional_args if len(positional_args) > 0 else "",
                    kwargs=kwargs_dict_repr,
                )
            )
            return func(*args, **kwargs)

        return wrapper

    return decorate
