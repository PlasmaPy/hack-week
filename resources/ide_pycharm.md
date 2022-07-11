---
tags: Hack Week, IDE, 2022
---

[![hackmd-github-sync-badge](https://hackmd.io/-MvWnXf2S8OrKhreH1Wzgg/badge)](https://hackmd.io/-MvWnXf2S8OrKhreH1Wzgg)


[PyCharm]: https://www.jetbrains.com/pycharm/

# 2022 Hack Week: IDE PyCharm

This file covers the PyCharm IDE overview discussed on Day 1 of the [2022 Plasma Hack Week](https://hack.plasmapy.org/2022/about).

## What is PyCharm

[PyCharm] is an IDE distributed by JetBrains that focuses around code development for Python projects.  Even though PyCharm is Python centric, it does support development of many languages.

## Download and Install

PyCharm provides several versions.  There is a free open-source **Community** version and a pay-for **Professional** version.  Both have an installer that can be [**downloaded**](https://www.jetbrains.com/pycharm/download/#section=mac) directly from JetBrains.  The Community version can also be found on GitHub (https://github.com/JetBrains/intellij-community/tree/master/python).

In additional to the Community and Professional versions, JetBrains provides an **Educational** version.  This gives students and teachers free access to many of the Professional features.  One can request an educational license with the following link: https://www.jetbrains.com/community/education/.

## Useful Tutorials and Demos

* PyCharm's [YouTube Tour](https://youtu.be/BPC-bGdBSM8)
* JetBrain's PyCharm [YouTube playlist](https://youtube.com/playlist?list=PLQ176FUIyIUbDwdvWZNuB7FrCc6hHregy)

## PyCharm Walkthrough

1. Open `plasmapy` in PyCharm
2. Highlight Project Tab
    * IDE is package development centric, not script centric
    * There is a [LightEdit mode](https://www.jetbrains.com/help/pycharm/lightedit-mode.html) for editing files without creating a project
3. PyCharm Settings: Project Interpreter
    * Defines Python environment for project
    * Can create virtual environments
    * can define several environments
    * selectable in bottom right cornert
2. Terminal integration
    * utilizes project environment
    * you can select which terminal flavor you like
4. Python console integration
    * IPython console
    * utilizes project environment
    * current project is appended to the PYTHONPATH
5. Highlight Code Editor
    * color highlighting
    * line numbering and rules
    * splitting windows
    * code inspection and linters
        * use `plasmapy/formulary/speeds.py` as example
        * PEP8
        * can be configured in settings
        * highlight gutter indicators/warnings
5. version control (`git`) integration
    * **Will cover in more detail on Day 2.**
    * can utilize many version control systems, but we'll focus on `git`
    * `git` dropdown has many of the basic git commands
    * `git` tab
        * view local changes
        * view git history
7. GitHub integration
    * **Will cover in more detail on Day 2.**
    * go to `settings` -> `Version Control` -> `GitHub`
    * allows you to communicat directly with GitHub
    * View Pull Request
    * Push and Pull changes
9. Debugger and Test runners
    * builtin debugging
    * test runners for both `unittests` and `pytest`
    * support for code coverage
    * can run debugger from Python Consol and from tests
11. Extendable with Plugins
    * `Settings` -> `Plugins`

