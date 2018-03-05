
# coding: utf-8

# # Functions

# In[10]:


#pip.main(['install', 'num2words'])


# In[11]:


def init_board(n):
    '''
    This function creates a set of coordinates of (row, col), where row is in
    {0,..,n} and col is in {0,...,n}. This is used by the game to keep track 
    of empty cells as the game is played.
    INPUT: integer n (the size of the square matrix)
    OUTPUT: set of coordiates (0,0) through (n,n) which track empty cells
    '''
    empty_cells = set()
    for row in range(0,n):
        for col in range(0,n):
            empty_cells.add((row,col))
    return empty_cells

def print_board(moves,size):
    '''
    This functions accepts a screen size. The blocks are 4 lines by 5 spaces
    inside the borders of the "square". The rows are (5*size) + 1 long. There
    are (6*size) + 1 columns per row. Each block has a coordinate block in 
    row 1 of the 4 rows make it up.
    This function also requires moves, a dictionary of (player: set of 
    moves) combinations. The function uses moves to identify non-empty cells.
    INPUT: integer size, dict player_moves {player's name : set of player moves}
    OUTPUT: None. All output goes to the screen.
    '''
    # First, we need to get the player names out of the dictionary.
    players = list(moves.keys())
    # Since dictionaries are mapptings, not ordered data objects, we need to 
    # print the first character of the player's name in a diamond shape in the
    # square. This also opens the way for more than two players to play at some
    # point. This loop assigns all of the players to their first letter.
    for i in range(0, len(players)):
        print("{0}' is represented by {1}".format(players[i], players[i][0]))

    # We make the top/bottom border.
    h_border_char = '_'  # This is the horizontal character used.
    v_border_char = '|'  # This is the vertical character used.
    
    # reference_ruler_horiz allows us to check lengths and positions.
    # It was only used to help out with getting the sizing correct.
    # Just add a print command to use it.
    reference_rule_horiz = '0123456789'*(size - 1)
    
    # This is the horizontal border at the top, between each row of
    # cells, and across the bottom of the board.
    horiz_border = h_border_char*((6*size) + 1)
    
    print(horiz_border)
    # This is a text game. That means that we have to construct strings
    # for each line that forms the board before printing out the board.
    # So, we need to start with rows of characters, concatenating the
    # pieces that form the cells in each column of the row.
    for row in range(0,size):
        # coord_block (coordinate block) is where each cell's coordinates
        # print out. We build it one cell per column for each row.
        # cells_row1 is built from the first line below the coord_block for
        # cells in each column of the board.
        # cells_row2 is built from the second line below the coord_block.
        # cells_row3 is built from the third line below the coord_block.
        # Remember: Each cell of the game board is 4 lines by 5 columns
        # in a form like this:
        #              occupied       empty
        #              _______       _______
        # coord_block  |(n,n)|       |(n,n)|
        # _row1        | PPP |       |     |
        # _row2        | PPP |       |     |
        # _row3        | PPP |       |     |
        #              _______       _______
        # All of the rows are have separater lines above and below.
        # This initializes each line as the current row is constructed.
        coord_block = cells_row1 = cells_row2 = cells_row3 = v_border_char
        for col in range(0,size):
            # First, we need build a string, new_cell_coord, that contains
            # the information for the coordinate block for row.
            new_cell_coord = "(" + str(row)+"," + str(col) + ")" + v_border_char
            # Next, we add this new coord block to the row's coordinate block.
            coord_block = coord_block + new_cell_coord
            # Now, we need to know if the cell is empty. We initialize
            # empty_flag as True.
            empty_flag = True
            for i in range(0, len(players)):
                # Now, we need to run through all of the players and see if
                # this cell appears in the set of their moves. If so, the
                # cell is not empty. We will flip the flag and construct
                # the three rows that form the cell accordingly. These cells
                # are denoted by _row1,, _row2, and _row3. We only need to
                # construct the first, as the other 2 are copies.
                # Note, this lays the ground work for allowing more than two
                # players at some point.
                if ((row,col) in moves[players[i]]):
                    new_cell_row1 = ' '+players[i][0]*3+' '+ v_border_char
                    empty_flag = False
            # Now, if the flag is still True, we can create a 5 character
            # blank line for _row1 of the new cell. Otherwise, it will skip
            # this command.
            if empty_flag == True: 
                new_cell_row1 = ' '*5 + v_border_char
            # The remaining rows in the cell mimic _row1.
            new_cell_row2 = new_cell_row1
            new_cell_row3 = new_cell_row1

            # Now, we concatenate the cell contents with the rest of each row.
            cells_row1 = cells_row1 + new_cell_row1
            cells_row2 = cells_row2 + new_cell_row2
            cells_row3 = cells_row3 + new_cell_row3
        
        # Once each row is complete, print out the row of cells, complete with
        # a border line at the bottom of the cells.
        print(coord_block)
        print(cells_row1)
        print(cells_row2)
        print(cells_row3)
        print(horiz_border)
    return

