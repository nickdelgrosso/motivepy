from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy

native = Extension(
    'motive.native',
    sources=["src\\native.pyx"],
    include_dirs=["C:\\Program Files\\OptiTrack\\Motive\\inc", "src"],
    library_dirs=["C:\\Program Files\\OptiTrack\\Motive\\lib" ],
    extra_link_args=["/DEFAULTLIB:NPTrackingToolsx64"],
    language="c++"
)

camera = Extension(
    'motive.camera',
    sources=["src\\camera.pyx"],
    include_dirs=["C:\\Program Files\\OptiTrack\\Motive\\inc", "src", numpy.get_include()],
    library_dirs=["C:\\Program Files\\OptiTrack\\Motive\\lib" ],
    extra_link_args=["/DEFAULTLIB:NPTrackingToolsx64"],
    language="c++"
)

rigidbody = Extension(
    'motive.rigidbody',
    sources=["src\\rigidbody.pyx" ],
    include_dirs=["C:\\Program Files\\OptiTrack\\Motive\\inc", "src"],
    library_dirs=["C:\\Program Files\\OptiTrack\\Motive\\lib" ],
    extra_link_args=["/DEFAULTLIB:NPTrackingToolsx64"],
    language="c++"
)


setup(
    name="motive",
    ext_modules= cythonize([native, rigidbody, camera]),
    packages= find_packages(),
    scripts=['scripts/vislight.py', 'scripts/viewer.py'],
    install_requires=['cython', 'appdirs', 'numpy', 'pyqtgraph', 'btk' ],
    package_data= {'': ['data/*.ttp']}
)
