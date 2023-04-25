# Secure Logger

[![Source code](https://img.shields.io/static/v1?logo=github&label=Git&style=flat-square&color=brightgreen&message=Source%20code)](https://github.com/lpm0073/secure-logger)
[![PyPI releases](https://img.shields.io/pypi/v/secure-logger?logo=python&logoColor=white)](https://pypi.org/project/secure-logger)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

A Python decorator to generate redacted and nicely formatted log entries of class instantiations, class method calls and standard Python function calls. Redacts function parameter values and dict values based on a customizable list.

Redacts the following values by default:

```python
DEFAULT_SENSITIVE_KEYS = [
    "password",
    "token",
    "client_id",
    "client_secret",
    "Authorization",
    "secret",
    "aws_access_key_id",
    "aws_secret_access_key",
]
```

## Installation

```bash
pip install secure-logger
```

## Usage

```python
from secure_logger.decorators import secure_logger

MY_SENSITIVE_KEYS = ["top-secret-password", "equally-secret-value",]

class TestClass(object):

    @secure_logger(sensitive_keys=MY_SENSITIVE_KEYS, indent=4)
    def test_2(self, test_dict, test_list):
        pass

test_dict = {
    'insensitive_key': 'you-can-see-me',
    'top-secret-password': 'i-am-hidden',
    'equally-secret-value': 'so-am-i'
}
test_list = ['foo', 'bar']
o = TestClass()
o.test_2(test_dict=test_dict, test_list=test_list)
```

Generates log entries of this style and form:

```log
INFO:secure_logger: __main__.TestClass().test_2()  keyword args: {
    "test_dict": {
        "insensitive_key": "you-can-see-me",
        "top-secret-password": "*** -- REDACTED -- ***",
        "equally-secret-value": "*** -- REDACTED -- ***"
    },
    "test_list": [
        "foo",
        "bar"
    ]
}
```

### Contributing

Pull requests are welcome, and you can also contact [Lawrence McDaniel](https://lawrencemcdaniel.com/contact) directly.

### Getting Started With Local development

- Use the same virtual environment that you use for edx-platform
- Ensure that your Python interpreter to 3.8x
- install black: <https://pypi.org/project/black/>
- install flake8: <https://flake8.pycqa.org/en/latest/>
- install flake8-coding: <https://pypi.org/project/flake8-coding/>

```bash
# Run these from within your edx-platform virtual environment
python3 -m venv venv
source venv/bin/activate

pip install -r requirements/local.txt
pip install pre-commit black flake8
pre-commit install
```

#### Local development good practices

- run `black` on modified code before committing.
- run `flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`
- run `flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics`
- run `pre-commit run --all-files` before pushing. see: <https://pre-commit.com/>
