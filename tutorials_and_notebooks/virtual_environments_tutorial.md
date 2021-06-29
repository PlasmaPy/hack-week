# Plasma Hack Week 2021: Virtual Environments

## What is a Virtual Environment?

From Python (https://docs.python.org/3/glossary.html#term-virtual-environment):

![](https://i.imgur.com/DILxFrs.png)

Virtual environments allow you to create independent collections of installed packages.  This is often useful when you need two 3rd party pacakages that conflict with eachother.  Instead of installing and unstalling when need, you can create a virtual environment for configurate A with package A and an environment for configuration B with package B.  Then you can switch between environments as needed.

## Existing Packages for Creating Virtual Environments

There are several packages that exist for creating virtual environments.

* [`venv`](https://docs.python.org/3/library/venv.html#module-venv): A builtin module included in Python 3.3+.  Designed for crating lightweight virtual environments.
* [`virtualenv`](https://virtualenv.pypa.io/en/stable/): A 3rd party package that is almost identicaly in use to `venv`, but available for both Python 2 and 3.
* [`pyenv`](https://github.com/pyenv/pyenv):  Allows for switcing between Python versions.
* [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv):  A plugin for `pyenv` that provides features to manage virtual environments created by `virtualenv` and `conda`.
* [`conda`](https://docs.conda.io/en/latest/):  An open-source pacakge management and environment management system.  This is like combining `pip` and `venv` into one, but `conda` is not associated with either of thos.  The `conda` manager is independent of `pip` and <https://pypi.org>, and is used for Anaconda, Minconda, and the Anaconda Repository.
* and much more....

## The Tutorial

This tutorial focuses on using `venv` to create virtual environments.  The follow is covered below...

1. [Crating a Virtual Environment](#Creating-a-Virtual-Environment)
2. ["Modifying" `PYTHONPATH` for Your Virtual Environment](#“Modifying”-PYTHONPATH-for-Your-Virtual-Environment)
3. [Using Virtual Environments with Jupyter Notebooks](#Using-Virtual-Environments-with-Jupyter-Notebooks)

### Creating a Virtual Environment

1. The base python version used for your virtual enviroment comes from the python version used to create the virtual environment.
    ```shell=
    $ python3 --version
    Python 3.8.6
    ```
    In this casse it is Python 3.8
2. You can view the packages currently installed in your Python 3.8 distribution by...
    ```shell=
    $ python3 -m pip list # equivalent to pip list
    Package    Version
    ---------- -------
    pip        21.1.3
    setuptools 49.2.1
    ```
    In this case, only `pip` and `setuptools` are installed in addition to the builtin packages.
4. Create a directory for your virtual environemnt
    ```shell
    $ cd ~/Desktop/2021_Hack_Week
    $ mkdir venvs
    $ cd venves
    $ mkdir py38_hack
    ```
3. Now, create the environment.  Make sure you are sitting one level outsite the directory where the environment will be created.  In this example, that is the `venvs` directory.
    ```shell=
    $ python3 -m venv py38_hack
    ```
5. Now, the environment is created but not yet ativated.  By moving into `py38_hack` you can see it is now populated.
    ```shell=
    $ cd py38_hack
    $ ls
    bin/    include/    /lib    pyvenv.cfg
    ```
7. To activate the virtual environment we have to execute the `activate` script in `bin/`
    ```shell=
    $ source bin/activate
    (py38_hack)$
    
    # on Windows
    $ .\Scripts\activate
    ```
    Now, the virtual environment is activated this can be seen by the `(py38_hack)` being added to the command prompt.
9. To deactivate the virtual environment just do...
    ```shell=
    (py38_hack)$ deactivate
    $
    ```
11. Installing packages to a virtual environment is just like normal, but the virtual environment must be activated
    ```shell=
    $ source bin/activate
    (py38_hack)$ pip list
    Package         Version
    --------------- -------
    pip             21.1.3
    setuptools      49.2.1
    (py38_hack)$ pip install numpy
    (py38_hack)$ python -m pip install matplotlib
    (py38_hack)$ pip list
    Package         Version
    --------------- -------
    cycler          0.10.0
    kiwisolver      1.3.1
    matplotlib      3.4.2
    numpy           1.21.0
    Pillow          8.2.0
    pip             21.1.3
    pyparsing       2.4.7
    python-dateutil 2.8.1
    setuptools      49.2.1
    six             1.16.0
    ```
### "Modifying" `PYTHONPATH` for Your Virtual Environment

`PYTHONPATH` is a list of all the directories python searches to find packages when importing.  There are several ways to modify your paths.  The "difficult" way is modifying the `/bin/activate` script (similar to modifying your `.bashrc` file) so `PYTHONPATH` is appended when the shell/terminal is launched.  In this example I'm going to use the "more elegant" way of appending your `PYTHONPATH` by adding a `<name>.pth` file to your `lib/pythonX.Y/site-packages` directory.  Python will recognize this file and know to append the files contents to Python's search paths.  Continuing with the above example, I'm going to add my `plasmapy` local repository to to Python's search paths so I can use it the Python console or Jupyter notebooks without having to install `plasmapy`.

1. We want to navigate to the `site-packages` directory for our virtual environment.
    ```shell=
    (py38_hack)$ cd lib/python3.8/site-packages
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
        '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
        '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
        '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
        '/.../Hack_Week_2021/venvs/py38_hack/lib/python3.8/site-packages',
        '/.../PlasmaPy',
    ]
    >>> import plasmapy
    >>> plasampy.__version__
    '0.7.dev42+g48972c4f.d20210626'
    ```
    Note, for `plasmapy` to import correctly you first must install all of its dependencies into the virtual environment.

### Using Virtual Environments with Jupyter Notebooks

1. First we want to install the necessary Jupyter packages to our virtual environment
    ```shell=
    (py38_hack)$ pip install jupyter
    (py38_hack)$ pip install jupyterlab
    (py38_hack)$ pip install ipykernel
    ```
2. Add your virtual environment to Jupyter notebooks
    ```shell=
    python -m ipykernel install --user --name py38_hack --display-name "py38_hack"
    ```

    * `--user` install for only the curren tuser
    * `--name` The name for kernelspec (internal naming for Jupyter).  If the name already exist, then it will be overwritten.
    * `--display-name` The name seen in notebook menus.
4. Now, you can lauch Jupyter notebook and create a new notebook using your

    ```shell=
    (py38_hack)$ python -m jupyterlab
    ```
    
    ![](https://i.imgur.com/iYcGxxX.png)
    
    Note, you do not need to activate your virtual envirnment to be able to use it in your Jupyter notebook.  Each notebook has its own kernel associated with it and Jupyter will activate the approriat environment for that notebook.

5. To view the currnt kerenls added to Jupyter do the following
    ```shell=
    (pyt38_hack)$ python -m jupyter kernelspec list
    Available kernels:
      py38_hack   /.../Jupyter/kernels/py38_hack
    ```
7. To remove a kernel, one can unistall it by doing...
    ```shell=
    (py38_hack)$ python -m jupyter kernelspec uninstall py38_hack
    ```

## Useful References

* <https://stackoverflow.com/a/41573588>
* https://docs.python.org/3/library/venv.html
* https://docs.python.org/3/tutorial/venv.html
* https://virtualenv.pypa.io/en/stable/
* https://docs.python.org/3/glossary.html#term-virtual-environment
