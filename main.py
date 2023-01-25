from Sparse import SparseMatrix

filename = 'input.txt'
with open(filename) as file:
    input_matr = [line.rstrip() for line in file][0]

str_matr = '[[1,2,0],[0,11,3],[0,0,1]]'

matrix1 = SparseMatrix()

# matrix1.parse(str_matr)
matrix1.parse(input_matr)

matrix1.print_values()

matrix2= matrix1.scalardot(4)
matrix2.print_values()

path = 'output'
matrix2.write_to_file(path)