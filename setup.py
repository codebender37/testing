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
    version="3.2.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)

# Testing 1
# Release v0.2.0
# Release v1.0.0
# add fix 1
# add feature without feat
# add feature with feat
# add fix 2
# ready to release
# add fix 3
# normal commit
# add fix 4

# add fix 5
# add feature