def create_wins(size):
    '''
    This function takes a size and returns a dictionary with all of the 
    winning move combinations in nested dictionaries of move sets.
    INPUT: integer size
    OUTPUTS: a dictionary of winning built out of three levels of nesting
        the contents (see comments in the function.)
    '''
    # The dictionary of winning moves is going to require three levels
    # of nesting. The outermost layer is the "type of win". The key values
    # are: columns, rows, and diagonals.
    # diagonals has only two elements until a smaller win size is
    # implemented. 
    # 'columns' connects to a nested dictionary with "size" number of keys.
    # {columns: {0 : set(coordinates of column0),
    #            1 : set(coordinates of column1),
    #            ...
    #            N : set(cordinates of columnN)}}
    # These integer keys then map to a set of coordinates for each column0,
    # column1, column2, ..., columnN.
    # 'rows' has the same kind double nesting. 
    # 'diagonals' has two keys, ['down', 'up']. These keys, in turn, point
    # to their contents:
    #      {down: set(coordinates of the down diagonal),
    #       up  : set (coordinates of the up diagonal)}.

    wins = {}                 # Initialize the master dictionary.
    wins['columns'] = {}      # Initialize the columns dictionary.
    wins['rows'] = {}         # Initialize the rows dictionary.
    wins['diagonals'] = {}    # Initialize the diagonals dictionary.
    # print(wins)
    
    # There are only two diagonal, up and down.
    wins['diagonals']['down'] = set()
    wins['diagonals']['up'] = set()
    # print(wins)

    for i in range(0, size):
        # This for loop will iterate the rows and columns nested
        # dictionaries to initialize the sets at the second nested
        # level, e.g. wins['columns'][0] = set(). Although this
        # looks like a list, 0 is actually a key.
        wins['columns'][i] = set()
        wins['rows'][i] = set()
        # The down diagonal has ascending rows and columns. The tough one
        # is the up or ascending diagonal. The columns ascend as the rows
        # descend. Performing this inside the nested loop would make it
        # repeat the steps, without adding anything (sets are unique
        # elements).
        # rows and columns ascend together for down.
        row = col = i
        wins['diagonals']['down'].add((row, col))
        # columns ascend while rows descend.
        row = size - i - 1
        col = i
        wins['diagonals']['up'].add((row, col))
    
        # Now, we focus on adding the size number of cell coordinates
        # that make up row and column wins.
        for j in range(0, size):
            # Here, j is ascending rows on column i.
            row = j
            col = i
            wins['columns'][i].add((row, col))
            # Here, j is the right moving column in row i.
            row = i
            col = j
            wins['rows'][i].add((row, col))
    # print(wins['columns'])
    # print(wins['rows'])
    # print(wins['diagonals'])
    return wins

def win_check(moves, wins):
    '''
    This function takes a set of moves (possible or actual) and checks
    to see if any possible winning combination is contained in that set.
    If so, it returns True. If not, it returns False.
    INPUTS: two arguments
        moves (set) a set of moves
        winners (dict)
            Winners is organized into nested dictionaries: columns, rows,
            and diagonals. The keys in cols and rows are integers 0 
            through n corresponding to column 0 through n (and rows) on
            the actual board. diagonals corresponds to the up and down
            diagonals on the board. [At some future point, the logic for
            diagonals shorter than the board size for winning conditions
            will be added to make the game more interesting.]
    OUTPUT: True if a winning combination is contained in the moves, False
        otherwise
    NOTE: This function can be used to check if a winning combination
    exists in the game.
    '''
    # A few notes on the winners dictionary:
    # The dictionary of winning moves has three levels of nesting.
    # The outermost layer is the "type of win". The key values are: 
    # columns, rows, and diagonals. diagonals has only two elements
    # until a smaller win size is implemented. See comments in the
    # function, create_wins for more details.
    
    # Note: The keys in 'columns' and 'rows' are the same, allowing
    # them to be iterated together. Once win_len is implemented as
    # <= size, there will be more diagonals.

    # Basically, we iterate through all of the winnning sets in wins
    # looking to see if the set moves (a set of all of the player's
    # moves in the game so far) contains one of the winning sets of
    # moves. The syntax for this if statement is set1 <= set2 (set1
    # is fully contained in set2).
    
    # First, we look at the columns and rows. Iterators allow us to
    # work through them quickly.
    for key in wins['columns'].keys():
        if (wins['columns'][key] <= moves):
            return True
        if (wins['rows'][key] <= moves):
            return True
        
    # So, a winning combination was not found in the rows or columns.
    # Time to check the diagonals.
    if (wins['diagonals']['up'] <= moves):
        return True
    if (wins['diagonals']['down'] <= moves):
        return True
    
    # If the execution made it past all of these tests, no winning
    # combination has been found.
    return False

