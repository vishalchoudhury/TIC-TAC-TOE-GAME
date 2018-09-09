def clear_output():
    print('\n'*100)

#Win check
def win_check(board,marker):
    for i,v in enumerate(board[1:5]):
#        print(i,v)
        if i == 1:
#            print("one")
            if [board[i],board[i+1],board[i+2]] == [marker,marker,marker]:
                print("You have won")
                return True
            elif [board[i],board[i+3],board[i+6]] == [marker,marker,marker]:
                print("You have won")
                return True
            elif [board[i],board[i+4],board[i+8]] == [marker,marker,marker]:
                print("You have won")
                return True
        elif i == 2:
#            print("two")
            if [board[i],board[i+3],board[i+6]] == [marker,marker,marker]:
                print("you have won")
                return True
        elif i == 3:
#            print("three")
            if [board[i],board[i+2],board[i+4]] == [marker,marker,marker]:
                print("You have won")
                return True
            elif [board[i],board[i+3],board[i+6]] == [marker,marker,marker]:
                print("You have won")
                return True
    return False

#Displaying the board
def display_board(board):
    clear_output()
    patterns = {1:[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],2:['-','-','-','-','-','-','-','-','-','-','-'],3:[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '], 4: [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '], 5: [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']}
    for key,value in patterns.items():
        if key == 3:
            value[1] = board[1]
            value[5] = board[2]
            value[9] = board[3]
        if key == 4:
            value[1] = board[4]
            value[5] = board[5]
            value[9] = board[6]
        if key == 5:
            value[1] = board[7]
            value[5] = board[8]
            value[9] = board[9]
    test_board = [1,3,1,2,1,4,1,2,1,5,1]
    for pattern in test_board:
        print(''.join(patterns[pattern]))
        
#choosing the symbol
def player_input():
    player1=''
    while True:
        player1 = input('Choose your symbol X or O: ').upper()
        if player1 in ['X','O']:
            break
    return player1

#Choosing the position
def choose_pos(board):
    while True:
        pos = int(input("Choose your position: "))
        if pos in range(1,10):
            if board[pos] == ' ':
                return pos
            else:
                print('Choose another position.')
        else:
            print("Choose the position from 1-9\nTry Again!")
            
#Marking the posiiton            
def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)

play = 'Y'
while play.upper() == 'Y': 
    count = 1
    player1 = player_input()
    if player1 == 'X':
        player2 = 'O'
        
    else:
        player2 = 'X'
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while count <= 9:
        #clear_output()
        position = choose_pos(board)
        if(count % 2 != 0):
            place_marker(board,player1,position)
            if win_check(board,player1):
                break
        else:
            place_marker(board,player2,position)
            if win_check(board,player2):
                break
        count += 1
    if(count == 10):
        print("There is a TIE!")
    play = input('Do you want to play again? Y or N: ')
    if play.upper() == 'N':
        print('Thanks for Playing!')
    clear_output()