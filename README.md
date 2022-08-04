# SCC
[![Python 3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/downloads/release)

A cmdline tool for cython-compiling a python script, mainly for code encryption purpose. 
SCC = Script Cython-Compilation.

## Install
```
python setup.py install
```

## Usage

Under command-line console, input:

    scc python_file
    scc python_file -compiler msvc
    scc python_file -save_folder .

This will generate *.pyd and *.def files on Windows or *.so file on Linux in the same directory with the source python file (by default)
 or in the directory specified by `-save_folder`
