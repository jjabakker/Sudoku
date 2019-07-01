


def print_board(board):

    for i in range(1,10):
        for j in range(1,10):
            print(board[i,j], end = ' ')
            if j in (3, 6):
                print('\t', end = ' ')
        if i in (3, 6):
            print('\n', end =' ')
        print('\n')

def print_analysis_board(analysis_board):

    for i in range(1,10):
        for j in range(1,10):

            aset = analysis_board[i,j]
            str = ""
            for a in aset:
                str = str+ '%s' % a
            str1 = '%-10s' % str
            print(str1, end = ' ')
            if j in (3, 6):
                print(' ', end = ' ')
        if i in (3, 6):
            print('\n', end =' ')
        print('\n')

def initialise_board(board, analysis_board):

    for i in range(1,10):
        for j in range(1,10):
            board[i,j] = 0


    filename = input(f'Specify the sudoku filename:  ')

    try:
        f = open(filename, "r")
    except:
        print ("File not found")
        exit()

    for line in f:
        x = line.split(' ')
        board[int(x[0]), int(x[1])] = int(x[2])


    for i in range(1, 10):
        for j in range(1, 10):
            analysis_board[i, j] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for i in range(1, 10):
        for j in range(1, 10):
            if board[i, j] != 0:
                analysis_board[i, j] = set([board[i, j]])
                analysis_board[i, j] = set()


def analyse_board(board, analysis_board):

    for i in range(1,10):
        for j in range(1,10):
            if board[i,j] != 0:

                # remove that value from everything in the row
                for k in range(1, 10):
                    analysis_board[k,j].discard(board[i, j])

                # remove that value from everything in the column
                for k in range(1, 10):
                    analysis_board[i, k].discard(board[i, j])

                # remove that value from everything in the main square

                ii = ((i - 1)// 3) * 3 + 1
                jj = ((j - 1)// 3) * 3 + 1

                for k1 in range(ii, ii+3):
                    for k2 in range (jj,jj+3):
                        analysis_board[k1, k2].discard(board[i, j])

                # remove that value from everything in the grey square

                ii = 0
                jj = 0
                if (i == 2 or i == 3 or i == 4 ):
                    ii = 2
                elif (i == 6 or i == 7 or i == 8 ):
                    ii = 6

                if (j == 2 or j == 3 or j == 4):
                    jj = 2
                elif (j == 6 or j == 7 or j == 8):
                    jj = 6

                if ii != 0 and jj != 0:
                    for k1 in range(ii, ii + 3):
                        for k2 in range(jj, jj + 3):
                            analysis_board[k1, k2].discard(board[i, j])

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


def sudoko_game():

    board = {}
    analysis_board = {}

    initialise_board(board, analysis_board)
    print_board(board)
    print_analysis_board(analysis_board)

    while True:
        analyse_board(board, analysis_board)
        print_board(board)
        print('\n')
        print_analysis_board(analysis_board)
        print('\n')

        if input('Suggestion?') == 'y':
            x = int(input ('Row: '))
            y = int(input ('Col: '))
            v = int(input ('Val: '))
            analysis_board[x,y]=set()
            board[x,y] = v
            print('\n')
            print_board(board)
            print('\n')
        else:
            break

    print('\n\n')
    print_board(board)

if __name__ == "__main__":
    sudoko_game()
