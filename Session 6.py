def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        
        if all([board[j][i] == player for j in range(3)]):
            return True
        
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, choose a row (0-2): "))
        col = int(input(f"Player {current_player}, choose a column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already occupied. Try again.")
            

play_game()
