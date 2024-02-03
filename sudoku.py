import numpy as np
def rc_possible(matrix,cell,in_square):
    numbers = np.arange(1,10)
    row=[]
    column=[]
    square=[]
    for x in numbers:
        if str(x) not in matrix[cell[0]]:
            row.append(x)
 
        if str(x) not in matrix[:,cell[1]]:
            column.append(x)
  
        if str(x) not in in_square:
            square.append(x)
    return row,column,square

def in_square(dicti,cell):
    if cell[0]>=0 and cell[0]<=2 and cell[1]>=0 and cell[1]<=2:
        return dicti['0']
    if cell[0]>=0 and cell[0]<=2 and cell[1]>=2 and cell[1]<=5:
        return dicti['1']
    if cell[0]>=0 and cell[0]<=2 and cell[1]>=5 and cell[1]<=8:
        return dicti['2']
    if cell[0]>=3 and cell[0]<=5 and cell[1]>=0 and cell[1]<=2:
        return dicti['3']
    if cell[0]>=3 and cell[0]<=5 and cell[1]>=2 and cell[1]<=5:
        return dicti['4']
    if cell[0]>=3 and cell[0]<=5 and cell[1]>=5 and cell[1]<=8:
        return dicti['5']
    if cell[0]>=6 and cell[0]<=8 and cell[1]>=0 and cell[1]<=2:
        return dicti['6']
    if cell[0]>=6 and cell[0]<=8 and cell[1]>=2 and cell[1]<=5:
        return dicti['7']
    if cell[0]>=6 and cell[0]<=8 and cell[1]>=5 and cell[1]<=8:
        return dicti['8']

def possible(row,column,square):
    possible=[]
    for x in row:
        if x in column and x in square:
            possible.append(x)
    return possible

def squares(matrix):
    dicti = {}
    dicti['0']=matrix[0:3,0:3]
    dicti['1']=matrix[0:3,3:6]
    dicti['2']=matrix[0:3,6:9]
    dicti['3']=matrix[3:6,0:3]
    dicti['4']=matrix[3:6,3:6]
    dicti['5']=matrix[3:6,6:9]
    dicti['6']=matrix[6:9,0:3]
    dicti['7']=matrix[6:9,3:6]
    dicti['8']=matrix[6:9,6:9]
    return dicti

def possible_matrix(board):
    possible_ = [[[] for _ in range(len(board))] for _ in range(len(board))]
    square_ = squares(board)
    for i in range(len(board)):
        for j in range(len(board)):
            i = int(i)
            j = int(j)
            if board[i][j]=='.':
                in_square_ = in_square(square_,[i,j])
                row,column,square = rc_possible(board,[i,j],in_square_)
                possible_[i][j]=possible(row,column,square)
    return possible_

def add_values(board,possible_matrix):
    for i in range(9):
        for j in range(9):
            if len(possible_matrix[i][j])==1:
                board[i][j] = possible_matrix[i][j][0]
                
def sudoku_solver(input_board):
    new_board = np.copy(input_board)
    while '.' in new_board:
        p=possible_matrix(new_board)
        add_values(new_board,p)
    print("Input:\n",input_board)
    print("\nSolved:\n",new_board)
