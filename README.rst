cookiecutter-django
=======================

A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

Lighter version of the Daniel Greenfeld's cookiecutter-django.

It uses the latest stable versions and it only defines a skeleton which can be extended as needed.

Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

Set up your virtualenv
    $ cd <your-envs-folder>
    $ virtualenv  --no-site-packages redditclone
    $ cd redditclone
    $ source bin/activate
    $ pip install cookiecutter

Now run it against this repo::

    $ cd <your-workspace>
    $ cookiecutter  https://github.com/marcofucci/cookiecutter-django.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.


**Warning**: After this point, change 'Marco Fucci', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 443, done.
    remote: Compressing objects: 100% (242/242), done.
    remote: Total 443 (delta 196), reused 419 (delta 176)
    Receiving objects: 100% (443/443), 119.91 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (196/196), done.
    project_name (default is "project_name")? redditclone
    repo_name (default is "repo_name")? redditclone
    author_name (default is "Your Name")? Marco Fucci
    email (default is "Your email")? <your-email>
    description (default is "A short description of the project.")? A reddit clone
    year (default is "Current year")? 2013

Enter the project and take a look around::

    $ cd redditclone/
    $ ls
    $ pip install -r requirements/local.txt
    $ python ./manage.py syncdb
    $ python ./manage.py migrate
    $ python ./manage.py runserver

and load localhost:8000/admin


Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit!"
    $ git remote add origin git@github.com:pydanny/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Awesome, right?

It's time to write the code!!!


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:

Fork This
~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* cookiecutter_ so it gets listed in the README as a template.
* The cookiecutter grid_ on Django Packages.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutter/

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they make my own project development
experience better.
