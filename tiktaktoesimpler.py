import random
theBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ','mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ','low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def nextGo(y):
    theBoard
    theBoard[y] = 'O'
    printBoard(theBoard)
    endGame(theBoard)
    

def endGame(board):
    if (board['top-L'] == board['top-M'] == board['top-R'] == 'O') or (board['mid-L'] == board['mid-M'] == board['mid-R'] == 'O') or (board['low-L'] == board['low-M'] == board['low-R'] == 'O') or (board['top-L'] == board['mid-L'] == board['low-L'] == 'O') or (board['top-M'] == board['mid-M'] == board['low-M'] == 'O') or (board['top-R'] == board['mid-R'] == board['low-R'] == 'O') or (board['top-L'] == board['mid-M'] == board['low-R'] == 'O') or (board['top-R'] == board['mid-M'] == board['low-L'] == 'O'):
        print('Game over, you win!!!')
        exec(open('/Users/chrissie/Documents/Python practice/tiktaktoesimpler.py').read())
        
    else:
        theBoard_subset = {key: value for key, value in theBoard.items() if value == ' '}
        compKeys = list(theBoard_subset.keys())
        theBoard[random.choice(compKeys)] = 'X'
        print('Ok, my go!')
        printBoard(theBoard)
        if (board['top-L'] == board['top-M'] == board['top-R'] == 'X') or (board['mid-L'] == board['mid-M'] == board['mid-R'] == 'X') or (board['low-L'] == board['low-M'] == board['low-R'] == 'X') or (board['top-L'] == board['mid-L'] == board['low-L'] == 'X') or (board['top-M'] == board['mid-M'] == board['low-M'] == 'X') or (board['top-R'] == board['mid-R'] == board['low-R'] == 'X') or (board['top-L'] == board['mid-M'] == board['low-R'] == 'X') or (board['top-R'] == board['mid-M'] == board['low-L'] == 'X'):
            print('Game over, I win!!!')
            exec(open('/Users/chrissie/Documents/Python practice/tiktaktoesimpler.py').read())
        else:
            print('Your go!')
            y = input()
            nextGo(y)
        
    
print('Would you like to play Tik Tak Toe (Y or N)?' )
x = input()


if x == 'Y':
    printBoard(theBoard)
    print('Cool. You are "O". You go first, where would you like to go?')
    y = input()
    nextGo(y)
    



    
elif x == 'N':
    print('No worries.')
else:
    print('I can only process "Y" or "N" answers')

