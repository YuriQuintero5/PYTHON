class Matrix:
     # Initializer / Instance Attributes
    def __init__(self, cadena):
        self.cadena = cadena
        self.matriz = self.get_matrix(cadena)

    def get_matrix(self, cadena):
        cadena = str(cadena)
        fil = cadena.split('\n')
        matrix = []
        for col in fil:
            fila = []
            celdas = col.split(' ')
            for item in celdas:
                fila.append(item.strip())
            matrix.append(fila)
        return matrix

    def columnas(self):
        #cols = map(len, mat)
        #print('Columnas')
        col_matrix = ''
        cols = len(self.matriz)
        for i in range(cols):
            # print(self.__column(i))
            col_matrix = '{}\n{}|{}'.format(col_matrix, i+1, self.__join(self.__column(i), ','))
        return col_matrix


    def filas(self):
        # print('Filas')
        row_matrix = ''
        rows = len(self.matriz)
        for i in range(rows):
            # print(self.matriz[i])
            row_matrix = '{}\n{}|{}'.format(row_matrix, i+1, self.__join(self.matriz[i], ','))
        return row_matrix

    def __column(self, i):
        return [row[i] for row in self.matriz]

    def __join(self, l, sep):
        out_str = ''
        for i, el in enumerate(l):
            out_str += '{}{}'.format(el, sep)
        return out_str[:-len(sep)]