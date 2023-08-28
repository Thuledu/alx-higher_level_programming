#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Programme that prints basic info about Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p) {
	if (!PyList_Check(p)) {
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *) p)->allocated);

	for (i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - Programme that prints basic info about Python byte objects.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	if (size > 10) {
		size = 10;
	}

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++) {
		printf("%02x", (unsigned char) PyBytes_AsString(p)[i]);
		if (i < size - 1) {
			printf(" ");
		}
	}
	printf("\n");
}

/**
 * print_python_float - Programme that prints basic info about Python float objects.
 * @p: PyObject float object.
 */
void print_python_float(PyObject *p) {
	if (!PyFloat_Check(p)) {
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AsDouble(p));
}
