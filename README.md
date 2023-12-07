# Secure Logger

[![FullStackWithLawrence](https://a11ybadges.com/badge?text=FullStackWithLawrence&badgeColor=orange&logo=youtube&logoColor=282828)](https://www.youtube.com/@FullStackWithLawrence)
[![Python](https://a11ybadges.com/badge?logo=python)](https://www.python.org/)<br>
[![12-Factor](https://img.shields.io/badge/12--Factor-Compliant-green.svg)](./doc/Twelve_Factor_Methodology.md)
[![Unit Tests](https://github.com/FullStackWithLawrence/secure-logger/actions/workflows/tests.yml/badge.svg)](https://github.com/FullStackWithLawrence/secure-logger/actions)
![GHA pushMain Status](https://img.shields.io/github/actions/workflow/status/FullStackWithLawrence/secure-logger/pushMain.yml?branch=main)
![Auto Assign](https://github.com/FullStackwithLawrence/secure-logger/actions/workflows/auto-assign.yml/badge.svg)[![Source
code](https://img.shields.io/static/v1?logo=github&label=Git&style=flat-square&color=orange&message=Source%20code)](https://github.com/FullStackWithLawrence/secure-logger)
[![Release Notes](https://img.shields.io/github/release/FullStackWithLawrence/secure-logger)](https://github.com/FullStackWithLawrence/secure-logger/releases)
[![PyPI
releases](https://img.shields.io/pypi/v/secure-logger?logo=python&logoColor=white)](https://pypi.org/project/secure-logger)
[![License: AGPL
v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![hack.d Lawrence
McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

A Python decorator to generate redacted and nicely formatted log
entries. Works on all callables: class, class methods, Python module
functions. Recursively redacts Python dictionary key values based on a
customizable list of case-insensitive keys. Prevents your sensitive
application data like cloud provider key-pairs from leaking into your
application logs.

## Installation

```bash
pip install secure-logger
```

## Usage

### As a decorator

```python
from secure_logger.decorators import secure_logger
import logging

logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Foo(object):
    @secure_logger(log_level='INFO')
    def bar(self, dict_data, list_data):
        pass

# call your method, passing some sensitive data
dict_data = {
    "not_a_sensitive_key": "you-can-see-me",
    "aws-access-key-id": "i-am-hidden",
    "aws-secret-access-key": "so-am-i",
}
list_data = ["foo", "bar"]
foo = Foo()
foo.bar(dict_data=dict_data, list_data=list_data)
```

Log output:

```console
INFO:secure_logger: __main__.bar() ['<__main__.Foo object at 0x103474ac0>'] keyword args: {
    "dict_data": {
        "not_a_sensitive_key": "you-can-see-me",
        "aws-access-key-id": "*** -- secure_logger() -- ***",
        "aws-secret-access-key": "*** -- secure_logger() -- ***"
    },
    "list_data": [
        "foo",
        "bar"
    ]
```

### As library functions

```python
from secure_logger.masked_dict import masked_dict, masked_dict2str

dict_data = {
    'not_a_sensitive_key': 'you-can-see-me',
    'aws-access-key_id': conf.AWS_ACCESS_KEY_ID,
    'aws-secret-access-key': conf.AWS_SECRET_ACCESS_KEY
}
print(masked_dict2str(dict_data))
```

Output:

```bash
{
    "not_a_sensitive_key": "you-can-see-me",
    "aws-access-key-id": "*** -- secure_logger() -- ***",
    "aws-secret-access-key": "*** -- secure_logger() -- ***"
}
```

## Configuration

secure_logger accepts optional parameters which you can configure as either bash environment variables or with a .env file placed in the root of your project

- **SECURE_LOGGER_SENSITIVE_KEYS**: a Python list of dictionary keys. Not case sensitive.
- **SECURE_LOGGER_REDACTION_MESSAGE**: a string value that will replace the sensitive key values
- **SECURE_LOGGER_INDENTATION**: number of characters to indent JSON string output when logging output
- **SECURE_LOGGER_LOG_LEVEL**: the level at which secure_logger generates log entries. One of: 'CRITICAL', 'FATAL', 'ERROR', 'WARN', 'WARNING', 'INFO', 'DEBUG'

Additionally, you can override individual invocations of the decorator by passing _sensitive_keys_, _message_ and _indent_:

```python
class MyClass():

    @secure_logger(sensitive_keys=["password", "apikey", "crown_jewels"], message="*** -- TOP SECRET -- ***", indent=4)
    def another_function(self, password: str, apikey: str, crown_jewels: List(dict)):
         pass
```

## Configuration Defaults

```python
SECURE_LOGGER_REDACTION_MESSAGE = "*** -- secure_logger() -- ***"
SECURE_LOGGER_INDENTATION = 4
SECURE_LOGGER_SENSITIVE_KEYS = [
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
SECURE_LOGGER_LOG_LEVEL = 'DEBUG'
```

### Contributing

Pull requests are welcome, and you can also contact [Lawrence
McDaniel](https://lawrencemcdaniel.com/contact) directly.
