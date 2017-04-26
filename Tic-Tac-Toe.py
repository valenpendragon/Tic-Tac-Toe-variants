print "Hello. You have accessed Tic Tac Toe."
print "The default board is 3x3 and the winner must control three"
print "spaces in a row, column, or diagonal to win."
option = raw_input("You may specify a larger board now, if you like. (y/n):")
if ((option == 'y') or (option == 'Y') or (option == 'yes')):
    # new_size is a str that will be passed to size as an integer.
    new_size = raw_input("The boards are square. Choose a size between 3 and 9:")
    size = int(new_size)
    if size in range(3,10):
        print "Thank you. Confirming that you wish a "+new_size+'x'+new_size+' board.'
    else:
        print new_size+' is an invalid board size. Exiting.'
        quit()
else:
    print "Board will be the default size of 3x3"
    size = 3
# The size has been initialized. Next, it asks for player names. These will be
# used to initial the dictionary player_moves. This dictionary is in the form
# {'player1' : {set of moves}, 'player2' : {set of moves}}. These sets are key
# to refreshing the board, determining wins, etc.
player1 = raw_input("What is the name of the first player?")
print "Thank you. Confirming that the first player is "+player1
player2 = raw_input("what is the name of the second player?")
print "Thank you. Confirming that the second player is "+player2

print player1+' and '+player2+', I am initializing the game for you.'
print "This will just take a moment."

# Initializing player_moves. Note, they are empty sets.
player_moves = {}
player_moves[player1] = set()
player_moves[player2] = set()

# We also need the number of players.
num_players = len(players)

# Now, we need to create a dictionary of winning moves. This is going to require three
# levels of nesting. The outermost layer is type of win. These key values are: column,
# row, or diagonal. diagonal has only two elements until a smaller win size is
# implemented. Columns connects to a nested dictionary with "size" number of keys.
# {column: {0 : set(coordinates of column0), 1 : set(coordinates of column1), ...}}
# These integer keys then map to a set of coordinates for each column0, ...columnn.
# rows has the same kind double nesting. Diagonal has two keys, ['down', 'up'] and 
# they, in turn point to their contents. {down: set(coordinates of the down diagonal),
# up : set (coordinates of the up diagonal)}.

wins = {}                 # Initialize the master dictionary.
wins['columns'] = {}      # Initialize the columns dictionary.
wins['rows'] = {}         # Initialize the rows dictionary.
wins['diagonals'] = {}    # Initialize the diagonals dictionary.

# print wins
# There are only two diagonal, up and down. So, we will initialize them as empty sets.
# We will initialize them at the innermost for loop below.
wins['diagonals']['down'] = set()
wins['diagonals']['up'] = set()
# print wins

# This for loop will iterate the rows and columns nested dictionaries to initialize
# the sets at the second nested level.
for i in xrange(0, size):
    wins['columns'][i] = set()
    wins['rows'][i] = set()
    # The down diagonal has ascending rows and columns. The tough one is the up 
    # or ascending diagonal. The columns ascend as the rows descend. Performing
    # this inside the nested loop would make it repeat the steps, without adding
    # anything (sets are unique elements).
    wins['diagonals']['down'].add((i,i))          # both ascend in value
    wins['diagonals']['up'].add((size - i -1,i))     # cols ascend while rows descend
    
    # Now, we focus on adding the size number of cell coordinates that make up row, 
    # column, and diagonal wins. They will addressed via the next nested loop.
    for j in xrange(0, size):
        wins['columns'][i].add((j,i))  # Here, j is ascending rows on column i.
        wins['rows'][i].add((i,j))     # Here, j is the right moving column in row i.
# print wins['columns']
# print wins['rows']
# print wins['diagonals']

# Next, we need to initialize the board_moves set. As a player takes a cell.
# it will be removed from board_moves and added to their moves set in the 
# player_moves dictionary. This set is composed of coordinates corresponding
# to the coordinate blocks printed in each game cell.

board_moves = init_board(size)

# player_turn tracks who is the next player to be asked for a move.
player_turn = player1
move_count = 0
for num in xrange(0, size**2):  # This is enough moves to fill the board.
    # Print the board based on current moves
    print_board(player_moves, size)
    
    print player_turn+", it is your turn. I will prompt you for row and column."
    print "Use single digits less than "+str(size)+". I will do the rest."
    row = raw_input("Which row?")
    row = int(row)
    if ((row in range(0,size)) != True ):
        print "Please try again. The row was invalid."
        continue
    col = raw_input("Which col?")
    col = int(col)
        if ((col in range(0,size)) != True ):
        print "({},{}) is not available. Please try again.".format(row,col)
        print "Available spaces: ", board_moves
        continue
    if ((row,col) in board_moves) != True:
        # That cell is occupied already.
        print "That move is not available. Please try again."
        continue
    print "("+str(row)+","+str(col)+") is available."
    # Record the player's move.
    player_moves[player_turn].add((row,col))
    # Remove their choice from availale moves.
    board_moves.discard((row,col))
    # Increment the move count
    move_count += 1
    # Use the move count to determine the next player in the sequence.
    next_player = move_count % num_players
    player_turn = players[next_player]

    for player in players:
        # Now, we check to see if it is possible for either player to win with the moves that are
        # left on the board. That is why the union of player_moves[player] with board_moves, 
        # the remaining open cells, is checked for winning conditions. A False return means that
        # the player cannot win.
        if (win_check(player_moves[player].union(board_moves), wins) == False):
            del can_win[player]
            print player+" no longer has any moves that will win the game."
            print can_win
    if (len(can_win) == 0):
        print_board(player_moves, size)
        print "No players have moves that can win the game. This game is a draw."
        break  # At this level, this break ends the outermost loop.
    else:
        # Before prompting the next player to take their turn, we need to see
        # if any player has already won the game. That was the purpose of having "win condition" sets.
        # We send to win_check the set of player's moves. wins is an argument as well. Since we 
        # plan to check to see if any winning combinations remain, we need to make this process a 
        # function, instead part of the main program. What this program does is check to see if
        # any player won yet.
        for player in players:
            # First, we check to see if a win has occurred.
            # if (win_check(player_moves[player], wins) == True):
            if False == True:
                print_board(player_moves, size)
                print player+" is the winner."
                break
            else:
                continue
        else:
            continue     # This ensures that the loop will continue when it should.
    break # This ensures than any nested break leave the outermost loop as well.
