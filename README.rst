DjangoVE
==============================

.. image:: https://requires.io/github/djangove/djangove/requirements.svg?branch=master
      :target: https://requires.io/github/djangove/djangove/requirements/?branch=master
      :alt: Requirements Status

.. image:: https://travis-ci.org/djangove/djangove.svg?branch=master
      :target: https://travis-ci.org/djangove/djangove?branch=master
      :alt: Build Status

.. image:: https://badges.gitter.im/djangove/djangove.svg
      :target: https://gitter.im/djangove/djangove?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
      :alt: Join the chat at https://gitter.im/djangove/djangove

DjangoVE, es una iniciativa hecha comunidad fundada por desarrolladores para desarrolladores en Venezuela, enfocados en evangelizar sobre el framework Django y contribuir con la educación de todos los que sean parte y hagan vida en esta nueva comunidad como complemento de lo aprendido en las universidades a través de tutoriales, talleres y eventos.


LICENSE: BSD

Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.org/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.org/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd djangove
    celery -A djangove.taskapp worker -l info

Please note: For Celerys import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.







It's time to write the code!!!


Running end to end integration tests
------------------------------------

N.B. The integration tests will not run on Windows.

To install the test runner::

  $ pip install hitch

To run the tests, enter the djangove/tests directory and run the following commands::

  $ hitch init

Then run the stub test::

  $ hitch test stub.test

This will download and compile python, postgres and redis and install all python requirements so the first time it runs it may take a while.

Subsequent test runs will be much quicker.

The testing framework runs Django, Celery (if enabled), Postgres, HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.
