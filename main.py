the_board = {'a1': ' ', 'b1': ' ', 'c1': ' ',
             'a2': ' ', 'b2': ' ', 'c2': ' ',
             'a3': ' ', 'b3': ' ', 'c3': ' '}

def print_board(board):
    print('   1     2     3')
    print('a   ' + board['a1'] + ' | ' + board['b1'] + '   | ' + board['c1'])
    print('------+-----+-----')
    print('b   ' + board['a2'] + ' | ' + board['b2'] + '   | ' + board['c2'])
    print('------+-----+-----')
    print('c   ' + board['a3'] + ' | ' + board['b3'] + '   | ' + board['c3'])

def main():
    turn = 'X'
    move = ''
    while ' ' in the_board.values():
        print_board(the_board)
        print(turn + ', please choose a square: ')
        move = input()
        the_board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print('game over')
    print_board(the_board)

def check_win:
    win = False
    for k in ['X', 'O']:
    if board['a1'] == k and board['a2'] == k and board['a3'] == k:
        return

main()
