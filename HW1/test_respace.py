import respacing
import traceback
from dynamic_programming import DynamicProgramTable

def test_respace(testcase):
    outputString = ""
    testname, wordlist, string, expected_respace = testcase

    # Set up a special dictionary class on this wordlist
    class Dictionary:
        def __init__(self):
            self.words = set(wordlist)
            self.count = 0
    
        def is_word(self, w):
            self.count += 1
            return w in self.words

    # Set up the dynamic programming table.
    D = DynamicProgramTable(len(string) + 1, len(string) + 1, respacing.cell_ordering(len(string)), respacing.fill_cell)

    # Special version of the dynamic-programming fill method with some respacing-specific assertions.
    D.dictionary = Dictionary()
    def fill_with_test(D, **kwargs):
        for cell in D._ordering:
            count_before = D.dictionary.count
            D._table[cell[0]][cell[1]] = D._fill_cell(D, *cell, **kwargs)
            count_after = D.dictionary.count
            assert(count_after <= count_before + 1), "fill_cell should make at most one call to is_word. At cell (%d, %d) it made %d."% (cell[0], cell[1], count_after-count_before)
        D.freeze()
    
    try:
        fill_with_test(D, string=string, is_word=D.dictionary.is_word)
    except:
        outputString += "Exception encountered when filling dynamic-programming table:\n"
        outputString += traceback.format_exc()
        return outputString

    pre_count = D.dictionary.count
    try:
        respaced = respacing.respace_from_table(string, D)
    except:
        outputString += "Exception encountered when running respace_from_table:\n"
        outputString += traceback.format_exc()
        return outputString

    post_count = D.dictionary.count
    if(post_count > pre_count):
        outputString += "respace_from_table called is_word; only table-cell-filling code should do that\n"

    if respaced == None and len(expected_respace) > 0:
        outputString += "Respacing code returned None, but expected a respacing like:\n\t%s\nFor input string:\n\t%s\nAnd wordlist:\n\t%s\n"%(expected_respace, string,str(wordlist))
        return outputString

    if respaced == None: return outputString

    # Here, respaced is not None. Ensure it is a valid respacing.
    words = respaced.split(" ")
    if "".join(words) != string:
        outputString += "Respacing code returned this respacing:\n\t%s\nWhich is not a respacing of the input:\n\t%s\n"%(respaced, string)

    for (i,w) in enumerate(words):
        if w not in wordlist:
            outputString += "Respacing code returned this respacing:\n\t%s\nWhich has as word number %d:\n\t%s\nwhich was not in the wordlist:\n\t%s\n"%(respaced,i,w,str(wordlist))

    return outputString

with open("respace_tests.txt", 'r') as testfile:
    L = testfile.readlines()
    num_tests_run = 0
    for l in L:
        values = l.strip().split(";")
        testname = values[0]
        wordlist = values[1]
        string = values[2]
        expected_respace = values[3]
        wordlist = wordlist.split(",")
        testcase = (testname, wordlist, string, expected_respace)
        test_result = test_respace(testcase)
        num_tests_run += 1
        if len(test_result) > 0:
            print("Failed test with name %s" % testname)
            print(test_result)
            break

print("Ran %d tests"%num_tests_run)