def create_player_moves(size):
    '''
    This function takes an integer size. From there, it will prompt
    the players for how many players actually want to play. It will
    allow up to size - 1 to give the players some chance of winning.
    It will return an initialized player_moves dictionary. This
    dictionary maps the player's name to a set of tuples (x,y)
    representing the two-dimensional coordinates of every move the
    player will make in the game. create_player_moves does that for
    every player in the game.
    INPUT: integer size for the size of the size x size board
    OUTPUT: dictionary player_moves, initialized with all player
        names mapped to empty sets ready to receive their moves.
    '''
    # Initialize the player_moves dictionary.
    player_moves = {}
    max_players = size - 1
    print("To increase the likelihood of a player winning, this game")
    print("limits the number of players to one less than the size of")
    print("the board.")
    num_players = 0
    while (num_players < 2) or (num_players >= size):
        if (size == 3):
            print("Due to the small size of the board (3x3), this game will")
            print("default to 2 players.")
            num_players = 2
        else:
            new_num = input("Please choose a number between 2 and {0}: ".format(max_players))
            try:
                num_players = int(new_num)
            except:
                print("That number was invalid. Please try again.")
            # Note: Either num_players is non-zero, or the string could
            # not be converted to an integer. Either way, the while
            # loop will handle it correctly.

    # Anaconda makes it very very difficult to add modules, like
    # num2words to the installation because it creates so many 
    # in ProgramData and AppData. One of these is not getting the
    # right update to add it. conda does not recognize the package;
    # so, I am still stuck with using an ordinal words list, which
    # limits this program to 9x9.
    ordinal_words = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
    
    # Now, we initialize the player_moves dictionary. We need a name
    # (string) for each player, which will be added to the keys of
    # the dictionary. Each name will be mapped to a set of tuples that
    # starts out empty). The set stores that players moves throughout
    # the game.
    print("Please enter the names of the players. Do not duplicate")
    print("first initials to avoid confusion between players.")
    for num in range(0, num_players):
        player_name = input("What is the name of the player? ".format(ordinal_words[num]))
        player_moves[player_name] = set()
        print("Confirming that the {0} will be {1}".format(ordinal_words[num], player_name))
    print(player_moves)
    ready_to_play = 'n'
    while (ready_to_play.lower() != 'y') and (ready_to_play.lower() != 'yes'):
        ready_to_play = input("Are all of the players ready to start? (y/n) ")
    return player_moves

# This is a new function created for the Python3 conversion.
def get_number(coord_type, size):
    """
    This function asks the players for a number, either for a row or column
    number, determined by coord_type. It uses size to determine if the 
    number is a valid choice before returing this value.
    INPUTS: two arguments
        coord_type: string, no default, only 'row' or 'column' are valid
        size: integer, no default
    OUTPUTS: integer between 0 and size
    """
    choice = -1
    while choice not in range(0, size):
        # choice must be a valid row or column choice or the while loop
        # will not stop iterating. It must be an integer in the range
        # [0, size].
        trial = input("Which {0}? ".format(coord_type))
        try:
            choice = int(trial)
        except:
            print("{0} must be between 0 and {1}".format(coord_type,size))
            print("Please try again.")
    return choice


# # Game Code

# In[12]:


print("Hello. Welcome to Tic Tac Toe.")
print("The default board is 3x3 and the winner must control three")
print("spaces in a row, column, or diagonal to win. The boards are square.")
option = input("Would you like a larger board? (y/n):")
if (option.lower() == 'y') or (option.lower() == 'yes'):
    # new_size is a str that will be passed to size as an integer.
    size = 0
    while size not in range(3, 10):
        new_size = input("Choose a board size between 3 and 9:")
        # This option keeps the program in the loop until a valid
        # integer for the size is chosen.
        try:
            size = int(new_size)
        except:
            print("{0} is an invalid board size. Please try again.".format(new_size))
            continue
                
