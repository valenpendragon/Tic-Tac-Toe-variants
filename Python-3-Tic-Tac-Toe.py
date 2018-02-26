
# coding: utf-8

# # Functions

# In[5]:


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
    players = moves.keys()
    # Since dictionaries are mapptings, not ordered data objects, we need to 
    # print the first character of the player's name in a diamond shape in the
    # square. This also opens the way for more than two players to play at some
    # point. This loop assigns all of the players to their first letter.
    for i in range(0, len(players)):
        print(players[i]+' is represented by '+players[i][0])

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
    for key in wins['columns'].iterkeys():
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


# # Game Code
