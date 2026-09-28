#Tic Tac Toe
print('Tic Tac Toe')


# print(board[:3],)
# print(board[3:6])
# print(board[6:])

def display(board):
    print(f"-------------")
    print(f"| {1 if board[0] ==' 'else board[0]} | {2 if board[1] ==' 'else board[1]} | {3 if board[2] ==' 'else board[2]} |")
    print(f"-------------")
    print(f"| {4 if board[3] ==' 'else board[3]} | {5 if board[4] ==' 'else board[4]} | {6 if board[5] ==' 'else board[5]} |")
    print(f"-------------")
    print(f"| {7 if board[6] ==' 'else board[6]} | {8 if board[7] ==' 'else board[7]} | {9 if board[8] ==' 'else board[8]} |")
    print(f"-------------")


def user_input(symbol):
    while True:
        try:
            n = int(input('enter a cell number:-'))
            if n in range(1,10):
                if board[n-1] not in ['X','O']:
                    board[n-1] = symbol
                    display(board)
                    break
                else:
                    print('Cell already occupied!')
            else:
                print('Cell number not valid!!!')
        except ValueError:
            print('Invalid input! Please enter a valid cell no')
            

def win(symbol):
    
    #rows
    
    if board[0] == symbol and board[1] == symbol and board[2] == symbol:
        return True
    elif board[3] == symbol and board[4] == symbol and board[5] == symbol:
        return True
    elif board[6] == symbol and board[7] == symbol and board[8] == symbol:
        return True
        
    #columns
    
    elif board[0] == symbol and board[3] == symbol and board[6] == symbol:
        return True
    elif board[1] == symbol and board[4] == symbol and board[7] == symbol:
        return True
    elif board[2] == symbol and board[5] == symbol and board[8] == symbol:
        return True
    
    #diagonals

    elif board[0] == symbol and board[4] == symbol and board[8] == symbol:
        return True
    elif board[2] == symbol and board[4] == symbol and board[6] == symbol:
            return True
    
    else:
        return False
    
def draw():  
    for i in board: 
        if i == ' ':
            return False
    return True

def rematch():
    while True:
        ch = input('Rematch ?(y/n):-')
        if ch == 'y':
            return True
        elif ch == 'n':
            return False
        else:
            print('Invalid choice!!!') 
      

#asking symbol choice from player 1
while True:
    p1 = input('Player 1 select a symbol (X/O):-')
    p1 = p1.lower()
    if p1 in ['x','o']:
        if p1 == 'x':
            p1 = 'X'
            p2 = 'O'
            break
        else:
            p1 = 'O'
            p2 = 'X'
            break
    else:
        print('Invalid Symbol!!!')
        
            
want_to_play = True


while want_to_play:
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display(board)
    turn = 1 
    while True:
        
        if turn == 1:
            print(f"Player 1's turn! ({p1})")
            user_input(p1)
            
            if win(p1):
                print('Player 1 has Won the game!!!!')
                break
                    
            
            if draw():
                print('Draw Game!!!!!')
                break

            turn = 2
            
        else :
            print(f"Player 2's turn! ({p2})")
            user_input(p2)
            
            if win(p2):
                print('Player 2 has Won the game!!!!')
                break
                         
                        
            if draw():
                print('Draw Game!!!!!')
                break

            turn = 1
            
        print('***********************')
        
        
    if rematch():
        want_to_play = True
    else:
        want_to_play = False
        print("\nThanks for playing Tic-Tac-Toe! Goodbye! 👋\n")
         
    


    