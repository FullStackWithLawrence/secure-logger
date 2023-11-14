Secure Logger
=============

|Tests| |Source code| |PyPI releases| |License: AGPL v3| |hack.d
Lawrence McDaniel|

A Python decorator to generate redacted and nicely formatted log
entries. Works on all callables: class, class methods, Python module
functions. Recursively redacts Python dictionary key values based on a
customizable list of case-insensitive keys. Prevents your sensitive
application data like cloud provider key-pairs from leaking into your
application logs.

Usage
-----

As a decorator
~~~~~~~~~~~~~~

.. code:: python

   from secure_logger.decorators import secure_logger

   class Foo(object):

       @secure_logger()
       def bar(self, dict_data, list_data):
           pass

   # call your method, passing some sensitive data
   dict_data = {
       'not_a_sensitive_key': 'you-can-see-me',
       'aws-access-key_id': conf.AWS_ACCESS_KEY_ID,
       'aws-secret-access-key': conf.AWS_SECRET_ACCESS_KEY
   }
   list_data = ['foo', 'bar']
   foo = Foo()
   foo.bar(dict_data=dict_data, list_data=list_data)

Log output:

.. code:: log

   INFO:secure_logger: __main__.Foo().bar()  keyword args: {
       "dict_data": {
           "not_a_sensitive_key": "you-can-see-me",
           "aws-access-key-id": "*** -- secure_logger() -- ***",
           "aws-secret-access-key": "*** -- secure_logger() -- ***"
       },
       "list_data": [
           "foo",
           "bar"
       ]
   }

As library functions
~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from secure_logger.masked_dict import masked_dict, masked_dict2str

   dict_data = {
       'not_a_sensitive_key': 'you-can-see-me',
       'aws-access-key_id': conf.AWS_ACCESS_KEY_ID,
       'aws-secret-access-key': conf.AWS_SECRET_ACCESS_KEY
   }
   print(masked_dict2str(dict_data))

Output:

.. code:: bash

   {
       "not_a_sensitive_key": "you-can-see-me",
       "aws-access-key-id": "*** -- secure_logger() -- ***",
       "aws-secret-access-key": "*** -- secure_logger() -- ***"
   }

Installation
------------

.. code:: bash

   pip install secure-logger

Configuration
-------------

secure_logger accepts optional parameters.

-  sensitive_keys: a Python list of dictionary keys. Not case sensitive.
-  message: a string value that will replace the sensitive key values
-  indent: number of characters to indent JSON string output when
   logging output

.. code:: python

   class MyClass():

       @secure_logger(sensitive_keys=["password", "token", "crown_jewels"], message="***", indent=4)
       def another_def(self):
            pass

Configuration Defaults
----------------------

.. code:: python

   DEFAULT_REDACTION_MESSAGE = "*** -- secure_logger() -- ***"
   DEFAULT_INDENT = 4
   DEFAULT_SENSITIVE_KEYS = [
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

Contributing
~~~~~~~~~~~~

Pull requests are welcome, and you can also contact `Lawrence
McDaniel <https://lawrencemcdaniel.com/contact>`__ directly.

Getting Started With Local development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Use the same virtual environment that you use for edx-platform
-  Ensure that your Python interpreter to 3.11
-  install black: https://pypi.org/project/black/
-  install flake8: https://flake8.pycqa.org/en/latest/
-  install flake8-coding: https://pypi.org/project/flake8-coding/

.. code:: bash

   # Run these from within your edx-platform virtual environment
   python3 -m venv venv
   source venv/bin/activate

   pip install -r requirements/local.txt
   pip install pre-commit black flake8
   pre-commit install

Local development good practices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  run ``black`` on modified code before committing.
-  run
   ``flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics``
-  run
   ``flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics``
-  run ``pre-commit run --all-files`` before pushing. see:
   https://pre-commit.com/

.. |Tests| image:: https://github.com/lpm0073/secure-logger/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/lpm0073/secure-logger/actions
.. |Source code| image:: https://img.shields.io/static/v1?logo=github&label=Git&style=flat-square&color=brightgreen&message=Source%20code
   :target: https://github.com/lpm0073/secure-logger
.. |PyPI releases| image:: https://img.shields.io/pypi/v/secure-logger?logo=python&logoColor=white
   :target: https://pypi.org/project/secure-logger
.. |License: AGPL v3| image:: https://img.shields.io/badge/License-AGPL_v3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0
.. |hack.d Lawrence McDaniel| image:: https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg
   :target: https://lawrencemcdaniel.com
