from matrix import Matrix

mat = Matrix(3, 3, values=2)
mat2 = Matrix(3, 3, values=6)

print(mat)
print(mat2)

mat3 = mat2 / mat
print(mat3)
mat2 /= mat
print(mat2)
