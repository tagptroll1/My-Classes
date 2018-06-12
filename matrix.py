class Matrix:
    def __init__(self, values=None, data_type=int, row=5, col=5):
        self.data_type = data_type
        self.width = 5
        self.rows = row
        self.cols = col
        self.shape = (self.rows, self.cols)
        self.matrix = [[values] * self.cols for y in range(self.rows)]


    def __add__(self, other):
        new_matrix = Matrix(data_type=self.data_type, 
                            row=self.rows, col=self.cols)

        # Check if it's another matrix of same shape and datavalue
        if isinstance(other, Matrix):
            if self.data_type is not other.data_type:
                raise TypeError("Matrices does not contain same data type")

            if self.shape != other.shape:
                raise ShapeError(
                    f"Both matrices must have the same shape {self.shape}, and {other.shape} were used")
            # If shape and datatype is correct, add every cell of same position together
            for row in range(self.rows-1):
                for col in range(self.cols):
                    if self.matrix[row][col] is not None and other.matrix[row][col] is not None:
                        new_matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
        
        return new_matrix


    def __sub__(self, other):
        new_matrix = Matrix(data_type=self.data_type,
                            row=self.rows, col=self.cols)

        # Check if it's another matrix of same shape and datavalue
        if isinstance(other, Matrix):
            if self.data_type is not other.data_type:
                raise TypeError("Matrices does not contain same data type")

            if self.shape != other.shape:
                raise ShapeError(
                    f"Both matrices must have the same shape {self.shape}, and {other.shape} were used")

            # If shape and datatype is correct, add every cell of same position together
            for row in range(self.rows-1):
                for col in range(self.cols):
                    if self.matrix[row][col] is not None and other.matrix[row][col] is not None:
                        new_matrix[row][col] = self.matrix[row][col] - \
                            other.matrix[row][col]

        return new_matrix


    def __iadd__(self, other):
        # Check if it's another matrix of same shape and datavalue
        if isinstance(other, Matrix):
            if self.data_type is not other.data_type:
                raise TypeError("Matrices does not contain same data type")

            if self.shape != other.shape:
                raise ShapeError(
                    f"Both matrices must have the same shape {self.shape}, and {other.shape} were used")
            # If shape and datatype is correct, add every cell of same position together
            for row in range(self.rows-1):
                for col in range(self.cols):
                    if self.matrix[row][col] is not None and other.matrix[row][col] is not None:
                        self.matrix[row][col] += other.matrix[row][col]

        return self



    def __isub__(self, other):
        # Check if it's another matrix of same shape and datavalue
        if isinstance(other, Matrix):
            if self.data_type is not other.data_type:
                raise TypeError("Matrices does not contain same data type")

            if self.shape != other.shape:
                raise ShapeError(
                    f"Both matrices must have the same shape {self.shape}, and {other.shape} were used")

            # If shape and datatype is correct, add every cell of same position together
            for row in range(self.rows-1):
                for col in range(self.cols):
                    if self.matrix[row][col] is not None and other.matrix[row][col] is not None:
                        self.matrix[row][col] -= other.matrix[row][col]

        return self


    def __getitem__(self, key):
        # Check if key is a slice
        if isinstance(key, slice):
            # If theres no stop [x:] fetch the row of x
            if key.start is not None and key.stop is None:
                return self.matrix[key.start]
            # If theres no start [:y] generate list of column values
            elif key.start is None and key.stop is not None:
                return [row[key.stop] for row in self.matrix]
            elif all(x is None for x in [key.start, key.stop]):
                raise SyntaxError("matrix index must use 1 or 2 integers")
            # Fetches x from start, and y from stop
            else:
                return self.matrix[key.start][key.stop]
        # Else check if it's an int to return a whole row
        elif isinstance(key, int):
            return self.matrix[key]
        # Nothing supported, raise error
        else:
            raise TypeError


    def __setitem__(self, key, val):
        # Check if val is correct data type
        if type(val) is not self.data_type:
            raise TypeError(
                f"Matrix takes {self.data_type}, {val} of type {type(val)} was given ")

        # Assign new max width, if its bigger
        self.width = max(self.width, len(str(val))+1)
        # Check if key is a slice
        if isinstance(key, slice):
            # Fetches x from start, and y from stop
            self.matrix[key.start][key.stop] = val
        # Nothing supported, raise error
        else:
            raise TypeError

    def __repr__(self):
        matrix_display = ",\n ".join(map(str, self.matrix))
        return f"""[{matrix_display}]\
                \rNumber of rows: {self.rows}\
                \rNumber of columns: {self.cols}\
                \rShape: {self.shape}\
                \rData type: {self.data_type}\n"""
            
    def __str__(self):
        join_width = " " * (self.width - 1)
        return_string = f"\t {join_width.join([f'{_}.' for _ in range(self.cols)])}\n"

        for row in range(self.rows):
            return_string += f"{row}. "
            for col in range(self.cols):
                return_string += f"{str(self.matrix[row][col]):>{self.width}}"
            return_string += "\n"
        
        return return_string
        #return "\n".join(map(str, self.matrix))
        """ Join string version of displaying matrix by Wattle
        heading = '{:5} {}'.format('',
            ' '.join(format(f'{i}.', '<5') for i in range(COLS)))

        body = '\n'.join('{:<5} {}'.format(f'{i}.',
            ' '.join(f'{str(cell):<5}' for cell in row))
            for i, row in enumerate(matrix))

        return heading + '\n' + body
        """

    
class ShapeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
