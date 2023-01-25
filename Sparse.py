import re
import json

class SparseMatrix():
    def __init__(self, values=[], cols=[], rows=[]):
        self.values = []
        self.cols = []
        self.rows = []

    def print_values(self):
        print(f'Values {self.values}')
        print(f'Columns {self.cols}')
        print(f'Rows {self.rows}')


    def write_to_file(self, path):
        with open(f'{path}.txt', 'w') as fw:
            json.dump(self.values, fw)
            json.dump(self.cols, fw)
            json.dump(self.rows, fw)
            print(f'Записано в файл {path}.txt')

    def parse(self, string):
        col_idx = 0
        row_idx = 0

        items = string.split(',')

        for el in items:

            # начало матрицы
            if re.match('\\[\\[\d+', el) is not None:
                cur_value = el.split('[[')[1]
                if cur_value != '0':
                    self.values.append(int(cur_value))
                    self.rows.append(row_idx)
                    self.cols.append(col_idx)
                col_idx += 1

            # начало строки матрицы
            elif re.match('\\[\d+', el) is not None:
                cur_value = el.split('[')[1]
                if int(cur_value) > 0:
                    self.values.append(int(cur_value))
                    self.rows.append(row_idx)
                    self.cols.append(col_idx)
                col_idx += 1

            # конец строки матрицы
            elif re.match('\d+\\]', el) is not None:
                cur_value = el.split(']')[0]
                if int(cur_value) > 0:
                    self.values.append(int(cur_value))
                    self.rows.append(row_idx)
                    self.cols.append(col_idx)
                row_idx += 1
                col_idx = 0

            # конец  матрицы
            elif re.match('\d+\\]\\]', el) is not None:
                cur_value = el.split(']]')[0]
                if int(cur_value) > 0:
                    self.values.append(int(cur_value))
                    self.rows.append(row_idx)
                    self.cols.append(col_idx)
                return 0

            elif el == '0':
                col_idx += 1

            elif re.match('\d+', el) is not None:
                self.values.append(int(el))
                self.rows.append(row_idx)
                self.cols.append(col_idx)
                col_idx += 1


    def dot(self, SomeSparseMatrix):
        result = SparseMatrix()

        cur_dot_value = 0

        if (max(self.rows) != max(self.cols) ) or  (max(SomeSparseMatrix.rows) != max(SomeSparseMatrix.cols) ):
            print('матрицы не являются квадратными')

        else:
            indexes_A = [str(row) + str(col) for row,col in zip(self.rows, self.cols)]
            indexes_B = [str(row) + str(col) for row,col in zip(SomeSparseMatrix.rows, SomeSparseMatrix.cols)]

            for i in range(max(self.rows)):
                for j in range(max(self.cols)):
                    cur_dot_value = self.values[indexes_A.index(str(i) + str(j))] * SomeSparseMatrix.values[
                            indexes_B.index(str(i) + str(j))]
                    if cur_dot_value != 0:
                        result.values.append(cur_dot_value)
                        result.rows.append(i)
                        result.cols.append(j)
        return result

    def add(self, SomeSparseMatrix):
        result = SparseMatrix()

        cur_dot_value = 0

        if (max(self.rows) != max(self.cols)) or (max(SomeSparseMatrix.rows) != max(SomeSparseMatrix.cols)):
            print('матрицы не являются квадратными')

        else:
            indexes_A = [str(row) + str(col) for row, col in zip(self.rows, self.cols)]
            indexes_B = [str(row) + str(col) for row, col in zip(SomeSparseMatrix.rows, SomeSparseMatrix.cols)]

            for i in range(max(self.rows)):
                for j in range(max(self.cols)):
                    cur_dot_value = self.values[indexes_A.index(str(i) + str(j))] + SomeSparseMatrix.values[
                        indexes_B.index(str(i) + str(j))]
                    if cur_dot_value != 0:
                        result.values.append(cur_dot_value)
                        result.rows.append(i)
                        result.cols.append(j)
        return result

    def scalardot(self, scalar):
        result = SparseMatrix()
        result.values = [el*scalar for el in self.values]
        result.rows = self.rows
        result.cols = self.cols
        return result