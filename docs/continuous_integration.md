# Continuous Integration

## Code styleguide

This project’s code formatting is enforced with:

- [black](https://github.com/psf/black)
- [flake8](https://github.com/pycqa/flake8)
- [isort](https://github.com/PyCQA/isort)

## Automatic linting locally

You can run the linting tests automatically before committing using pre-commit.

To use when making commits on your host machine you must install pre-commit, either create a virtualenv to use with the project or to install globally see instructions at (https://pre-commit.com/#install).

You can also manually run pre-commit without using a git hook by running:

```bash
$ pre-commit run --all-files
```

## Automatic checks on Github

When commits are pushed to Github, CI pipelines including tests, and linting checks are run.

This is configured in `.github/workflows/ci.yml`.