else:
    print("Board will be the default size of 3x3.")
    size = 3

# The create_player_moves function initializes the dictionary that
# stores the player moves as sets of (x,y) tuples (coordinates)
# mapped to the key which is the player's first name.
player_moves = create_player_moves(size)
 
# We make a list of players from the keys in the player_moves
# dictionary. The items are sets of each player's moves. Sets
# are used to prevent duplication.
players = list(player_moves.keys())

# We also need the number of players.
num_players = len(players)

# can_win is a very small dictionary with a player name matched
# to a True/False flag. When a player is no longer able to win,
# their entry is removed from the dictionary. Once the
# dictionary is empty, the game ends in a draw. We populate this
# 
can_win = {}
for player in players:
    can_win[player] = True

# Now, we need to create a dictionary of winning moves. The wins
# dictionary is fully described in the comments in the function
# create_wins() above.
wins = create_wins(size)

# Next, we need to initialize the set board_moves. This stores all
# of the possible moves that can be made in the game. Using a set
# ensures that there can be no duplication of moves.As a player
# takes a cell, tis coordinate tuple (horizontal, verticle), will
# removed from board_moves and added to their set of moves in the 
# player_moves dictionary. This set is composed of coordinates
# corresponding to the coordinate blocks printed in each game cell.
board_moves = init_board(size)

# The player_turn variable tracks which player is next in line to
# make a move on the board. move_count iterates through all of the
# possible moves on the board, although the game has code to end
# the game when a winner is found or a stalemate has been reached.
# We have a boolean player_won. A player win will flip this flag.
# A second boolean, stalemate, becomes True is no players have
# any moves left that can win the game.
player_turn = players[0]
move_count = 0
player_won = False
stalemate = False
while move_count < size**2:  # Game move loop
    # Print the board based on current moves. It does this each
    # iteration before prompting the next player for a move.
    print_board(player_moves, size)

    print("{}, it is your turn. I will prompt you for row and column.".format(player_turn))
    print("Please use single digits less than {0}. I will do the rest.".format(str(size)))
    # We use a second while loop to make sure that the space is
    # not occupied. The valid_move boolean is used to control
    # this loop. The funcion, get_number makes sure that the row
    # and column choices are integers between 0 and size.
    valid_move = False
    while not valid_move:
        row = get_number('row', size)
        col = get_number('column', size)
        if (row,col) in board_moves:
            print("({0}, {1}) is empty. Registering the move.".format(row, col))
            # Record the player's move.
            player_moves[player_turn].add((row,col))
            # Remove their choice from availale moves.
            board_moves.discard((row,col))
            # Increment the move count
            move_count += 1
            valid_move = True
        else:
            # That cell is already occupied.
            print("That cell is already occupied. Please choose another.")
            continue

    # The move has been registerd. We need to print the board
    # again to reflect the change.
    print_board(player_moves, size)
    
    # Only the player who just made a move can win in any
    # event. win_check returns a boolean. With the options
    # below, it will return Turn that the player who just
    # moved won, and False, if not.
    if win_check(player_moves[player_turn], wins):
        print("Congratulations, {0}, you won the game.".format(player_turn))
        player_won = True
        break # This break ends the outermost loop.
    
    # This routine was moved down and the block handling
    # player win checks was added above.
    for player in players:
        # Now, we check to see if it is possible for any player
        # to win with the moves that are left on the board. That
        # is why the union of player_moves[player] with
        # board_moves, the remaining open cells, is checked for
        # winning conditions. A False return means that the
        # player cannot win. If that results come up, the
        # player is removed from can_win list.
        if not win_check(player_moves[player].union(board_moves), wins):
            if player in can_win:
                del can_win[player]
                print("{} no longer has any moves that will win the game.".format(player))
    if (len(can_win) == 0):
        print("No players have moves that can win the game. This game is a draw.")
        stalemate = True
        break  # This break ends the outermost loop.

    # Getting this far (the end of the move loop, the game
    # may still be winnable. Use the move count to determine
    # the next player in the sequence.
    next_player = move_count % num_players
    player_turn = players[next_player]
    # End of game move loop.

# In case the game reached this point with all spaces on
# the board filled without a winner, we need to declare a
# draw. The stalemate flag and player_won flag show which
# options occurred. If they are unchanged, the game ended
# with a full board. This is unlikely to happen without
# can_win emptying first, but we have to allow for it.
if (not player_won) and (not stalemate):
    print("The game board is full, but no player won the game.")
    print("The game is a draw.")

