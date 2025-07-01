# -*- coding: utf-8 -*-
"""Setup for secure_logger package."""
from setuptools import find_packages, setup

from setup_utils import get_semantic_version  # pylint: disable=import-error
from setup_utils import load_readme


setup(
    name="secure-logger",
    version=get_semantic_version(),
    description="A decorator to generate redacted and nicely formatted log entries",
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    author="Lawrence McDaniel",
    author_email="lpm0073@gmail.com",
    maintainer="Lawrence McDaniel",
    maintainer_email="lpm0073@gmail.com",
    url="https://github.com/FullStackWithLawrence/secure-logger",
    license="GPL-3.0-or-later",
    license_files=("LICENSE.txt",),
    platforms=["any"],
    packages=find_packages(),
    package_data={
        "secure_logger": ["*.md"],
    },
    python_requires=">=3.6",
    install_requires=["pydantic>=2.5.0"],
    extras_require={},
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
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
        "Source": "https://github.com/FullStackWithLawrence/secure-logger",
        "Documentation": "https://pypi.org/project/secure-logger/",
        "Changelog": "https://github.com/FullStackWithLawrence/secure-logger/blob/main/CHANGELOG.md",
        "Security": "https://github.com/FullStackWithLawrence/secure-logger/blob/main/SECURITY.md",
        "Code of Conduct": "https://github.com/FullStackWithLawrence/secure-logger/blob/main/CODE_OF_CONDUCT.md",
        "Tracker": "https://github.com/FullStackWithLawrence/secure-logger/issues",
    },
)
