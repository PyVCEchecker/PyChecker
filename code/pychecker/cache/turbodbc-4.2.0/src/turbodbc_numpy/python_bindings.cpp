#include <turbodbc_numpy/numpy_result_set.h>
#include <turbodbc_numpy/set_numpy_parameters.h>
#include <turbodbc/cursor.h>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// compare http://docs.scipy.org/doc/numpy/reference/c-api.array.html#importing-the-api
// as to why this define is necessary
#define PY_ARRAY_UNIQUE_SYMBOL turbodbc_numpy_API
#include <numpy/ndarrayobject.h>


using turbodbc_numpy::numpy_result_set;


namespace {

numpy_result_set make_numpy_result_set(std::shared_ptr<turbodbc::result_sets::result_set> result_set_pointer)
{
    return numpy_result_set(*result_set_pointer);
}

void set_numpy_parameters(turbodbc::cursor & cursor, std::vector<std::tuple<pybind11::array, pybind11::array_t<bool>, std::string>> const & columns)
{
    turbodbc_numpy::set_numpy_parameters(cursor.get_command()->get_parameters(), columns);
}

}

void * enable_numpy_support()
{
    import_array();
    return nullptr;
}

PYBIND11_MODULE(turbodbc_numpy_support, module) {
    enable_numpy_support();
    module.doc() = "Native helpers for turbodbc's NumPy support";

    pybind11::class_<numpy_result_set>(module, "NumpyResultSet")
        .def("fetch_next_batch", &numpy_result_set::fetch_next_batch);

    module.def("make_numpy_result_set", make_numpy_result_set);
    module.def("set_numpy_parameters", set_numpy_parameters);
}
