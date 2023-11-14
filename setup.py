# -*- coding: utf-8 -*-
"""Lawrence McDaniel https://lawrencemcdaniel.com."""
# pylint: disable=open-builtin
import io
import os
import sys
from setuptools import find_packages, setup, __version__ as setuptools_version
from distutils.command.install import INSTALL_SCHEMES
from distutils.command.install_data import install_data
from typing import Dict

HERE = os.path.abspath(os.path.dirname(__file__))

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if int(setuptools_version.split(".", 1)[0]) < 18:
    assert "bdist_wheel" not in sys.argv, "setuptools 18 or later is required for wheels."


class osx_install_data(install_data):
    """
    Fix macOS installation path.

    On MacOS, the platform-specific lib dir is at:
      /System/Library/Framework/Python/.../
    which is wrong. Python 2.5 supplied with MacOS 10.5 has an Apple-specific
    fix for this in distutils.command.install_data#306. It fixes install_lib
    but not install_data, which is why we roll our own install_data class.
    """

    def finalize_options(self):
        """
        Finalize options.

        By the time finalize_options is called, install.install_lib is set to
        the fixed directory, so we set the installdir to install_lib. The
        install_data class uses ('install_data', 'install_dir') instead.
        """
        self.set_undefined_options("install", ("install_lib", "install_dir"))
        install_data.finalize_options(self)


if sys.platform == "darwin":
    cmdclasses = {"install_data": osx_install_data}
else:
    cmdclasses = {"install_data": install_data}

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme["data"] = scheme["purelib"]


def load_readme() -> str:
    """Stringify the README."""
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        readme = f.read()
    # Replace img src for publication on pypi
    return readme.replace(
        "./doc/",
        "https://github.com/lpm0073/secure-logger/raw/main/doc/",
    )


def load_about() -> Dict[str, str]:
    """Stringify the __about__ module."""
    about: Dict[str, str] = {}
    with io.open(os.path.join(HERE, "__about__.py"), "rt", encoding="utf-8") as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


def load_version() -> Dict[str, str]:
    """Stringify the __about__ module."""
    version: Dict[str, str] = {}
    with io.open(os.path.join(HERE, "__version__.py"), "rt", encoding="utf-8") as f:
        exec(f.read(), version)  # pylint: disable=exec-used
    return version


def get_semantic_version() -> str:
    """
    Return the semantic version number.

    Note:
    - pypi does not allow semantic version numbers to contain a dash.
    - pypi does not allow semantic version numbers to contain a 'v' prefix.
    - pypi does not allow semantic version numbers to contain a 'next' suffix.
    """
    return VERSION["__version__"].replace("-next.", "a")


CHANGELOG = open(os.path.join(os.path.dirname(__file__), "CHANGELOG.md")).read()
ABOUT = load_about()
VERSION = load_version()

setup(
    name="secure-logger",
    version=get_semantic_version(),
    description="A decorator to generate redacted and nicely formatted log entries",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    author="Lawrence McDaniel",
    author_email="lpm0073@gmail.com",
    maintainer="Lawrence McDaniel",
    maintainer_email="lpm0073@gmail.com",
    url="https://github.com/lpm0073/secure-logger",
    license="AGPLv3",
    license_files=("LICENSE.txt",),
    platforms=["any"],
    packages=find_packages(),
    package_data={"": ["*.html"]},  # include any Mako templates found in this repo.
    include_package_data=True,
    cmdclass=cmdclasses,
    python_requires=">=3.6",
    install_requires=[],
    extras_require={},
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    keywords="logging, security, redaction",
    project_urls={
        "Source": "https://github.com/lpm0073/secure-logger",
        "Documentation": "https://pypi.org/project/secure-logger/",
        "Changelog": "https://github.com/lpm0073/secure-logger/blob/main/CHANGELOG.md",
        "Security": "https://github.com/lpm0073/secure-logger/blob/main/SECURITY.md",
        "Code of Conduct": "https://github.com/lpm0073/secure-logger/blob/main/CODE_OF_CONDUCT.md",
        "Tracker": "https://github.com/lpm0073/secure-logger/issues",
    },
)
