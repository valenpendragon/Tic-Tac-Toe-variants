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

    print wins
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

