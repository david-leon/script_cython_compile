# SCC
[![Python 3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/downloads/release)

A cmdline tool for cython-compiling a python script, mainly for code encryption purpose. 
SCC = Script Cython-Compilation.

## Install
Download the source and
```commandline
python setup.py install
```
or just simply
```commandline
pip install git+https://github.com/david-leon/script_cython_compile.git
```

## Usage

Under command-line console, input:

    scc python_file
    scc python_file -compiler msvc
    scc python_file -save_folder .

This will generate *.pyd file on Windows or *.so file on Linux in the same directory with the source python file (by default)
 or in the directory specified by `-save_folder`

## Q&A
1. Q: Error `ImportError: dynamic module does not define module export function` when importing from the generated .pyd/.so file     
   A: DO NOT rename the generated .pyd/.so file
