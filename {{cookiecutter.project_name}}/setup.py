from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='{{cookiecutter.package_name}}',
    version='{{cookiecutter.package_version}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    description='{{cookiecutter.package_short_description}}',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'setuptools'
    ],
    packages=[
        '{{cookiecutter.package_name}}'
    ],
)