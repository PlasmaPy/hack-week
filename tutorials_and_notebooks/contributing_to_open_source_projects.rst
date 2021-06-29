======================================
Contributing to an Open Source Project
======================================

This doc describes the workflow for making a contribution to PlasmaPy
using `git` via a command line interface (such as a Unix shell).  These
steps can also be done using an integrated development environment like
`PyCharm <https://www.jetbrains.com/pycharm/>`_.

Beforehand
==========

1. `Create a GitHub account <https://github.com/join>`_.
2. `Install git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_.
3. Do the first-time git setup and set your name and email.

   .. code-block:: shell

       git config --global user.name "John Doe"
       git config --global user.email johndoe@example.com

Getting started
===============

1. Go to `PlasmaPy’s repository <https://github.com/PlasmaPy/plasmapy>`_
   on GitHub.
2. Click on the “Fork” button to create your own fork of PlasmaPy.
3. Click on the “Code” button.  Select “HTTPS” is selected, unless you’ve
   set up SSH.  Click on the clipboard icon to copy the address.
4. Open a terminal.
5. Navigate to a directory where you want to put your repository.  For
   example, you could create a ``Repositories`` directory within your
   home directory.
6. Clone your fork of PlasmaPy to your local computer.

   .. code-block:: shell

       git clone https://github.com/PlasmaPy/PlasmaPy.git

   This will create a directory called ``PlasmaPy`` subdirectory inside
   the directory you were already in.
7. Add a remote for PlasmaPy's main repository.

   .. code-block:: shell

       git remote add upstream

   Then check the remotes with

   .. code-block:: shell

       git remote -v

   There should be ``origin`` (which corresponds to your fork) and
   ``upstream`` (which corresponds to the original PlasmaPy
   repository).

Making a code contribution
==========================

1. Fetch the most recent changes from remotes.

   .. code-block:: shell

       git fetch --all

2. Create a feature branch based off of the ``main`` branch on the
   ``upstream`` remote, and give it a descriptive name.  This command
   will create the branch, and switch you to it.

   .. code-block:: shell

      git checkout -b descriptive-branch-name upstream/main

   To check the branches that you have and which branch you are on, do:

   .. code-block:: shell

      git branch

3. Push and link the branch to your fork of PlasmaPy on GitHub.

   .. code-block:: shell

      git push --set-upstream origin descriptive-branch-name

4. Edit a file, for example ``filename.py``.
5. Commit the file and push it to GitHub

   .. code-block:: shell

       git add filename.py
       git commit -m "Add exciting new feature"
       git push

6. Go to GitHub's repository and create a pull request from the
   ``descriptive-branch-name`` branch on your fork of PlasmaPy to
   the ``main`` branch on PlasmaPy.

7. Repeat steps 4–5 until you get tests to pass.

8. Create a changelog entry.  For pull request 12345 on GitHub,
   create a file in the ``changelog`` directory ``12345.doc.rst`` and
   add a sentence or two describing the changes.  You can alternatively
   create ``12345.feature.rst`` for a new feature, ``12345.trivial.rst``
   for a minor change, and ``12345.breaking.rst`` for a breaking change.

9. Request a code review.
10. Address comments.

