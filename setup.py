"""Setup module."""
from setuptools import find_packages, setup

setup(
    name="workshop",
    version="1.0.0",
    packages=[*find_packages(exclude=["test", "test.*"])],
    url="https://github.com/adriaanslechten/klarna_python_workshop",
    entry_points={"console_scripts": ["workshop= workshop.__main__:main"]},
    include_package_data=True,
)
