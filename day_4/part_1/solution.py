data_sections = []
draw_order = []
draw_index = 0
drawn_numbers = []
bingo_boards = []
board_scores = []
winner = None

#########################################################
#helper functions
#check if bingo board is winner
#no diagonals, assumes list of 25 entries (5x5 board)
def check_winner(board):
    #first, check for horizontal winnings
    horz_roots = [0, 5, 10, 15, 20]
    for root in horz_roots:
        pos_to_check = [root, root+1, root+2, root+3, root+4]
        board_numbers = []
        for pos in pos_to_check:
            board_numbers.append(board[pos])
        if set(board_numbers).issubset(drawn_numbers):
            return True
    
    #then, check for vertical winnings
    vert_roots = [0, 1, 2, 3, 4]
    for root in vert_roots:
        pos_to_check = [root, root+5, root+10, root+15, root+20]
        board_numbers = []
        for pos in pos_to_check:
            board_numbers.append(board[pos])
        if set(board_numbers).issubset(drawn_numbers):
            return True
    return False

def calculate_score(board):
    sum_unmarked = 0
    for number in board:
        if number not in drawn_numbers:
            sum_unmarked += int(number)
    last_number = int(drawn_numbers[-1])
    return sum_unmarked * last_number
#########################################################

with open("input.txt", "r", encoding='utf-8') as input:
    data = input.read()
    ##data is split by empty lines "\n\n"
    data_sections = data.split("\n\n")

#draw order is listed in the input first.
draw_order = data_sections[0].split(',')

#bingo boards are listed next, all the way to the end.
for board in data_sections[1:]:
    #remove newlines
    board_data = board.replace("\n", " ")
    board_data = board_data.strip()
    #fix double spaces
    while "  " in board_data:
        board_data = board_data.replace("  ", " ")
    bingo_boards.append(board_data.split(" "))

#draw numbers until a winner is found
while winner == None:
    drawn_numbers.append(draw_order[draw_index])
    draw_index += 1
    for board in bingo_boards:
        if check_winner(board):
            winner = board

print('found winner!')
print('drawn: ' + str(drawn_numbers))
print('board: ' + str(winner))
print('score: ' + str(calculate_score(winner)))