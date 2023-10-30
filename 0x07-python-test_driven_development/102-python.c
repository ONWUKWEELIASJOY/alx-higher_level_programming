#include <stdlib.h>
#include <python.h>
/**This header file provides the required declarations for Python/C API functions.
 **/
void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        const char *str = PyUnicode_AsUTF8(p);
        if (str != NULL) {
            printf("Python string: \"%s\"\n", str);
            return;
        }
    }

    printf("Error: Invalid Python string\n");
}
