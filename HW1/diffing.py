# TODO: Nilay Altun, na523
# TODO: Kelly Mayhew, khm53

import dynamic_programming

# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    # TODO: YOUR CODE HERE

    # this is left top corner in the table
    if i == 0 and j == 0:
    	return DiffingCell("-","-",0)

    # j should be same in x axis of the table
    if j == 0:
    	# it is own cost + check the left cell to calculate the total cost
    	cost_j = cost(s[i-1],"-") + table.get(i-1,0).cost
    	return DiffingCell(s[i-1],"-",cost_j)

    # i should be same in y axis of the table
    if i == 0:
    	# it is own cost + check the upper cell to calculate the total cost
    	cost_i = cost("-",t[j-1]) + table.get(0,j-1).cost
    	return DiffingCell("-",t[j-1],cost_i)

    # there is 3 possible choices for each cell in this case. We will get the min cost one
    # s,t should add the diagonal cell    	
    # s,- should add the side cell
    # -,t should add the top cell
    else:

	    choices = { cost(s[i-1],t[j-1]) + table.get(i-1,j-1).cost: [s[i-1], t[j-1]],
	    			cost(s[i-1],"-") + table.get(i-1, j).cost: [s[i-1], "-"],
	    			cost("-",t[j-1]) + table.get(i, j-1).cost: ["-",t[j-1]]
	    }

	    min_cost = min(choices.keys())
	    return DiffingCell(choices[min_cost][0], choices[min_cost][1], min_cost)

# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called
def cell_ordering(n,m):
    # TODO: YOUR CODE HERE
    cells_list= []
    for i in range(n+1):
    	for j in range(m+1):
    		cells_list.append((i,j))
    
    return cells_list

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    # TODO: YOUR CODE HERE
    # cost in bottom right corner will give us the lowest cost
    corner_cell = table.get(len(s),len(t))

    final_cost = corner_cell.cost

    i, j = len(s), len(t)
    align_s, align_t = corner_cell.s_char, corner_cell.t_char

    while not(i == 0 and j == 0):
    	first_char = table.get(i,j).s_char
    	second_char = table.get(i,j).t_char

    	# backtrace by going up
    	if (first_char == "-" and second_char != "-"):
    		j = j - 1

    	# backtrace by going left
    	elif (first_char != "-" and second_char == "-"):
    		i = i - 1

    	# backtrace diagonal
    	else:
    		i = i - 1
    		j = j - 1

    	current_cell = table.get(i, j)
    	if not (current_cell.s_char == "-" and current_cell.t_char == "-"):
	        align_s = align_s + current_cell.s_char
	        align_t = align_t + current_cell.t_char 



    return (final_cost, align_s[::-1], align_t[::-1])

# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print align_s
    print align_t
    print "cost was %d"%cost
