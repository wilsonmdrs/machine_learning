try:
    from setuptools import setup
    from distutils.core import Extension
    from numpy import *
    from Cython.Build import cythonize
    # np.get_include()
except ImportError:
    from distutils.core import setup

setup(
    name='machine_learning',
    version='1.0.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=[
        'modules',
        'views',
    ],
    py_modules=[
        'app',
    ],
    include_dirs=[np.get_include()],
    # install_requires=['javabridge'],
    # ext_modules=[
    #     Extension("javabridge",["javabridge/_javabridge_mac.c"],
    #               include_dirs=[np.get_include(),
    #                             "/Library/Java/JavaVirtualMachines/jdk1.8.0_261.jdk/Contents/Home/include",
    #                             "/Library/Java/JavaVirtualMachines/jdk1.8.0_261.jdk/Contents/Home/include/darwin",
    #                             "/Users/wilsonmedeiros/.virtualenvs/facecourse-py3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h"]),
    # ],
)
