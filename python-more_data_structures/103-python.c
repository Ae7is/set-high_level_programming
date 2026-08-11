#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <bytesobject.h>
#include <listobject.h>

void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    list = (PyListObject *)p;

    size = ((PyVarObject *)p)->ob_size;
    allocated = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = list->ob_item[i];

        printf("Element %ld: %s\n",
               i,
               item->ob_type->tp_name);

        if (strcmp(item->ob_type->tp_name, "bytes") == 0)
            print_python_bytes(item);
    }
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i, limit;
    char *str;

    printf("[.] bytes object info\n");

    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;

    size = ((PyVarObject *)p)->ob_size;

    str = bytes->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    limit = size + 1;

    if (limit > 10)
        limit = 10;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        printf(" %02hhx", str[i]);

    printf("\n");
}
