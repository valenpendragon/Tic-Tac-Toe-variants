
# coding: utf-8

# #Functions

# In[4]:


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

