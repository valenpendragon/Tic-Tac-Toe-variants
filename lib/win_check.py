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
