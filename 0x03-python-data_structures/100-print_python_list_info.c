#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *pyton_ls = (PyListObject *)p;
	size_t i = 0, largo =  PyList_Size(p);

	printf("[*] Size of the Python List = %lu\n", largo);
	printf("[*] Allocated = %lu\n", pyton_ls->allocated);
	for (i = 0; i < largo; i++)
		printf("Element %lu: %s\n", i, Py_TYPE(pyton_ls->ob_item[i])->tp_name);
}
