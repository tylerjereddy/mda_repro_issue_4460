from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Extension modules
extensions = [
    Extension("reproducer", ["reproducer.pyx"],
              include_dirs=[np.get_include()],
              language="c++")
              # will fail to compile on 1.26.4 with this:
              #extra_compile_args=["-DNPY_NO_DEPRECATED_API=NPY_1_9_API_VERSION"])
]


setup(
    ext_modules = cythonize(extensions),
    include_dirs=[np.get_include()]
)

