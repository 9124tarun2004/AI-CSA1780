# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check anti-diagonal
        return True
    return False

# Function to check if the board is full (for draw condition)
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to handle the main game logic
def tic_tac_toe():
    # Initialize the game board (3x3 grid)
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Current player starts with 'X'
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn:")
        
        # Get player input
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")
            continue
        
        # Check if the input is valid
        if row not in range(3) or col not in range(3):
            print("Invalid position! Please enter row and column between 0 and 2.")
            continue
        if board[row][col] != ' ':
            print("That position is already taken. Try another one.")
            continue
        
        # Make the move
        board[row][col] = current_player
        
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
