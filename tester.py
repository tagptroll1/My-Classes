from matrix import Matrix

mat = Matrix(3, 3, values=2)
mat2 = Matrix(3, 3, values=3)

print(mat)
print(mat2)

mat3 = mat + mat2
print(mat3)
mat += mat2
print(mat)

mat3 = mat - mat2
print(repr(mat3))
mat -= mat2
print(repr(mat))
