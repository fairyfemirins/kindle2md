from setuptools import setup, find_packages

setup(
    name="kindle2md",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click", "jinja2"],
    entry_points={"console_scripts": ["kindle2md=kindle2md.cli:cli"]},
)