
# coding: utf-8

# Placeholder for functions

# In[1]:


def init_board(n):
    '''
    This function creates a set of coordinates of (row, col), where row is in
    {0,..,n} and col is in {0,...,n}. This is used by the game to keep track 
    of empty cells as the game is played.
    INPUT: integer n (the size of the square matrix)
    OUTPUT: set of coordiates (0,0) through (n,n) which track empty cells
    '''
    empty_cells = set()
    for row in xrange(0,n):
        for col in xrange(0,n):
            empty_cells.add((row,col))
    return empty_cells

def print_board(moves,size):
    '''
    This functions accepts a screen size. The blocks are 4 lines by 5 spaces
    inside the borders of the "square". The rows are (5*size) + 1 long. There
    are (6*size) + 1 columns per row. Each block has a coordinate block in 
    row 1 of the 4 rows.
    This function als0 requires moves, a dictionary of (player: set of 
    moves) combinations. The function uses this to identify non-empty cells.
    INPUT: integer size, dict player_moves {player's name : set of player moves}
    '''
    # First, we need to get the player names out of the dictionary.
    players = moves.keys()
    # Since dictionaries are mapptings, not ordered data objects, we need to print
    # the first character of the player's name in a diamond shape in the square.
    # This also opens the way for more than two players to play at some point.
    # This loop assigns all of the players to their first letter.
    for i in xrange(0, len(players)):
        print players[i]+' is represented by '+players[i][0]
    
    # We make the top/bottom border. For now, it will use Bs for borders.
    # border_char is a constant that is used to build the borders of the cells.
    h_border_char = '_'  # This is the horizontal character used.
    v_border_char = '|'  # This is the vertical character used.
    
    # reference_ruler_horiz allows us to check lengths and positions.
    reference_rule_horiz = '0123456789'*(size - 1)
    horiz_border = h_border_char*((6*size) + 1)
    # print reference_rule_horiz
    # Next, we need to create and print coordinate blocks.
    print horiz_border
    for row in xrange(0,size):
        # coord_block (coordinate block) is where each cell's coordinates print out.
        # cells_row1 of each cell is the first line below the coord_block.
        # cells_row2 of each cell is the second line below the coord_block.
        # cells_row3 of each cell is the third (and last) line below the coord_block.
        # This initializes each line as the current row is constructed.
        coord_block = cells_row1 = cells_row2 = cells_row3 = v_border_char
        for col in xrange(0,size):
            new_cell_coord = "(" + str(row)+"," + str(col) + ")" + v_border_char
            coord_block = coord_block + new_cell_coord
            
            # Now, we need to know if the cell is empty. We set the empty_flag to True.
            empty_flag = True
            for i in xrange(0, len(players)):
                # This block created a block of the player's initial. This sets the first line.
                # Note, this lays the ground work for allowing more than two players at some point.
                if ((row,col) in moves[players[i]]):
                    new_cell_row1 = ' '+players[i][0]*3+' '+ v_border_char
                    empty_flag = False
            if empty_flag == True: new_cell_row1 = ' '*5 + v_border_char
            # The remaining lines mimic the first line.
            new_cell_row2 = new_cell_row1
            new_cell_row3 = new_cell_row1
            # Now, we concatenate the cell contents with the rest of the row.
            cells_row1 = cells_row1 + new_cell_row1
            cells_row2 = cells_row2 + new_cell_row2
            cells_row3 = cells_row3 + new_cell_row3
        print coord_block
        print cells_row1
        print cells_row2
        print cells_row3
        print horiz_border
    return

def create_wins(size):
    '''
    This function takes a size and returns a dictionary with all of the winning move combinations in 
    nested dictionaries of move sets.
    INPUT: integer size
    OUTPUTS: a dictionary of winning built out of three levels of nesting the contents (see
    comments in the funcution.)
    '''
    # The dictionary of winning moves is going to require three levels of nesting. The outermost
    # layer is the "type of win". The key values are: columns, rows, and diagonals. diagonals has
    # only two elements until a smaller win size is implemented.
    # 'columns' connects to a nested dictionary with "size" number of keys.
    # {columns: {0 : set(coordinates of column0), 1 : set(coordinates of column1), ...}}
    # These integer keys then map to a set of coordinates for each column0, ...columnn.
    # 'rows' has the same kind double nesting. 'diagonals' has two keys, ['down', 'up'] and 
    # they, in turn point to their contents. {down: set(coordinates of the down diagonal),
    # up : set (coordinates of the up diagonal)}.

    wins = {}                 # Initialize the master dictionary.
    wins['columns'] = {}      # Initialize the columns dictionary.
    wins['rows'] = {}         # Initialize the rows dictionary.
    wins['diagonals'] = {}    # Initialize the diagonals dictionary.

    print(wins)
    # There are only two diagonal, up and down. So, we will initialize them as empty sets.
    # We will initialize them at the innermost for loop below.
    wins['diagonals']['down'] = set()
    wins['diagonals']['up'] = set()
    print wins

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
    print wins['columns']
    print wins['rows']
    print wins['diagonals']
    return wins

