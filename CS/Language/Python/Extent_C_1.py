# Preamble
# This tutorial is about extending Python with C, Having a least a basic understanding of C will be very helpful.
# Compiling this on Windows is a done with a different process. So I suggest Googling it if you insist on doing thing on Windows. (Or you can use MingW)

# What are C Extensions?
# Python talking with the C programming language.
# Creation of wrappers which bind python objects to C Functions.
# There is many sub-topic’s of C Extensions.

# What are they for?
# Because of Python’s high level abstractions some things cant be done without a lower level implementation first.
# Perhaps you already have a library of C functions that you want to turn into a python module to use.

# Python Header
# Everything in the Python header starts with the prefix Py or PY.
# The PyObject type is always used as a pointer and is handles all the data parsing between python and C.
# Eg. static PyObject* myFunc(PyObject* self)

# Python.h Functions
# PyArg_ParseTuple(args, format, …)Handles getting the arguments from Python.
# Py_BuildValue(format, …)Handles turning values into PyObject pointers.
# PyModule_Create(moduleDef)Initializes the module and wraps the method pointers using the module definitions.
# If you want your function to return nothing, return the Py_None value.

# PyMethodDef
# The PyMethodDef structure is one of the most critical parts bec ause the compiler wont pick up any errors inside.
# The structure must always end with terminating NULL and 0 values. {NULL, NULL, 0, NULL}
# Here we tell python if the function has argument, no arguments or arguments and keywords.
# MethodDef Example
# static PyMethodDef myMethods[] = {	{“func1”, func1, METH_NOARGS, “func1 doc” },	{“func2”, func2, METH_VARARGS, “func2 doc” },	{NULL, NULL, 0, NULL}}
# Pattern: pyMethodName, function, functionType, Docs
# PyModuleDef
# The PyModuleDef structure is what we use to tell the PyModule_Create() function what information to use to create the module.
# We need to give it a name, documentation, tell python of we will control the module state and the structure of methods to include in the module.
# PyModuleDef
# static struct PyModuleDef myModule = { 	PyModuleDef_HEAD_INIT,	"myModule", #name of module.	"Fibonacci Module", #Module Docs	-1, #-1 the module state is global.	myMethods #method def structure.};
# Our C Program
# Sudo apt-get install python-dev
# Lets create a simple Fibonacci function in C and create the bindings for a module.
# We will also add a version function so we can see a function that doesn’t take arguments.
# Lets call it myModule.c

# The Setup Script
# Now that we have written our c program and created the python binding ready to compile.
# There is a nicely made utility modules that comes with python to make the building and linking easy.
# Lets call out setup script setup.py
# - cmingw32

# Using it!
# Now that we have built our extension it will be output into a build directory.
# We need to copy the module.so file into the directory of our python code. (Or to the python libs folder) Then we can import it!
# Lets create a test.py program

# Notes
# SWIG – Makes this process easier, rather than having to write the bindings, SWIG will generate them for you.
# If you were able to get this example working, using some of the more advanced features of the python header should be easier to understand and implement.

from distutils.core import setup, Extension

module = Extension("myModule", sources = ["myModule.c"])

setup(name = "PackageName",
      version = "1.0",
      description = "This is a package for myModule",
      ext_modules = [module])
