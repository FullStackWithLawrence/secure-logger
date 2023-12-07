# Change Log

## v0.2.0 Draft Release Notes

- Add a config.Settings class with Pydantic validations and ability to configure at run-time via bash environment variable and/or a .env file.
- Add SecureLoggerConfigurationError exception class to raise exception in the event of any Pydantic and/or package data validation errors during configuration.
- add log_level input parameter to decorator to allow customization of the log level on individual log entries.
- Refactored setup.py to remove deprecated macOS functions.
- Add a security policy
- Add a contributor policy
- Added README badges to report live status of unit tests and CI/CD. Converted README to markdown.
- Add dependabot and mergify to periodically monitor and update PyPi and NPM requirements
- Add pre-commit with codespell, black, flake8, isort, pylint, bandit, tox, plus built-in pre-commit hooks for code style and security.
- Added the following Github Actions:
  - Auomated unit testing on push
  - Auto-assign new Issues
  - Periodic automated patch releases after Dependabot runs
  - Pull request automation
  - Semantic release
  - Automated merge of main to dev branches
- Add GitHub templates for Issue, Contributing, Funding, Pull Request
- Add the following to the Makefile
  - Recognition of .env file
  - Scaffold multi platform support
  - Make lint
  - Make help

## [0.1.18](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.17...v0.1.18) (2023-12-05)

### Bug Fixes

