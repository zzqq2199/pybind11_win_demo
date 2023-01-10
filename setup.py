import os, sys

from distutils.core import setup, Extension
from distutils import sysconfig
# specify the path of pybind header file and funcs.hpp
# cpp_args = ["-I./"]
cpp_args = []

ext_modules = [
  Extension(
    'wrap',
    ['func.cpp', 'wrap.cpp'],
    include_dirs=['pybind11/include'],
    language='c++',
    extra_compile_args=cpp_args,
  ),
]
setup(
  name='wrap',
  version='0.0.1',
  author='unknown',
  description='Example',
  ext_modules=ext_modules,
)