def win_check(moves, winners):
    '''
    This function takes a set of moves (possible or actual) and checks to see if any possible winning
    combination is contained in that set. If so, it returns True. If not, it returns False.
    INPUTS: set moves, which is a set of moves, and dictionary winners. Winners is organized into 
    nested dictionaries: columns, rows, and diagonals. The keys in cols and rows are integers 0 
    through n corresponding to column 0 through n (and rows) on the actual board. diagonals corresponds
    to the up and down diagonals on the board. [At some future point, the logic for diagonals 
    shorter than the board size for winning conditions will be added to make the game more
    interesting.]
    OUTPUT: True if a winning combination is contained in the moves, False otherwise
    NOTE: This function can be used to check if a winning combination exists in the game.
    '''
    # A few notes on the winners dictionary:
    # The dictionary of winning moves has three levels of nesting. The outermost
    # layer is the "type of win". The key values are: columns, rows, and diagonals. diagonals has
    # only two elements until a smaller win size is implemented.
    
    # 'columns' connects to a nested dictionary with "size" number of keys.
    # {columns: {0 : set(coordinates of column0), 1 : set(coordinates of column1), ...}}
    # These integer keys then map to a set of coordinates for each column0, ...columnn.
    # 'rows' has the same kind double nesting. 'diagonals' has two keys, ['down', 'up'] and 
    # they, in turn point to their contents. {down: set(coordinates of the down diagonal),
    # up : set (coordinates of the up diagonal)}.
    # Note: The keys in 'columns' and 'rows' are the same, allowing them to be iterated
    # together. Once win_len is implemented as <= size, there will be more diagonals.

    
    # Basically, we iterate through all of the winnning sets in wins looking to see if
    # the set moves (a set of all of the player's moves in the game so far) contains one
    # of the winning sets of moves.
    
        # Next, we look at the columns and rows. Iterators allow us to work through them quickly.
    for key in winners['columns'].iterkeys():
        if (winners['columns'][key] <= moves):
            return True
        if (winners['rows'][key] <= moves):
            return True
    # So, a winning combination was not found in the rows or columns. Time to check the diagonals.
    if (winners['diagonals']['up'] <= moves):
        return True
    if (winners['diagonals']['down'] <= moves):
        return True
    
    # If the execution made it past all of these tests, no winning combination has been found.
    return False

def create_player_moves(size):
    '''
    This function takes an integer size. From there, it will prompt the players for how many players
    actually want to play. It will allow up to size - 1 to give the players some chance of winning.
    It will return an initialized player_moves dictionary. This dictionary maps the player's name
    to a set of tuples (x,y) representing the two-dimensional coordinates of every move the player
    will make in the game. player_moves does that for every player in the game.
    INPUT: integer size for the size of the size x size board
    OUTPUT: dictionary player_moves, initialized with all player names mapped to empty sets ready to 
    receive their moves.
    '''
    # Initialize the player_moves dictionary.
    player_moves = {}
    max_players = size - 1
    print "To increase the likelihood of a player winning, this game limits the number of"
    print "players to one less than the size of the board."
    num_players = 0
    while (num_players < 2) or (num_players >= size):
        if (size == 3):
            print "Due to the small size of the board (3x3), this game will default to 2 players."
            num_players = 2
        else:
            new_num = raw_input("Please choose a number between 2 and {0}: ".format(max_players))
            num_players = int(new_num)
    # Ordinals in Python seem to be a work in progress. Since the board is currently limited
    # to 9 squares at most, this limits players ordinals to 1st through 8th (for now). So, we
    # initialize a good list to use when addressing the players.
    ordinal_words = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
    
    # Now, we initialize the player_moves dictionary. We need a name for each player, which
    # will be added to the keys of the dictionary. Each name will be mapped to a set of tuples
    # (currently empty), that stores that players moves throughout the game.
    for num in xrange(0, num_players):
        player = raw_input("What is the name of the "+ordinal_words[num]+" player? ")
        player_moves[player] = set()
        print "Confirming that the "+ordinal_words[num]+ " will be "+player
    print player_moves
    ready_to_play = 'n'
    while (ready_to_play != 'y') and (ready_to_play != 'Y') and (ready_to_play != 'yes'):
        ready_to_play = raw_input("Are all of the players ready to start? ")
    return player_moves


