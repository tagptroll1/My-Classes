import logging

from matrix import Matrix

logging.basicConfig(filename="tests.log", level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

mat = Matrix(3, 3, values=2)
mat2 = Matrix(3, 3, values=6)

logging.debug(f"Created Matrix: mat\n{mat}")
logging.debug(f"Created Matrix: mat2\n{mat2}")

logging.debug("performing mat3 = mat2/mat")
mat3 = mat2 / mat
logging.debug(f"mat3\n{mat3}")
logging.debug("performing mat2/=mat")
mat2 /= mat
logging.debug(f"mat2\n{mat2}")
