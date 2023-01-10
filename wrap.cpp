#include "pybind11/pybind11.h"
#include "func.hpp"

namespace py = pybind11;
using namespace pybind11::literals;
PYBIND11_MODULE(wrap, m) {
  m.def("add", &add, "A function which adds two numbers", 
    // "i"_a=1, "j"_a=2 tells pybind11 to generate variables named i with default
    // value 1 and j with default value 2 for the add function.
    "i"_a = 1, "j"_a = 2);
}