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
