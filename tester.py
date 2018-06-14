import logging

from matrix import Matrix

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="tests.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter(
    "%(asctime)s:%(levelname)s:%(message)s"))
logger.addHandler(handler)

mat = Matrix(3, 3, values=2)
mat2 = Matrix(3, 3, values=6)

logger.debug(f"Created Matrix: mat\n{mat}")
logger.debug(f"Created Matrix: mat2\n{mat2}")

logger.debug("performing mat3 = mat2/mat")
mat3 = mat2 / mat
logger.debug(f"mat3\n{mat3}")
logger.debug("performing mat2/=mat")
mat2 /= mat
logger.debug(f"mat2\n{mat2}")
