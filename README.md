# sila_abstract_base_features

Abstract base features (ABFs) serve to abstract behavior/process interfaces away from specific applications and hardware. These base features help ensure that connectors expose the same behavior with the same interface, and Python's mixed inheritance allows ready composition of multiple behavioral interfaces in a device feature.

Concrete features should be implemented in the [sila_hackathon_devices](https://github.com/RxnRover/sila_hackathon_devices) repo.

## Design

**Computer Science Mappings**

| SiLA Concept | Computer Science Concept           |
|--------------|------------------------------------|
| ABF          | Interface/ABC                      |
| Feature      | Implementation of ABF interface(s) |
| Server       | Composition of features (device)   |
| Platform     | Composition of device servers      |

**Project Hierarchy**

The plan is to map features, servers, and projects in the following manner:

- 1 feature -> 1 behavior/concern
- *n* features compose 1 server
- 1 server -> 1 device/platform
- 1 server -> 1 project/package/repo
- *n* servers -> 1 computer

Visualized, a hierarchy from host computer to two device servers would look like this:

```
computer
├── project1/package1/repo1
│   └── server1 -> device/platform
│       ├── feature1 -> behavior/concern
│       └── feature2 -> behavior/concern
└── project2
    └── server2 -> device/platform2
        └── feature3 -> behavior/concern
```

## Learning

- [UniteLabs CDK Documentation](https://docs.unitelabs.io/connector-development/)
- [Naming Conventions](https://docs.unitelabs.io/connector-development/reference/naming-conventions/)
- [Designing Features](https://docs.unitelabs.io/connector-development/concepts/features/)

## Development Environment Setup

- Install Git
- Install Python
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install . --group dev`
- `pre-commit install`

**Recommended**

The project is set up for the following tools to help with good development practices. These are usually something you can set up in your IDE, and VSCode/VSCodium has extensions for them:

- Black and isort for Python formatting
- Flake8 for Python linting
- Docstrfmt for reStructuredText formatting
- Mypy for type checking (please use type hints)

## Project Automation

### Tox

This project is set up with project automation through [tox](https://tox.wiki/en/latest/). Unit tests can be run by simply invoking:

```bash
tox
```

or other actions can be run with:

```bash
tox run -e <action>
```

Multiple actions can be run in sequence with commas:

```bash
tox run -e clean,build
```

A list of available actions can be found by running `tox list` after [Development Environment Setup](#development-environment-setup).

### Pre-Commit

To help with code checking, this project is set up with [pre-commit](https://pre-commit.com/). Once installed for the repo (`pre-commit install` in [Development Environment Setup](#development-environment-setup)), a series of tests and checks will be automatically run through git pre-commit hooks before the commit is allowed to go through. Some issues are fixed automatically, some require manual intervention. Once everything has been fixed, commit the new changes and try again until all of the checks are passing!
