#include <Python.h>
#include <stdio.h>
/**
  *print_python_list_info - Prints basic info about Py lists
  *@p: List checked
  */
void print_python_list_info(PyObject *p)
{
int list_size, memory, idx;
PyObject *target;

list_size = Py_SIZE(p);
memory = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %d\n", list_size);
printf("[*] Allocated = %d\n", memory);
/*iterate through the list*/
for (idx = 0; idx < list_size; idx++)
{
	printf("Element %d: ", idx);
	target = PyList_GetItem(p, idx);
	printf("%s\n", Py_TYPE(target)->tp_name);
}
}
