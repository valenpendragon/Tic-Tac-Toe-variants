def start_screen(size=3):
    '''
    This functions accepts a screen size, defaulting to 3 if not specified.
    The blocks are 4 lines by 5 spaces inside the borders of the "square".
    The rows are (5*size) + 1 long. There are (6*size) + 1 columns per row.
    Each block has a coordinate block in row 1 of the 4 rows.
    INPUT: integer size, defaults to 3
    '''
    # First, we make the top/bottom border. For now, it will use Bs for borders.
    # border_char is a constant that is used to build the borders of the cells.
    border_char = 'B'
    # reference_ruler (horiz and vert) allows us to check lengths and positions.
    reference_rule_horiz = '0123456789'*(size - 1)
    horiz_border = border_char*((5*size) + 1)
    print reference_rule_horiz
    print horiz_border
    # Next, we need to create and print coordinate blocks.
    for row in xrange(0,1):      # For now, this is just row 0.
        coord_block = border_char
        for col in xrange(0,size):
            new_block = "(" + str(row)+"," + str(col) + ")" + border_char
            coord_block = coord_block + new_block
        print horiz_border
        print coord_block
    return
