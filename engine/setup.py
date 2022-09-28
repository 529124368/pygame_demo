from distutils.core import setup
from Cython.Build import cythonize
# E:/anconda/python.exe setup.py build_ext --inplace
setup(
    name='lsz',
    ext_modules=cythonize(["engine.py", "player.py"]),
)
