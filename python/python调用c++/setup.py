import glob
import os

import pybind11
from setuptools import Extension, setup

# 添加多个库例子
# opencv_lib_dir = "/usr/local/lib"
# opencv_libraries = [
#     os.path.splitext(os.path.basename(lib))[0][3:]
#     for lib in glob.glob(opencv_lib_dir + "/libopencv*.so")
# ]
setup(
    name="mymodule",
    ext_modules=[
        Extension(
            "mymodule",
            ["demo.cpp"], # 用到的cpp都加上,否则会出现为定义的symbol 
            include_dirs=[
                pybind11.get_include(),
                ".",
                "/home/gotpl/.xmake/packages/e/eigen/3.4.0/23adbe82fb82491f97ed0eac9cde1818/include/eigen3/",
                # "/usr/local/include/opencv4/",
            ],
            # library_dirs=[*opencv_libraries],
            language="c++",
        ),
    ],
    zip_safe=False,
)
