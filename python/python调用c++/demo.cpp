#include "Eigen/Core"
#include "pybind11/eigen.h" // 使用eigen必须包含，内置自动类型绑定及
#include <pybind11/pybind11.h>


Eigen::Vector3d test(int a, Eigen::Vector3d b) {
    return Eigen::Vector3d(1., 2., 3.)
}
// 指定需要绑定的函数
PYBIND11_MODULE(mymodule, m) {
  m.def("test", &test,
        "test func");
//   m.def("test2", &test,
//         "test func");
}
