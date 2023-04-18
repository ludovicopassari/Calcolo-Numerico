class Matrix(object):

    def __init__(self, custom=None) -> None:
        if not custom:
            self.__matrix = []
        else:
            self.__matrix = custom

    def getMatrix(self) -> list:
        if len(self.__matrix)==0:
            raise Exception('La matrice non contiene elementi...')
        else:
            return self.__matrix

    # crea una matrice identità di ordine n
    def identityMatrix(self, n: int) -> list:
        identity_matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)

            identity_matrix.append(row)

        self.__matrix = identity_matrix

    # crea una matrice randomica n x m di interi o di numeri decimali
    def randomMatrix(self, n: int, m: int, data_type: str = 'integer', decimal_digit: int = 3) -> list:
        import random
        if data_type == 'integer':
            for i in range(n):
                row = []
                for j in range(m):
                    row.append(random.randint(0, 9))
                self.__matrix.append(row)
        elif data_type == 'float':
            for i in range(n):
                row = []
                for j in range(m):
                    row.append(round(random.random()*100, decimal_digit))
                self.__matrix.append(row)

    # check compatibilità somma
    def __checkDimensionSum(self, b: object) -> bool:

        row_count_1 = 0
        column_count_1 = 0
        row_count_2 = 0
        column_count_2 = 0

        for row in self.__matrix:
            row_count_1 += 1
            for column in row:
                column_count_1 += 1

        column_count_1 /= row_count_1

        for row in b.__matrix:
            row_count_2 += 1
            for column in row:
                column_count_2 += 1

        column_count_2 /= row_count_2

        if row_count_1 == row_count_2 and column_count_1 == column_count_2:
            return True
        else:
            return False
    # check compatibilità prodotto

    def __checkDimensionMul(self, b: object) -> bool:

        row_count_1 = 0
        column_count_1 = 0
        row_count_2 = 0
        column_count_2 = 0

        for row in self.__matrix:
            row_count_1 += 1
            for column in row:
                column_count_1 += 1

        column_count_1 /= row_count_1

        for row in b.__matrix:
            row_count_2 += 1
            for column in row:
                column_count_2 += 1

        column_count_2 /= row_count_2

        if row_count_2 == column_count_1:
            return True
        else:
            return False

    def issquareMatrix(self):
        row_count = len(self.__matrix)
        column_count = len(self.__matrix[0])

        if row_count == column_count:
            return True
        else:
            return False

    # override operazione di print

    def __str__(self) -> str:
        result_string = ''
        for row in self.__matrix:
            result_string += str(row)+'\n'
        return result_string

    # override operazione di addizione
    def __add__(self, b: object) -> object:
        sum_matrix = Matrix()
        if self.__checkDimensionSum(b):

            for i in range(len(self.__matrix)):
                row = []
                for j in range(len(self.__matrix[0])):
                    row.append(self.__matrix[i][j]+b.__matrix[i][j])
                sum_matrix.__matrix.append(row)

            return sum_matrix
        else:
            raise Exception(
                'Non puoi sommare due matrici con dimensioni diverse...')

    # override operazione di moltiplicazione
    def __mul__(self, b: object) -> object:
        mul_matrix = Matrix()
        # se il tipo di dato passato come paramentro è di tipo intero o float esegui il prodotto di una mtrice per uno scalare
        if type(b) == int or type(b) == float:
            for i in range(len(self.__matrix)):
                row = []
                for j in range(len(self.__matrix[0])):
                    row.append(b*self.__matrix[i][j])
                mul_matrix.__matrix.append(row)
        # se il tipo di dato passato come parametro è un object type 'Matrix' fai il prodotto riga per colonna
        elif type(b) == Matrix:
            sum_temp = 0
            if self.__checkDimensionMul(b):
                for i in range(len(self.__matrix)):
                    row = []
                    for j in range(len(b.__matrix[0])):
                        sum_temp = 0
                        for k in range(len(b.__matrix)):
                            sum_temp += self.__matrix[i][k]*b.__matrix[k][j]
                        row.append(sum_temp)
                    mul_matrix.__matrix.append(row)
            else:
                raise Exception('Matrici non compatibili...')

        return mul_matrix

    def subMatrix(self, er, ec):
        sub_matrix = Matrix()
        n = len(self.__matrix)

        for r in range(n):
            if (r != er):
                riga = []
                for c in range(n):
                    if (c != ec):
                        riga.append(self.__matrix[r][c])
                sub_matrix.__matrix.append(riga)
        return sub_matrix

    def matrixDeterminant(self):
        matrix_ord = len(self.__matrix)

        if self.issquareMatrix():
            if (matrix_ord == 1):
                return self.__matrix[0][0]

            somma = 0
            segno = +1
            for r in range(matrix_ord):        # Sviluppa la 1° colonna...
                mm = self.subMatrix(r, 0)
                somma += segno*self.__matrix[r][0]*mm.matrixDeterminant()
                segno *= -1
            return somma
        else:
            raise Exception('La matrice non è quadrata...')

    def cofactorMatrix(self):

        matrix_cofactor = Matrix()

        row_count = len(self.__matrix)
        column_count = len(self.__matrix[0])

        sign = +1
        for i in range(row_count):
            row = []
            for j in range(column_count):
                mm = self.subMatrix(i, j)
                cofactor = sign*mm.matrixDeterminant()
                sign *= -1
                row.append(cofactor)
            matrix_cofactor.__matrix.append(row)

        return matrix_cofactor

    def transposeMatrix(self):
        transpose_matrix = Matrix()

        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[0])):
                row.append(self.__matrix[j][i])
            transpose_matrix.__matrix.append(row)

        return transpose_matrix

    def inverseMatrix(self):
        if self.matrixDeterminant() == 0:
            raise Exception('La matrice non è invertibile det() = 0')
        else:
            cofactor_matrix = self.cofactorMatrix()
            cofactor_matrix_T = cofactor_matrix.transposeMatrix()
            inverse_matrix = Matrix()

            for i in range(len(cofactor_matrix_T.__matrix)):
                row = []
                for j in range(len(cofactor_matrix_T.__matrix[0])):
                    row.append(1/self.matrixDeterminant() *
                               cofactor_matrix.__matrix[i][j])
                inverse_matrix.__matrix.append(row)

        return inverse_matrix.transposeMatrix()
