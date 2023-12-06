# -*- coding: utf-8 -*-
"""Python Secure Logger."""
# python stuff
import inspect
from functools import wraps

# our stuff
from secure_logger.conf import settings
from secure_logger.masked_dict import masked_dict2str


def secure_logger(
    log_level: str = settings.secure_logger_logging_level,
    sensitive_keys: list = settings.secure_logger_sensitive_keys,
    indent: int = settings.secure_logger_indent,
    message: str = settings.secure_logger_redaction_message,
):
    """Top level decorator, for defining input parameters."""

    def decorate(func):
        """
        Decorate a Python a class, a class method, or a function.

        Adds a log entry with the module name, class name and method/function name,
        its positional arguments, and keyword pairs presented as a formatted dict.

        Sample output: see README.md
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
                kwargs_dict_repr += masked_dict2str(
                    kwargs, sensitive_keys=sensitive_keys, indent=indent, message=message
                )

            if log_level == settings.secure_logger_logging_level:
                logger = settings.logger
            else:
                logger = settings.get_logger(log_level)

            logger(
                "secure_logger: %s %s %s",
                name_spec,
                positional_args if positional_args else "",
                kwargs_dict_repr,
            )
            return func(*args, **kwargs)

        return wrapper

    return decorate
