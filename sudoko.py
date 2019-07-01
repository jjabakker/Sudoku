


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

    for i in range(1,10):
        for j in range(1,10):
            analysis_board[i,j] = set([1,2,3,4,5,6,7,8,9])

    board[1,8] = 2
    board[1,9] = 5
    board[2,2] = 6
    board[2,4] = 3
    board[2,6] = 4
    board[3,8] = 6
    board[3,9] = 1
    board[4,2] = 5
    board[4,8] = 8
    board[5,5] = 7
    board[6,1] = 7
    board[6,3] = 3
    board[6,4] = 9
    board[6,5] = 5
    board[6,9] = 2
    board[7,1] = 3
    board[7,3] = 7
    board[7,4] = 5
    board[7,5] = 6
    board[8,6] = 7
    board[9,8] = 7

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



    analyse_board(board, analysis_board)
    m=1

if __name__ == "__main__":
    sudoko_game()
