# from setuptools import setup

# __version__ = "0.0.1"

# setup(
#     name="my-package",
#     version=__version__,
#     # And so on...
# )

from setuptools import find_packages, setup

setup(
    name="testing-package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)
