import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n, m = len(A), len(A[0])

    A_t = [[0]*n for i in range(m)]

    for i in range(m):
        for j in range(n):
            A_t[i][j] = A[j][i]

    return np.asarray(A_t)