- add missing actions ([d2ea137](https://github.com/FullStackWithLawrence/secure-logger/commit/d2ea1376034fcd33b47a53da9cb15ad893448314))

## [0.1.17](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.16...v0.1.17) (2023-11-14)

### Bug Fixes

- add regex expressions to correctly evaluate all possible values of **version**.py ([1ac6246](https://github.com/FullStackWithLawrence/secure-logger/commit/1ac6246f4840457a62d6a7a6ccf03065c28643c7))
- restore npx semantic-release logic in next branch ([e8e4b1d](https://github.com/FullStackWithLawrence/secure-logger/commit/e8e4b1db87d3e04e8e263080ca8adc4fda989d86))

## [0.1.16](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.15...v0.1.16) (2023-11-14)

### Bug Fixes

- convert prerelease version to strict semantic equivalent ([f463db5](https://github.com/FullStackWithLawrence/secure-logger/commit/f463db5d53499166968fe0d9a36a36e3327d36d4))
- remove pre-commit ([12c3da0](https://github.com/FullStackWithLawrence/secure-logger/commit/12c3da0042cd7ff03783c278fddf1c3bb6b4f69a))
- set prerelease to true for next and nexst-major ([b830102](https://github.com/FullStackWithLawrence/secure-logger/commit/b8301020b57a5e1bc09517100d3d2724e9c7d716))

## [0.1.15](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.14...v0.1.15) (2023-11-14)

### Bug Fixes

- add npx semantic-release --dry-run --no-ci ([d0133ab](https://github.com/FullStackWithLawrence/secure-logger/commit/d0133ab6d966370b5eabf44e3543c81d3fe6b850))

## [0.1.14](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.13...v0.1.14) (2023-11-14)

### Bug Fixes

- fix requirements path for semantic release ([f2ad049](https://github.com/FullStackWithLawrence/secure-logger/commit/f2ad049e7a146a3eadc75606db87651c0e89e59a))
- must add next and next-major ([7434ecf](https://github.com/FullStackWithLawrence/secure-logger/commit/7434ecfc7e82cf3c6c9b2e771ea410883a722343))

## [0.1.13](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.12...v0.1.13) (2023-11-14)

### Bug Fixes

- long_description_content_type='text/x-rst' ([d551597](https://github.com/FullStackWithLawrence/secure-logger/commit/d551597c208b3de6d635947ae2247c755928816e))

## [0.1.12](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.11...v0.1.12) (2023-11-14)

### Bug Fixes

- refactor python code blocks using readme_renderer compliant directives ([49a3423](https://github.com/FullStackWithLawrence/secure-logger/commit/49a34234bb95ed37676f0620eb481a221302b73a))

## [0.1.11](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.10...v0.1.11) (2023-11-14)

### Bug Fixes

- CURRENT_VERSION was unassigned ([528fa71](https://github.com/FullStackWithLawrence/secure-logger/commit/528fa71dc0fc008bd7098686cab94198a961f5c3))

## [0.1.10](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.9...v0.1.10) (2023-11-14)

### Bug Fixes

- add a dedicated version bump workflow ([8c59680](https://github.com/FullStackWithLawrence/secure-logger/commit/8c596807fda14a7d1ec927267d68db776ef1d822))
- need to git pull ([24f177d](https://github.com/FullStackWithLawrence/secure-logger/commit/24f177da2ef4b70ba73c69b9c1c51133a6d29c3c))
- need to git pull ([2e60dbb](https://github.com/FullStackWithLawrence/secure-logger/commit/2e60dbbd5922649e0dc5b0177f145d49f7b476dd))
- need to git pull ([e173922](https://github.com/FullStackWithLawrence/secure-logger/commit/e173922d290eba66addda88f408aa0d576382214))
- remove version bump ([7b71ae9](https://github.com/FullStackWithLawrence/secure-logger/commit/7b71ae9c484486cd124b751bc201f16cc2d627bf))

## [0.1.9](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.8...v0.1.9) (2023-11-13)

### Bug Fixes

- have to skip CI automated unit tests when commit **version**.py ([0e939c8](https://github.com/FullStackWithLawrence/secure-logger/commit/0e939c87eb3ab0aafe6475691f1380127ea1860b))
- refactor call to npx semantic-release ([2c7d768](https://github.com/FullStackWithLawrence/secure-logger/commit/2c7d768c8875a11f68ff47700e4c8a107a98c89b))

## [0.1.8](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.7...v0.1.8) (2023-11-13)

### Bug Fixes

- required upgrade to node 20.9.0 ([756ea63](https://github.com/FullStackWithLawrence/secure-logger/commit/756ea6366bfe828783be17f4d581e8b4cd7f6574))
- required upgrade to node 20.9.0 ([9bc8871](https://github.com/FullStackWithLawrence/secure-logger/commit/9bc88718b3ffbfdd002d9156dcbad3db974b723f))

## [0.1.7](https://github.com/FullStackWithLawrence/secure-logger/compare/v0.1.6...v0.1.7) (2023-11-13)

### Bug Fixes

- add missing package descriptors ([72bc5b3](https://github.com/FullStackWithLawrence/secure-logger/commit/72bc5b3c296e3f5d809ecad894c8b25aa1e0e0fa))
- correct path to python requirements ([cdc0557](https://github.com/FullStackWithLawrence/secure-logger/commit/cdc05577f5b6e5c1bb46b141ff61ff00a0eca899))
- fix calls to unit tests ([9b98d18](https://github.com/FullStackWithLawrence/secure-logger/commit/9b98d18016cfe99b38298bd910831c1de3988db0))
- fix path to secure_logger ([1d6a1d9](https://github.com/FullStackWithLawrence/secure-logger/commit/1d6a1d90c233464746a85dcb0add3ba6e0f8297a))
- move **version**.py to the root ([da0beac](https://github.com/FullStackWithLawrence/secure-logger/commit/da0beac04ec3144936aa92fb5deca8b97945b439))
- remove reference to django migrations ([e0a62be](https://github.com/FullStackWithLawrence/secure-logger/commit/e0a62be13deb323f683d39134f42b203e413ff49))

# CHANGE LOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.1.6] (2023-04-26)

- add Github Actions test workflow status to README

## [0.1.5] (2023-04-26)

- add automated unit testing

## [0.1.4] (2023-04-26)

- bug fix: make dict key evaluation case insensitive

## [0.1.3] (2023-04-26)

- rename serialized_masked_dict() to masked_dict2str() with backward compatibility
- add defaults for indentation and log value redaction string message
- add more tests
- refactor documentation

## [0.1.2] (2023-04-25)

- add strong type checking

## [0.1.1] (2023-04-25)

- renamed to secure_logger

## [0.1.0] (2023-04-14)

- initial release
