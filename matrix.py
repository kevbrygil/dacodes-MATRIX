# Probado con python 2.7.15 y 3.6.8
# ejemplo de ejecución:
# python matrix.py
# python3 matrix.py

import sys

right, down, left, up = 0,1,2,3
i=0
address = right
lines = int (input (u'T?'.encode('utf-8')))

if(lines < 1 and lines > 5000):
    sys.exit(u'Debe respetar la condicion: 1 \<= T \<= 5000'.encode('utf-8'))

limit_matrix = pow(10,9)

rows = int (input (u'N?'.encode('utf-8')))
if(rows < 1 and rows > limit_matrix):
    sys.exit(u'Debe respetar la condicion: 1\<= N \<= 10\xe59'.encode('utf-8'))

columns = int (input (u'M?'.encode('utf-8')))

if(columns < 1 and columns > limit_matrix):
    sys.exit(u'Debe respetar la condicion: 1\<= M \<= 10\xe59'.encode('utf-8'))

matrix = []

max = rows * columns

if(lines > max):
    sys.exit(u'Excede el limite de lineas de salidas'.encode('utf-8'))

for row in range(rows):
    matrix.append([])
    for column in range(columns):
        matrix[row].append(-1)
row,column = 0,0

print('\nResult:\n')

while matrix[row][column] == -1:
    if(lines == 0):
        sys.exit(u'Termino de lineas de salida'.encode('utf-8'))
    matrix[row][column] = i
    i += 1
    lines -= 1
    if address==right:
        print('R')
        if column+1 < columns and matrix[row][column+1] == -1:
            column += 1
        else:
            address = down
            row += 1
    elif address==down:
        print('D')
        if row + 1<rows and matrix[row+1][column] ==-1:
            row += 1
        else:
            address = left
            column -= 1
    elif address==left:
        print('L')
        if column>0 and matrix[row][column-1] == -1:
            column -=1
        else:
            address = up
            row -= 1
    elif address==up:
        print('U')
        if row>0 and matrix[row-1][column] == -1:
            row -= 1
        else:
            address = right
            column += 1
