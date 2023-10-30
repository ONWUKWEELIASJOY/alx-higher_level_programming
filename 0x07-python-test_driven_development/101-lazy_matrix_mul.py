#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Convert m_a and m_b to NumPy arrays
    arr_a = np.array(m_a)
    arr_b = np.array(m_b)

    # Perform matrix multiplication using NumPy
    result = np.matmul(arr_a, arr_b)

    return result.tolist()

