from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
#from Cython.Build import cythonize
ext_modules = [
    Extension("mymodule1",  ["170212_170278a2.py"]),

#   ... all your modules that need be compiled ...

]

setup(
    name = 'My Program Name',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules

)
