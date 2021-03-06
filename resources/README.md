[Anaconda]: https://www.anaconda.com
[anaconda-install]: https://docs.anaconda.com/anaconda/install/
[Anaconda Navigator]: https://docs.anaconda.com/anaconda/navigator/
[git-installation]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[GitHub]: https://www.github.com
[plasmapy-installation]: https://docs.plasmapy.org/en/stable/install.html
[PyCharm]: https://www.jetbrains.com/pycharm/
[python-download]: https://www.python.org/downloads/
[python-installation]: https://docs.plasmapy.org/en/stable/install.html#installing-python
[Spyder]: https://www.spyder-ide.org/
[VSCode]: https://code.visualstudio.com/


# Plasma Hack Week Resources

This directory contains resources pertinent to the 2022 Plasma Hack Week.
Added resources include, but are not limit to, pre-event background
materials, demo Jupyter notebooks, tutorials, etc.

### Contents:

1. [Pre-Event Materials](#pre-event-materials)
2. [Getting Yourself Setup for the Hack Week](#getting-yourself-setup-for-the-hack-week)
3. [Event Day Resources](#event-day-resources)

## Pre-Event Materials

1. [Installing `git`](#installing-git)
2. [Installing Python](#installing-python)
3. [Anaconda](#anaconda)
4. [Install your favorite code editor](#install-your-favorite-code-editor)
5. [Installing `plasmapy`](#installing-plasmapy)

### [Installing `git`][git-installation]
    
`git` is a free open-source version control system, and is the backbone to
collaborative open-source software development.  On Day 2 we will
cover how to use `git`, both through a command line interface (CLI)
and built-in graphical user interfaces (GUIs) to select code editors.

### [Installing Python][python-installation]

For the Hack Week we will require Python 3.8+, and recommend
installing Python 3.10.  A Python distribution can be
[downloaded][python-download] directly from python.org and installed.

### [Anaconda]

[Anaconda] is similar to the Python Package Index (PyPI), in that it
is a package distribution hub.  Unlike PyPI, packages listed on
Anaconda are not restricted to just Python packages.

Anaconda has its own package installer called `conda`, similar to PyPI's
installer `pip`.  Unlike `pip`, `conda` also has built-in functionality
for managing virtual environments.  For more detailed information, look
to Anaconda's
["Understanding Conda and Pip"](https://www.anaconda.com/blog/understanding-conda-and-pip)
primer.

Anaconda also provides the [Anaconda Navigator], which is a desktop GUI
which allows you to launch applications and manage conda packages.

### Install your favorite code editor

During the Hack Week the organizers will be using their Integrated
Development Environment (IDE), i.e. code editor, of choices, so you
will get exposure to the main IDEs out there.  The three IDEs that will be
used are:

* [VSCode] by Microsoft, 
* [PyCharm] by JetBrains 
* [Spyder]

On Day 1 we will give a brief overview of each IDE.

### [Installing `plasmapy`][plasmapy-installation]

For the Hack Week we will be using `v0.8.1` of `plasmapy`.  This can be
installed using `pip` or `conda`, depending on your workflow.  For full
[installation instructions][plasmapy-installation]
see PlasmaPy's documentation.

### Sign Up for GitHub

[GitHub] is a code hosting platform for version control and collaboration.
[GitHub] is where we will combine all of collaborative work during the
Hack Week to create the `hack` package.  There are two types of GitHub
accounts, a personal account and an organization account.  All you
need to do is 
[create a free personal account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account).

## Getting Yourself Setup for the Hack Week

Most on the getting setup resources are listed above in the
[Pre-Event Materials](#pre-event-materials) section.  However, here is
check list of the steps you should do.  Most of these steps will be
covered during days 1 and 2 of the Hack Week, but we highly encourage
you get started before the event.

 - [ ] [Install `git`][git-installation]
 - [ ] Create a free personal [GitHub] account
 - [ ] Decide if you want to used Anaconda or not

    - **Yes**: [Install Anaconda][anaconda-install], which will also install
      a copy of Python.
    - **No (and Yes)**: [Install Python][python-installation].  If yes,
      Anaconda does install a copy of Python, but you can still install
      other versions of Python to use in different environments.

 - [ ] [Install `plamsapy`][plasmapy-installation]
 - [ ] [Install your code editor of choice](#install-your-favorite-code-editor)

## Event Day Resources

### Day 1 Resources

* [Getting Python][python-installation]
  * [Python, PyPI, and `pip`](./2022HW_python_pypi_pip.md)
* [Getting Anaconda][anaconda-install]
* Terminals
  * [On Unix & MacOS](./unix_shell.md)
  * [On Windows](./terminals_windows.md)
* Interactive Development Environments
  * [Overview Slides](./2022HW_IDE_Overview.pdf)
  * [Spyder Overview & Walk-through](./ide_spyder.md)
  * [VSCode Overview & Walk-through](./ide_vscode.md)
  * [PyCharm Overview & Walk-through](./ide_pycharm.md)
* [Virtual Environments](./virtual_environments.md)

### Day 2 Resources

* [Getting `git`][git-installation]
* [GitHub Documentation](https://docs.github.com/en)
* [GitHub Hello World](https://docs.github.com/en/get-started/quickstart/hello-world)
* [`git` & GitHub Overview Slides](./2022HW_git_and_GitHub_overview_slides.pdf)
* Dive into `plasmapy` notebooks
  * [Blank Notebook](./2022HW_dive_into_plasmapy.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PlasmaPy/hack-week/HEAD?labpath=resources%2F2022HW_dive_into_plasmapy.ipynb)
  * [Completed Notebook](./2022HW_dive_into_plasmapy_completed.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PlasmaPy/hack-week/HEAD?labpath=resources%2F2022HW_dive_into_plasmapy_completed.ipynb)

[//]: # (## Day 3 Resources)

[//]: # (## Day 4 & 5 Resources)