# When it asks for player names, this needs to be made into a more generic approach (loop or iterator) -- Done
# 
# The same is true for initializing player_moves. -- Done
# 
# There needs to be a little better spacing between names and questions. -- Done
# 
# I need to include instructions not to use the same first letter in naming a new player. I may need to have something check that in create_player_moves.
# 
# I need to convert the y/n answers to .lower().startswith('y') to make those simpler.
# 
# It might be nice to include a list of players who cannot win each time the board prints out. [This could be done by passing can_win to print_board and having it check for each player in there. I need to use a try/except combo to trap errors from keys not in the can_win dictionary.
# 
# I should consider adding in the ability to clear a terminal (or iPython display). The syntax for iPython display is:
#     from IPython.display import clear_output
# then use clear_input() function to clear the i/o area on screen.
# A crude way to do might be exec(clear) to get the 'OS' to execute a clear.
# 
# Do I want to make the coordinate maps more intuitive (aka, add 1 to them before they print out)? That would require a lot of work to accomplish, but it might also be worth it. Actually, it's easy to do in print_board since it uses nested for loops. It doesn't look too bad to do in the main body. There, I just alter the text output. I also need to subtract 1 from row and col, while displaying row+1 and col+1 throughout.
# 
# I also like his random choice of first player. That might be worth implementing.
# 
# His advanced solution has a rematch option. That might be worth implementing or including a memory option that saves player names to lists.

# In[2]:


print "Hello. You have accessed Tic Tac Toe."
print "The default board is 3x3 and the winner must control three"
print "spaces in a row, column, or diagonal to win."
option = raw_input("You may specify a larger board now, if you like. (y/n):")
if ((option == 'y') or (option == 'Y') or (option == 'yes')):
    # new_size is a str that will be passed to size as an integer.
    new_size = raw_input("The boards are square. Choose a size between 3 and 9:")
    size = int(new_size)
    while size not in range(3,10):
        print new_size+' is an invalid board size. Please try again.'
        new_size = raw_input("Choose a size between 3 and 9.")
        size = int(new_size)
else:
    print "Board will be the default size of 3x3"
    size = 3

# The create_player_moves function initializes the dictionary that stores the 
# player moves as sets of (x,y) tuples (coordinates) mapped to the key which
# is the player's first name.
player_moves = create_player_moves(size)
 
# We take a list of players from the keys in the player_moves dictionary.
players = player_moves.keys()

# We also need the number of players.
num_players = len(players)

# can_win is a very small dictionary with a player name matched to a True/False flag.
# When a player is no longer able to win, their entry is removed from the dictionary.
# Once the dictionary is empty, the game ends in a draw.
can_win = {}                # Create the empty dictionary.
for player in players:
    can_win[player] = True  # Populate it with True values for each player.

# Now, we need to create a dictionary of winning moves. This dictionary has three
# levels of nesting. The outermost layer is "type of win". The key values are: columns,
# rows, and diagonals. diagonals has only two elements until a smaller "win size" is
# implemented. Columns connects to a nested dictionary with "size" number of keys.
# {columns: {0 : set(coordinates of column0), 1 : set(coordinates of column1), ...}}
# These integer keys then map to a set of coordinates for each column0, ...columnn.
# rows has the same kind double nesting. Diagonals has two keys, ['down', 'up'] and 
# they, in turn point to their contents. {down: set(coordinates of the down diagonal),
# up : set (coordinates of the up diagonal)}.
# wins is initialized by the function below:

wins = create_wins(size)

# Next, we need to initialize the board_moves set. As a player takes a cell.
# it will be removed from board_moves and added to their moves set in the 
# player_moves dictionary. This set is composed of coordinates corresponding
# to the coordinate blocks printed in each game cell.

board_moves = init_board(size)

# player_turn tracks who is the next player to be asked for a move.
player_turn = players[0]
move_count = 0
for move_count in xrange(0, size**2):  # This is enough moves to fill the board.
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
            if ((player in can_win) == True):
                del can_win[player]
                print player+" no longer has any moves that will win the game."
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
            if (win_check(player_moves[player], wins) == True):
                print_board(player_moves, size)
                print player+" is the winner."
                break
            else:
                continue
        else:
            continue     # This ensures that the loop will continue when it should.
    break # This ensures than any nested break leave the outermost loop as well.0

