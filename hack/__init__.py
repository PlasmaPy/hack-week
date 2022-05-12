"""
Welcome to the PlasmaPy `hack` package, an open source Python package
for plasma physics developed by the participants of the 2022 Plasma
Hack Week (https://hack.plasmapy.org/2022/about/).

Documentation is available in the docstrings and online at
https://hack-week.readthedocs.io/.
"""
__all__ = ["__version__"]

# Enforce Python version check during package import.
# This is the same check as the one at the top of setup.py
import sys

if sys.version_info < (3, 8):  # coverage: ignore
    raise ImportError("PlasmaPy does not support Python < 3.8")

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
import pkg_resources

# define version
try:
    # this places a runtime dependency on setuptools
    #
    # note: if there's any distribution metadata in your source files, then this
    #       will find a version based on those files.  Keep distribution metadata
    #       out of your repository unless you've intentionally installed the package
    #       as editable (e.g. `pip install -e {plasmapy_directory_root}`),
    #       but then __version__ will not be updated with each commit, it is
    #       frozen to the version at time of install.
    #
    #: PlasmaPy version string
    __version__ = pkg_resources.get_distribution("plasmapy").version
except pkg_resources.DistributionNotFound:
    # package is not installed
    fallback_version = "unknown"
    try:
        # code most likely being used from source
        # if setuptools_scm is installed then generate a version
        from setuptools_scm import get_version

        __version__ = get_version(
            root="..", relative_to=__file__, fallback_version=fallback_version
        )
        del get_version
        warn_add = "setuptools_scm failed to detect the version"
    except ModuleNotFoundError:
        # setuptools_scm is not installed
        __version__ = fallback_version
        warn_add = "setuptools_scm is not installed"

    if __version__ == fallback_version:
        from warnings import warn

        warn(
            f"plasmapy.__version__ not generated (set to 'unknown'), PlasmaPy is "
            f"not an installed package and {warn_add}.",
            RuntimeWarning,
        )

        del warn
    del fallback_version, warn_add

del pkg_resources, sys
