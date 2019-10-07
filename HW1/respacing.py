# TODO: Nilay Altun, na523
# TODO: Kelly Mayhew, khm53

# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    #TODO: YOUR CODE HERE
    #Skip cell if row > column by returning default cell
    if i > j or j == len(string) or i == len(string):
        return RespaceTableCell(False, None)

    #Check if substring is a word
    wordCheck = is_word(string[i:j+1])

    #The substring was a word and could be the first word
    if wordCheck and (i == 0):
        return RespaceTableCell(True, 0)

    #Substring is a word, but not the first one
    #Requires more processing
    elif wordCheck and (i > 0):
        #Step back through column of table to see if there's a word before this
        pastWord = False
        for x in range(len(string)+1):
            #If x>i-1, we haven't filled the cell (and won't). Skip it!
            #(Could get rid of this part by changing cell_ordering so it
            #has our program fill columns at a time instead, but works either way)
            if x > i-1:
                break
            elif(T.get(x,i-1).value):
                pastWord = True
                
        #If there was, we store that
        if pastWord:
            return RespaceTableCell(True, i)
        #Otherwise, we couldn't use this word in the solution. Set false
        else:
            return RespaceTableCell(False, i)

    #The substring was not a word. Do nothing
    else:
        return RespaceTableCell(False, None)
                  
# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    cells_list= []
    for i in range(N+1):
        for j in range(N+1):
            cells_list.append((i,j))
    
    return cells_list

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    #TODO: YOUR CODE HERE
    indexes = []
    for i in table._table:
        for j in i:
            if j.value:
                indexes.append(j.index)

    while 0 in indexes: indexes.remove(0)
    indexes = list(dict.fromkeys(indexes))
            
    indexes.sort()
    for i, index in enumerate(indexes):
        index += i
        s = s[:index] + " " + s[index:]
    print indexes
    return indexes and s

if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    s = "itwasthebestoftimes" #0,2,5,8,12,14
    wordlist = ["of", "it", "the", "best", "times", "was"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print respace_from_table(s, D)
