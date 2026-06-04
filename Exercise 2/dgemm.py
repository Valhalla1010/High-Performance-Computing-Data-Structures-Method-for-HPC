import numpy as np


def matrices_array(n):
    A = np.random.random((n,n)).astype(np.float64)
    B = np.random.random((n,n)).astype(np.float64)
    C= np.zeros_like(A)
    return A, B, C

def dgemm(A, B, C, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C



n = 5
A, B, C = matrices_array(n)
print(f"A:\n{A}")
print(f"B:\n{B}")

C_result = dgemm(A, B, C, n)
print(f"Result:\n{C_result}")




import pytest
def test_dgemm():
    n = 5
    A, B, C = matrices_array(n)
    C_result = dgemm(A, B, C, n)
    C_expected = np.matmul(A, B) 

    np.testing.assert_allclose(C_result, C_expected,)
    