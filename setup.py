import os
import re
from setuptools import find_packages
from setuptools import setup
import io, shutil
from distutils.extension import Extension

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'scc', '__init__.py'), 'r') as f:
    init_py = f.read()
version = re.search('__version__ = "(.*)"', init_py).groups()[0]

with io.open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    README = f.read()

setup(
    name="scc",
    version=version,
    description="cmdline tool for cython-compiling a python script",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        ],
    install_requires=[
        'cython',],
    keywords="code encryption",
    author="David Leon (Dawei Leng)",
    author_email="daweileng@outlook.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    # install_requires=install_requires,
    # extras_require={
    #     'testing': tests_require,
    #     },
    entry_points={
        'console_scripts': [
            'scc = scc.__main__:main',
        ],},
    )
