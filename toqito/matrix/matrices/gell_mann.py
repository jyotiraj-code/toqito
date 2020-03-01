"""Produces a Gell-Mann operator."""
import numpy as np
from scipy.sparse import csr_matrix


def gell_mann(ind: int, is_sparse: bool = False) -> np.ndarray:
    """
    Produce a Gell-Mann operator.

    Generates the 3-by-3 Gell-Mann matrix indicated by the value of `ind`.
    `ind = 0` gives the identity matrix, while values 1 through 8 each indicate
    one of the other 8 Gell-Mann matrices.

    References:
    [1] Wikipedia: Gell-Mann matrices,
        https://en.wikipedia.org/wiki/Gell-Mann_matrices

    :param ind: An integer between 0 and 8 (inclusive).
    :param is_sparse: Boolean to determine whether matrix is sparse.
    """
    if ind == 0:
        gm_op = np.identity(3)
    elif ind == 1:
        gm_op = np.array([[0, 1, 0],
                          [1, 0, 0],
                          [0, 0, 0]])
    elif ind == 2:
        gm_op = np.array([[0, -1j, 0],
                          [1j, 0, 0],
                          [0, 0, 0]])
    elif ind == 3:
        gm_op = np.array([[1, 0, 0],
                          [0, -1, 0],
                          [0, 0, 0]])
    elif ind == 4:
        gm_op = np.array([[0, 0, 1],
                          [0, 0, 0],
                          [1, 0, 0]])
    elif ind == 5:
        gm_op = np.array([[0, 0, -1j],
                          [0, 0, 0],
                          [1j, 0, 0]])
    elif ind == 6:
        gm_op = np.array([[0, 0, 0],
                          [0, 0, 1],
                          [0, 1, 0]])
    elif ind == 7:
        gm_op = np.array([[0, 0, 0],
                          [0, 0, -1j],
                          [0, 1j, 0]])
    elif ind == 8:
        gm_op = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, -2]])/np.sqrt(3)
    else:
        raise ValueError("Gell-Mann index values can only be values from 0 to "
                         "8 (inclusive).")

    if is_sparse:
        gm_op = csr_matrix(gm_op)

    return gm_op
