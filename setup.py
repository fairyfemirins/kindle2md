from setuptools import setup

setup(
    name="kindle2md",
    version="0.1.0",
    py_modules=["kindle2md"],
    install_requires=["click"],
    entry_points={"console_scripts": ["kindle2md=kindle2md:cli"]},
)