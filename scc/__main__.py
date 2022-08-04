# coding:utf-8
# Compile the source python script into cython version for deployment.
# Created   :   7,  3, 2017
# Revised   :   9, 17, 2018
#               8,  4, 2022  add explicit language level specification for `cythonize`
# All rights reserved
# ------------------------------------------------------------------------------------------------
__author__ = 'dawei.leng'
import os, shutil, argparse
import warnings

def generate_setup_file(filename, module_name=None, source_file=None):
    txt = "from distutils.core import setup\n" \
          "from distutils.extension import Extension\n" \
          "from Cython.Build import cythonize\n" \
          "import os\n" \
          "module_name = '%s'\n" \
          "if os.name == 'nt':\n" \
          "    ext_modules=[Extension(module_name, sources=[r'%s'], define_macros=[('MS_WIN64', None), ], extra_compile_args = ['-g0'])]\n" \
          "else:\n" \
          "    ext_modules=[Extension(module_name, sources=[r'%s'], extra_compile_args = ['-g0'])]\n" \
          "setup(\n" \
          "    name = module_name,\n" \
          "    ext_modules = cythonize(ext_modules, compiler_directives={'language_level' : '3'}))" % (module_name, source_file, source_file)
    with open(filename, mode='wt', encoding='utf8') as f:
        f.write(txt)

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('file', nargs='?', default=None, type=str, help='python file to be compiled')
    argparser.add_argument('-compiler', default=None, type=str, help='None|msvc')
    argparser.add_argument('-save_folder', default=None, type=str, help='where to save compiled files')
    arg = argparser.parse_args()

    # --- public paras ---#
    py_file     = arg.file
    compiler    = arg.compiler
    save_folder = arg.save_folder
    print('Source file = %s' % py_file)
    if py_file is None:
        return

    cwd = os.getcwd()
    py_file = os.path.abspath(py_file)
    dirpath, filename = os.path.split(py_file)
    basename, ext = os.path.splitext(filename)
    if ext.lower() != '.py':
        warnings.warn("File extension not '.py', you'd better check that")

    if save_folder is None:
        save_folder = dirpath

    pyx_file = os.path.join(save_folder, basename+'.pyx')
    shutil.copyfile(py_file, pyx_file)
    generate_setup_file(os.path.join(save_folder, 'setup.py'), basename, pyx_file)
    os.chdir(save_folder)
    if compiler is None:
        cmd = 'python %s build_ext --inplace' % (os.path.join(save_folder, 'setup.py'))
    else:
        cmd = 'python %s build_ext --inplace --compiler %s' % (os.path.join(save_folder, 'setup.py'), compiler)
    print(cmd)
    os.system(cmd)
    #--- clean up ---#
    file_to_be_removed = [os.path.join(save_folder, basename+ext) for ext in ['.c', '.pyx', '.o']]
    file_to_be_removed.append(os.path.join(save_folder, 'setup.py'))
    for file in file_to_be_removed:
        try:
            os.remove(file)
        except:
            pass
    os.chdir(cwd)
