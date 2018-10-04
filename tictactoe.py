# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:26:41 2018

@author: Dell
"""
import numpy
board=numpy.array([['1 1','1 2','1 3'],['2 1','2 2','2 3'],['3 1','3 2','3 3']])
p1s='X'
p2s='O'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,' won')
            return True
    return False
def check_diagonal(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False
def check_columns(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,' won')
            return True
    return False

def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonal(symbol)
def place(symbol):
    print(numpy.matrix(board))
    while 1:
        Row,Col=input("Enter row & col -1,2 or 3: ").split()
        row=int(Row)
        col=int(Col)
        if row>0 and row<4 and col>0 and col<4 and not(board[row-1][col-1]=='X' or board[row-1][col-1]=='O') :
            break
        else:
            print("Please enter a valid number")
    board[row-1][col-1]=symbol

def play():
    for i in range(9):
        if i%2==0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
            print("DRAW")
play()