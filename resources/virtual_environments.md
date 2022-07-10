# Plasma Hack Week 2021: Virtual Environments

## What is a Virtual Environment?

From Python (https://docs.python.org/3/glossary.html#term-virtual-environment):

![](https://i.imgur.com/DILxFrs.png)

Virtual environments allow us to create independent collections of installed packages. This is often useful when we need to use different versions of the same package for different projects. Instead of uninstalling and reinstalling when needed, virtual environments can isolate different execution environments in a way that it's easy to switch between them.

## Existing Packages for Creating Virtual Environments

There are several packages that exist for creating and managing virtual environments.

* [`venv`](https://docs.python.org/3/library/venv.html#module-venv): A builtin module included in Python 3.3+.  Designed for crating lightweight virtual environments. This is the recommended tool for creating virtual environments.
* [`virtualenv`](https://virtualenv.pypa.io/en/stable/): A 3rd party package that is almost identicaly in use to `venv`, but available for both Python 2 and 3.
* [`pyenv`](https://github.com/pyenv/pyenv):  Allows for switcing between Python versions.
* [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv):  A plugin for `pyenv` that provides features to manage virtual environments created by `virtualenv` and `conda`.
* [`conda`](https://docs.conda.io/en/latest/):  An open-source package and environment management tool.  This is like combining `pip` and `venv` into one, but `conda` is not tied to either of those.  The `conda` manager is independent of `pip` and <https://pypi.org>, and is used for Anaconda, Minconda, and the Anaconda Repository.
* and much more....

## The Tutorial

Since Python already comes with `venv` included, we will use that during this tutorial.

1. [Creating a Virtual Environment](#Creating-a-Virtual-Environment)
2. ["Modifying" `PYTHONPATH` for Your Virtual Environment](#“Modifying”-PYTHONPATH-for-Your-Virtual-Environment)
3. [Using Virtual Environments with Jupyter Notebooks](#Using-Virtual-Environments-with-Jupyter-Notebooks)

### Creating a Virtual Environment

1. The base python version used for your virtual enviroment comes from the python version used to create the virtual environment.

    **UNIX:**
    ```shell=
    $ python3 --version
    Python 3.9.8
    ```
    **Windows (Powershell):**
    ```shell=
    > py --version
    Python 3.9.13
    ```
    In this casse it is Python 3.9
2. You can view the packages currently installed in your Python 3.9 distribution by...

    **UNIX:**
    ```shell=
    $ python3 -m pip list # equivalent to pip list
    Package    Version
    ---------- -------
    pip        22.1.2
    setuptools 62.1.0
    ```
    **Windows (Powershell):**
    ```shell=
    > py -m pip list # equivalent to pip list
    Package    Version
    ---------- -------
    pip        22.1.2
    setuptools 58.1.0
    ```
    In this case, only `pip` and `setuptools` are installed in addition to the builtin packages.
3. Create a directory for your virtual environemnt
    
    **UNIX:**
    ```shell=
    $ mkdir -p ~/Desktop/hack-week-2022/py39-hack
    ```

    **Windows (Powershell):**
    ```shell=
    > mkdir ~\Desktop\hack-week-2022\py39-hack
    ```
4. Now, create the environment.  Make sure you are sitting one level outsite the directory where the environment will be created.  In this example, outside the `py39-hack` directory.

    **UNIX:**
    ```shell=
    $ cd ~/Desktop/hack-week-2022
    $ python3 -m venv py39-hack
    ```

    **Windows (Powershell):**
    ```shell=
    > cd ~\Desktop\hack-week-2022
    > py -m venv py39-hack
    ```

5. Now, the environment is created but not yet activated.  By listing the contents of `py39-hack`, you can see it is now populated.
    
    **UNIX:**
    ```shell=
    $ ls py39-hack
    bin/    include/    lib/    pyvenv.cfg
    ```
    
    **Windows (powershell):**
    ```shell=
    > ls py39-hack
    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         7/07/2022     03:05                etc
    d-----         7/07/2022     01:09                Include
    d-----         7/07/2022     01:09                Lib
    d-----         7/07/2022     03:11                Scripts
    d-----         7/07/2022     03:05                share
    -a----         7/07/2022     01:16            121 pyvenv.cfg
    ```
    
6. To activate the virtual environment we have to execute the `activate` script in `bin/`. This can vary depending on the terminal you are using.
![](https://i.imgur.com/bUFnzlV.png)

    **For bash/zsh:**
    ```shell=
    $ source py39-hack/bin/activate
    (py39-hack) $
    ```

    **Windows (Powershell):**
    ```shell=
    > Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
    > .\py39-hack\Scripts\Activate.ps1
    ```
    Now, the virtual environment is activated. This can be seen as the addition of `(py39-hack)` to the command prompt.
9. To deactivate the virtual environment just do...
    
    **UNIX:**
    ```shell=
    (py39-hack)$ deactivate
    $
    ```
    
    **Windows (Powershell):**
    ```shell=
    (py39-hack)> deactivate
    >
    ```

11. Installing packages to a virtual environment is just like normal, but the virtual environment must be activated

    **bash/zsh:**
    ```shell=
    $ source py39-hack/bin/activate
    (py39-hack)$ pip list
    Package         Version
    --------------- -------
    pip             22.1.2
    setuptools      62.1.0
    (py39-hack)$ pip install numpy
    (py39-hack)$ python -m pip install matplotlib
    (py39-hack)$ pip list
    Package         Version
    --------------- -------
    cycler          0.10.0
    kiwisolver      1.3.1
    matplotlib      3.4.2
    numpy           1.21.0
    Pillow          8.2.0
    pip             22.1.2
    pyparsing       2.4.7
    python-dateutil 2.8.1
    setuptools      62.1.0
    six             1.16.0
    ```

    **Windows (powershell):**
    ```shell=
    > .\py39-hack\Scripts\Activate.ps1
    (py39-hack)> pip list
    Package              Version
    -------------------- -----------
    anyio                3.6.1
    argon2-cffi          21.3.0
    argon2-cffi-bindings 21.2.0
    asteval              0.9.27
    astropy              5.1
    asttokens            2.0.5
    attrs                21.4.0
    Babel                2.10.3
    backcall             0.2.0
    beautifulsoup4       4.11.1
    bleach               5.0.1
    ```
    
### "Modifying" `PYTHONPATH` for Your Virtual Environment

`PYTHONPATH` is a list of all the directories python searches to find packages when importing.  There are several ways to modify your paths.  The "difficult" way is modifying the `/bin/activate` script (similar to modifying your `.bashrc` file) so `PYTHONPATH` is appended when the shell/terminal is launched.  In this example I'm going to use the "more elegant" way of appending your `PYTHONPATH` by adding a `<name>.pth` file to your `lib/pythonX.Y/site-packages` directory.  Python will recognize this file and know to append the files contents to Python's search paths.  Continuing with the above example, I'm going to add my `plasmapy` local repository to to Python's search paths so I can use it the Python console or Jupyter notebooks without having to install `plasmapy`.

1. We want to navigate to the `site-packages` directory for our virtual environment.
    ```shell=
    (py39-hack)$ cd lib/python3.9/site-packages
    ```
14. In this directory we create the `plasmapy.pth` file with the folowing contents
    ```
    /absolute/path/to/my/plasmapy_repo
    ```
    where this is the real absoute path on your own machine.
16. So, lauching a python console we can now see that the search path has been updated
    ```python=
    >>> import sys
    >>> sys.path
    [
        '', 
        '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', 
        '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9', 
        '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', 
        '/.../hack-week-2022/py39-hack/lib/python3.9/site-packages', 
        '/.../PlasmaPy'
    ]
    >>> import plasmapy
    >>> plasampy.__version__
    '0.7.1.dev104+g2ce52481'
    ```
    Note, for `plasmapy` to import correctly you first must install all of its dependencies into the virtual environment. The PlasmaPy dependencies can be found in the `requirements/install.txt` file in the PlasmaPy repository.
    
Some people prefer to use `Poetry`, so you might want to also have a look into it. A link is provided at the end of this page.

### (Optional) Using Virtual Environments with Jupyter Notebooks

1. First we want to install the necessary Jupyter packages to our virtual environment
    ```shell=
    (py39-hack)$ pip install jupyter
    (py39-hack)$ pip install jupyterlab
    (py39-hack)$ pip install ipykernel
    ```
2. Add your virtual environment to Jupyter notebooks
    ```shell=
    python -m ipykernel install --user --name py39-hack --display-name "py39-hack"
    ```

    * `--user` install for only the current user
    * `--name` The name for kernelspec (internal naming for Jupyter).  If the name already exist, then it will be overwritten.
    * `--display-name` The name seen in notebook menus.
4. Now, you can lauch Jupyter notebook and create a new notebook using your

    ```shell=
    (py39-hack)$ python -m jupyterlab
    ```
    
    ![](https://i.imgur.com/iYcGxxX.png)
    
    Note, you do not need to activate your virtual envirnment to be able to use it in your Jupyter notebook.  Each notebook has its own kernel associated with it and Jupyter will activate the approriat environment for that notebook.

5. To view the currnt kerenls added to Jupyter do the following
    ```shell=
    (py39-hack)$ python -m jupyter kernelspec list
    Available kernels:
      py39-hack   /.../Jupyter/kernels/py39-hack
    ```
7. To remove a kernel, one can unistall it by doing...
    ```shell=
    (py39-hack)$ python -m jupyter kernelspec uninstall py39-hack
    ```

## Useful References
* https://python-poetry.org/
* https://stackoverflow.com/a/41573588
* https://docs.python.org/3/library/venv.html
* https://docs.python.org/3/tutorial/venv.html
* https://virtualenv.pypa.io/en/stable/
* https://docs.python.org/3/glossary.html#term-virtual-environment
