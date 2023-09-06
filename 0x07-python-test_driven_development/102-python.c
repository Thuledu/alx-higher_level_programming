#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Error: Invalid string object\n");
        return;
    }

    Py_ssize_t size = PyUnicode_GetLength(p);
    const char *str = PyUnicode_AsUTF8(p);

    printf("String: '%s'\n", str);
    printf("Length: %zd\n", size);
}

