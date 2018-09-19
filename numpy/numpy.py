###############################################################################
#   @brief      Numpy playground
#   @author     llHoYall <hoya128@gmail.com>
#   @version    v1.0
#   @note
#       - 2018.04.10    Created.
###############################################################################

# Import Packages ------------------------------------------------------------#
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])

# Dimension
print(np.ndim(A), np.ndim(B))
# >>> 2 2

# Shape
print(A.shape, B.shape)
# >>> (2, 3) (3, 2)

# Inner Product
print(np.dot(A, B))
# >>> [[22 28]
#      [49 64]]
