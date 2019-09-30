import diffing
import traceback
import re
from dynamic_programming import DynamicProgramTable

def test_diffing(testcase):
    outputString = ""
    testname, cost_table, s, t, expected_cost = testcase

    # Set up a special cost functor class on this cost table
    class CostFunctor:
        def __init__(self):
            # Cost table arrives as a set of (character, character, cost); read these into a dictionary.
            self.cost_table = {}
            for (a,b,cost) in cost_table:
                self.cost_table[(a,b)] = cost
            self.count = 0
    
        def cost(self, a, b):
            self.count += 1
            assert((a,b) in self.cost_table), "Can't compute cost: no entry in the cost table for (%s, %s)"%(a,b)
            return self.cost_table[(a,b)]

    # Set up the dynamic programming table.
    D = DynamicProgramTable(len(s) + 1, len(t) + 1, diffing.cell_ordering(len(s), len(t)), diffing.fill_cell)

    # Special version of the dynamic-programming fill method with some diffing-specific assertions.
    D.cost_functor = CostFunctor()
    def fill_with_test(D, **kwargs):
        for cell in D._ordering:
            count_before = D.cost_functor.count
            D._table[cell[0]][cell[1]] = D._fill_cell(D, *cell, **kwargs)
            count_after = D.cost_functor.count
            assert(count_after <= count_before + 4), "fill_cell should make at most four calls to cost(). At cell (%d, %d) it made %d."% (cell[0], cell[1], count_after-count_before)
        D.freeze()
    
    try:
        fill_with_test(D, s=s, t=t, cost=D.cost_functor.cost)
    except:
        outputString += "Exception encountered when filling dynamic-programming table:\n"
        outputString += traceback.format_exc()
        return outputString

    pre_count = D.cost_functor.count
    try:
        (cost, align_s, align_t) = diffing.diff_from_table(s,t,D)
    except:
        outputString += "Exception encountered when running diff_from_table:\n"
        outputString += traceback.format_exc()
        return outputString

    post_count = D.cost_functor.count
    if(post_count > pre_count):
        outputString += "diff_from_table called cost; only table-cell-filling code should do that\n"

    if cost != expected_cost:
        outputString += "Diffing code returned a cost of %d, but expected a cost of %d. Returned alignment was\n\t%s\n\t%s\n"%(cost, expected_cost, align_s, align_t)
        return outputString

    #Ensure the alignment is valid.
    if len(align_s) != len(align_t):
      outputString += "align_s and align_t should have the same length, but they differ. Align_s was\n\t%s\nand align_t was\n\t%s\n"%(align_s, align_t)

    align_s_replaced = align_s.replace("-","")
    align_t_replaced = align_t.replace("-","")

    if align_s_replaced != s:
        outputString += "align_s is not the same as s with '-'s added. It was\n\t%s\nbut the input s was\n\t%s\n"%(align_s,s)
    if align_t_replaced != t:
        outputString += "align_t is not the same as t with '-'s added. It was\n\t%s\nbut the input t was\n\t%s\n"%(align_t,t)

    total_cost = 0
    for i in range(len(align_s)):
        if align_s[i] == '-' and align_t[i] == '-':
            outputString += "At position %d, both align_s and align_t were 't'. align_s was\n\t%s\nand align_t was\n\t%s\n"%(i,align_s,align_t)
            return outputString
        total_cost += D.cost_functor.cost(align_s[i],align_t[i])

    if total_cost != cost:
        outputString += "The alignment given by align_s:\n\t%s\nand align_t\n\t%s\nhas cost %d, but diffing code says it has cost %d.\n"%(align_s, align_t, total_cost, cost)

    return outputString

with open("diffing_tests.txt", 'r') as testfile:
    L = testfile.readlines()
    num_tests_run = 0
    for l in L:
        (testname, cost_table, s, t, expected_cost)  = l.strip().split(";")
        expected_cost = int(expected_cost)
        # Parse the cost table
        costs = []
        for i in range(0,len(cost_table),7):
            cost_here = cost_table[i:i+7]
            costs.append((cost_here[1], cost_here[3], int(cost_here[5])))
        testcase = (testname, costs, s,t, expected_cost)
        test_result = test_diffing(testcase)
        num_tests_run += 1
        if len(test_result) > 0:
            print("Failed test with name %s" % testname)
            print(test_result)
            break

print("Ran %d tests"%num_tests_run)
