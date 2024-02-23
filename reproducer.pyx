cimport numpy as cnp
cdef cnp.npy_intp dims[2]
pos = cnp.PyArray_ZEROS(2, dims, cnp.NPY_FLOAT32, 0)
cnp.PyArray_FILLWBYTE(pos, 0)
