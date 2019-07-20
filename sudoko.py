



def print_board(board):

    '''
    Print the board in a grid format with the numbers as placed
    '''

    print('_' * 24)
    for i in range(1, 10):
        print('|', end='')
        for j in range(1, 10):
            if board[i, j] == 0:
                pstr = '  '
            else:
                pstr = ' ' + str(board[i, j])
            print(pstr, end='')
            if j in (3, 6, 9):
                print(' ', end='|')

        if i in (3, 6, 9):
            print('')
            print('_' * 24, end=' ')
        print('\n')




def print_analysis_board(analysis_board):

    '''
    Print for each field the possible choices that are left - use a grid format
    '''

    print('_' * 106)
    for i in range(1, 10):
        print('| ', end='')
        for j in range(1, 10):

            aset = analysis_board[i, j]
            str1 = ""
            for a in aset:
                str1 = str1 + '%s' % a
            str2 = '%-10s' % str1
            print(str2, end=' ')
            if j in (3, 6, 9):
                print(' ', end='|')

        if i in (3, 6, 9):
            print('\n', '_' * 106)
        print('\n')


def initialise_board(board, analysis_board):

    '''
    Read in the file with positions.
    Fill the board (containing the positions)
    Fill the analysis_board (containing the remaining possibilities for each empty field)
    '''

    #  Empty the board - a 0 means 'empty'
    for i in range(1, 10):
        for j in range(1, 10):
            board[i, j] = 0

    # Expected file format per line is 'row - col - number'
    filename = input(f'Specify the sudoku filename:  ')

    try:
        f = open(filename, "r")
    except:
        print("File not found")
        exit()

    for line in f:
        x = line.split(' ')
        board[int(x[0]), int(x[1])] = int(x[2])

    # Initially every field in the analysis board can contain the full set of 1 - 9
    for i in range(1, 10):
        for j in range(1, 10):
            analysis_board[i, j] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # for all the fields with already a number tge set is emptied
    for i in range(1, 10):
        for j in range(1, 10):
            if board[i, j] != 0:
                #analysis_board[i, j] = set([board[i, j]])
                analysis_board[i, j] = set()


def analyse_board(board, analysis_board):
    for i in range(1, 10):
        for j in range(1, 10):
            if board[i, j] != 0:

                # remove that value from everything in the row
                for k in range(1, 10):
                    analysis_board[k, j].discard(board[i, j])

                # remove that value from everything in the column
                for k in range(1, 10):
                    analysis_board[i, k].discard(board[i, j])

                # remove that value from everything in the main square

                ii = ((i - 1) // 3) * 3 + 1
                jj = ((j - 1) // 3) * 3 + 1

                for k1 in range(ii, ii + 3):
                    for k2 in range(jj, jj + 3):
                        analysis_board[k1, k2].discard(board[i, j])

                # remove that value from everything in the grey square

                ii = 0
                jj = 0
                if i == 2 or i == 3 or i == 4:
                    ii = 2
                elif i == 6 or i == 7 or i == 8:
                    ii = 6

                if j == 2 or j == 3 or j == 4:
                    jj = 2
                elif j == 6 or j == 7 or j == 8:
                    jj = 6

                if ii != 0 and jj != 0:
                    for k1 in range(ii, ii + 3):
                        for k2 in range(jj, jj + 3):
                            analysis_board[k1, k2].discard(board[i, j])

    # If in analysis board there is a field that has a set length of 1 then that field can contain only one number
    # and that means that you have found a solution

    found = False
    for i in range(1, 10):
        for j in range(1, 10):
            if len(analysis_board[i, j]) == 1:
                print(f'\n\nFound one: {i} {j}: {analysis_board[i, j]}')
                q = analysis_board[i, j].pop()
                board[i, j] = q
                analysis_board[i, j] = set()
                found = True
                analyse_board(board, analysis_board)

    return found


def ppnb(number_board):

    '''
    Print the options of each of the four core boards
    '''

    print('_' * 36)
    for i in range(1, 4):
        for j in range(1, 4):
            print('|', end='')
            aset = number_board[i, j]
            str1 = " "
            for a in aset:
                str1 = str1 + '%s' % a
            str2 = '%-10s' % str1
            print(str2, end=' ')

        print('|')
    print('_' * 36)
    print('\n')


def print_board_core(analysis_board):
    number_board = {}

    for i in range(2, 5):
        for j in range(2, 5):
            number_board[i - 1, j - 1] = analysis_board[i, j]
    ppnb(number_board)

    for i in range(2, 5):
        for j in range(6, 9):
            number_board[i - 1, j - 5] = analysis_board[i, j]
    ppnb(number_board)

    for i in range(6, 9):
        for j in range(2, 5):
            number_board[i - 5, j - 1] = analysis_board[i, j]
    ppnb(number_board)

    for i in range(6, 9):
        for j in range(6, 9):
            number_board[i - 5, j - 5] = analysis_board[i, j]
    ppnb(number_board)



def print_number_board(number, analysis_board, board):
    number_board = {}

    for i in range(1, 10):
        for j in range(1, 10):
            number_board[i, j] = ' '

    for i in range(1, 10):
        for j in range(1, 10):
            if board[i, j] == number:
                number_board[i, j] = '*'
            if number in analysis_board[i, j]:
                number_board[i, j] = number

    print('_' * 24)
    for i in range(1, 10):
        print('| ', end='')
        for j in range(1, 10):
            print(f'{number_board[i, j]}', end=' ')
            if j in (3, 6, 9):
                print('| ', end='')
        if i in (3, 6, 9):
            print('\n', end='')
            print('_' * 24, end='')

        print('\n')
    print('\n')


def sudoko_game():
    board = {}
    analysis_board = {}

    initialise_board(board, analysis_board)
    print_board(board)
    analyse_board(board, analysis_board)
    print_board(board)

    while True:
        cmd = input('Command? ')

        if cmd == '':
            pass
        elif cmd == 'pb':
            print('\n')
            print_board(board)
        elif cmd == 'pa':
            print_analysis_board(analysis_board)
            print('\n')
        elif cmd[0] == 'n':
            try:
                i = int(cmd[1])
                if i in range(1, 10):
                    print_number_board(i, analysis_board, board)
                else:
                    continue
            except:
                continue
        elif cmd == 'pc':
            print_board_core(analysis_board)
        elif cmd[0] == 's':
            x = cmd.split(' ')
            try:
                i = int(x[1])
                j = int(x[2])
            except:
                continue
            analysis_board[i, j] = set()
            board[i, j] = int(x[3])
            analyse_board(board, analysis_board)
        elif cmd[0] == 'r]':
            initialise_board(board, analysis_board)
        elif cmd[0] == 'q':
            exit()
            print('\n')
        else:
            pass


if __name__ == "__main__":
    sudoko_game()
