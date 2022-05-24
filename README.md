# backoffice-demo-django

This is a Django example of using the Formal SQL commenter to propagate end-user identities through the time of database access.

1. See `backoffice_demo_django/middleware` for the database instrumentation package you can add to your own Django project. 
2. See `config/base.py` to see the `MIDDLEWARE` implementation that ativates the database instrumentation.
3. We will release a go package by Wednesday.


Don't hesitate to ping us here at Formal with any questions!



### To run this demo, with a new database: 

- add required .env files in root of project
- See https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html `DJANGO_READ_DOT_ENV_FILE` must be `True`
    - run `$ export DJANGO_READ_DOT_ENV_FILE=True`
- `$ python3 manage.py migrate`
---

---

## (The frontend of this demo was bootstrapped with a Cookiecutter Django template)

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy backoffice_demo_django

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
