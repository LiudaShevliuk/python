#!/usr/bin/env python3
# -*- coding: utf-8 -*-

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
marks = ['X','O']
computer = []
player = []
wins = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def is_winner(board, smb):
    return ((board[0] == smb and board[1] == smb and board[2] == smb) or  
            (board[3] == smb and board[4] == smb and board[5] == smb) or  
            (board[6] == smb and board[7] == smb and board[8] == smb) or  
            (board[0] == smb and board[3] == smb and board[6] == smb) or  
            (board[1] == smb and board[4] == smb and board[7] == smb) or  
            (board[2] == smb and board[5] == smb and board[8] == smb) or  
            (board[0] == smb and board[4] == smb and board[8] == smb) or  
            (board[2] == smb and board[4] == smb and board[6] == smb))  

def free_cells(board):
    count = 0
    for i in board:
        if i not in marks:
            count += 1
    return count

def take_edge(board, smb):
    if board[0] not in marks:
        board[0] = smb
        return 0
    elif board[2] not in marks:
        board[2] = smb
        return 2
    elif board[6] not in marks:
        board[6] = smb
        return 6
    elif board[8] not in marks:
        board[8] = smb
        return 8
    else:
        return -1

def take_free(board, smb):
    for i in board:
        if str(i).isdigit():
            board[i] = smb
            return i

def computer_move(board, smb):
    if board[4] == 4:
        board[4] = smb
        computer.append(4)
        return
    if free_cells(board) >= 7:
        computer.append(take_edge(board, smb))
        return
    if marks[0] == smb:
        enemy = marks[1]
    else:
        enemy = marks[0]

    for win in wins:
        if len(set(win) & set(computer)) == 2:
            i = (set(win) - set(computer)).pop()
            if board[i] not in marks:
                board[i] = smb
                computer.append(i)
                return

    for win in wins:
        if len(set(win) & set(player)) == 2:
            i = (set(win) - set(player)).pop()
            if board[i] not in marks:
                board[i] = smb
                computer.append(i)
                return

    edge = take_edge(board, smb)

    if edge != -1:
        computer.append(edge)
        return

    computer.append(take_free(board, smb))


def get_user_move(board):
    try:
        move = int(input("Enter cell number: "))
        if board[move] in marks:
            return get_user_move(board)
        else:
            return move
    except:
        return get_user_move(board)

def get_figure():
    figure = input("Choose X or O: ")
    if figure in marks:
        return figure
    else:
        return get_figure()

def draw_board(board):
    print('     |     |')
    print(' ', board[0], ' | ', board[1], ' | ', board[2])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print(' ', board[3], ' | ', board[4], ' | ', board[5])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print(' ', board[6], ' | ', board[7], ' | ', board[8])
    print('     |     |')

def start_game(board):
    user = get_figure()
    if marks[0] == user:
        computer_figure = marks[1]
    else:
        computer_figure = marks[0]

    if computer_figure == 'X':
        computer_move(board, computer_figure)

    for i in range(5):
        draw_board(board)
        move = get_user_move(board)
        player.append(move)
        board[move]=user
        if is_winner(board, user):
            print("You win!")
            return
        draw_board(board)
        computer_move(board, computer_figure)
        if is_winner(board, computer_figure):
            print("Computer win!")
            draw_board(board)
            return

start_game(board)
