# TODO: Nilay Altun, na523
# TODO: Kelly Mayhew, khm53

from helpers import *
from cnf_sat_solver import dpll

# DO NOT CHANGE SAT_solver 
# Convert to Conjunctive Normal Form (CNF)
"""
>>> to_cnf_gadget('~(B | C)')
(~B & ~C)
"""
def to_cnf_gadget(s):
    s = expr(s)
    if isinstance(s, str):
        s = expr(s)
    step1 = parse_iff_implies(s)  # Steps 1
    step2 = deMorgansLaw(step1)  # Step 2
    print (distributiveLaw(step2))
    return distributiveLaw(step2)  # Step 3

# ______________________________________________________________________________
# STEP1: if s has IFF or IMPLIES, parse them

# TODO: depending on whether the operator contains IMPLIES('==>') or IFF('<=>'),
# Change them into equivalent form with only &, |, and ~ as logical operators
# The return value should be an Expression (e.g. ~a | b )

# Hint: you may use the expr() helper function to help you parse a string into an Expr
# you may also use the is_symbol() helper function to determine if you have encountered a propositional symbol
def parse_iff_implies(s):
    # TODO: write your code here, change the return values accordingly
    # first check the "s" has operation or not
    if is_symbol(s.op):
        return s

    # list to keep the track of all the args in s
    transformed_args = []

    # for each arg in s, recursively call the function to get the bottom of it
    for arg in s.args:
        transformed_args.append(parse_iff_implies(arg))

    # after we came to the first expression, check if it contains iff and implies
    if s.op == '<=>':
        left = Expr("==>",transformed_args[0],transformed_args[1])
        right = Expr("==>",transformed_args[1],transformed_args[0])
        final = Expr("&",left,right)

        # if it contains implies we need to call the function again because implies logic is turned to iff after this
        return parse_iff_implies(final)

    elif s.op == '==>':
        not_op = Expr('~', transformed_args[0]) 
        or_op = Expr("|", not_op,transformed_args[1])

        return or_op

    return Expr(s.op, *transformed_args)


# ______________________________________________________________________________
# STEP2: if there is NOT(~), move it inside, change the operations accordingly.


""" Example:
>>> deMorgansLaw(~(A | B))
(~A & ~B)
"""

# TODO: recursively apply deMorgansLaw if you encounter a negation('~')
# The return value should be an Expression (e.g. ~a | b )

# Hint: you may use the associate() helper function to help you flatten the expression
# you may also use the is_symbol() helper function to determine if you have encountered a propositional symbol
def deMorgansLaw(s):
    # TODO: write your code here, change the return values accordingly
    #Base case: expression is just a symbol, no operation
    if is_symbol(s.op):
        return s
    #If the lead operator is ~, time to check if you need to apply DeMorgan's Law!
    elif s.op == '~':
        sub = dissociate('~', [s])[0] #~ is a unary operator, so we know we only have one result
        #Apply DeMorgan differently based on other operator
        bus = dissociate(sub.op, [sub])
        if sub.op == '~':
            sub = bus[0]
            return deMorgansLaw(sub)
        elif sub.op == '|' and len(bus) == 2:  #Assuming (pretty sure) only 2 parts, will need to edit if not the case
            bus[0] = deMorgansLaw(bus[0])
            bus[1] = deMorgansLaw(bus[1])
            return associate('&', [~bus[0], ~bus[1]])
        elif sub.op == '&' and len(bus) == 2:
            bus[0] = deMorgansLaw(bus[0])
            bus[1] = deMorgansLaw(bus[1])
            return associate('|', [~bus[0], ~bus[1]])
        #In this case none apply, probably a symbol but call recursive just in case
        else:
            blah = deMorgansLaw(sub)
            return ~blah
    #Otherwise same as before, return itself with method recursively applied
    else:
        holder = dissociate(s.op, [s])
        for i, each in enumerate(holder):
            holder[i] = deMorgansLaw(each)
        return associate(s.op, holder)
    #Expr(s.op, *args)

# ______________________________________________________________________________
# STEP3: use Distributive Law to distribute and('&') over or('|')


""" Example:
>>> distributiveLaw((A & B) | C)
((A | C) & (B | C))
"""

# TODO: apply distributiveLaw so as to return an equivalent expression in CNF form
# Hint: you may use the associate() helper function to help you flatten the expression
def distributiveLaw(s):
    # TODO: write your code here, change the return values accordingly
    #Base case: expression is just a symbol, no operation
    if is_symbol(s.op):
        return s
    #If starts with |, check if need to distribute (CNF is a bunch of ANDs of ORs, want ORs on inside)
    elif s.op == '|':
        holder = dissociate('|', [s])
        distribs = list()
        for i, each in enumerate(holder):
            #Apply distribution if fits
            if each.op == '&':
                distribs.append(each)
                holder.remove(each)
            #In this case we don't distribute, do same as in other else statement
            else:
                holder[i] = distributiveLaw(each)
        #At this point have two groups:
                #holder has what should be distributed
                #distribs has what should be distributed INTO
        #If distribs empty don't bother
        if len(distribs) == 0:
            return associate('|', holder)
        #Otherwise need to distribute
        for i, each in enumerate(distribs):
            sub = dissociate('&', [each])
            for j, one in enumerate(sub):
                rest = holder.copy()
                rest.append(one)
                sub[j] = associate('|', rest)
            distribs[i] = associate('&', sub)
        return associate('|', distribs)
    #If not check rest of expression recursively (same as the rest)
    #Have to make special case for ~ since it doesn't work with associate
    elif s.op == '~':
        blah = dissociate('~', [s])[0]
        blah = distributiveLaw(blah)
        return ~blah
    else:
        holder = dissociate(s.op, [s])
        for i, each in enumerate(holder):
            holder[i] = distributiveLaw(each)
        return associate(s.op, holder)



# ______________________________________________________________________________

# DO NOT CHANGE SAT_solver 
# Check satisfiability of an arbitrary looking Boolean Expression.
# It returns a satisfying assignment(Non-deterministic, non exhaustive) when it succeeds.
# returns False if the formula is unsatisfiable
# Don't need to care about the heuristic part


""" Example: 
>>> SAT_solver(A |'<=>'| B) == {A: True, B: True}
True
"""

""" unsatisfiable example: 
>>> SAT_solver(A & ~A )
False
"""
def SAT_solver(s, heuristic=no_heuristic):
    return dpll(conjuncts(to_cnf_gadget(s)), prop_symbols(s), {}, heuristic)


if __name__ == "__main__":

# Initialization
    A, B, C, D, E, F = expr('A, B, C, D, E, F')
    P, Q, R = expr('P, Q, R')

# Shows alternative ways to write your expression
    assert SAT_solver(A | '<=>' | B) == {A: True, B: True}
    assert SAT_solver(expr('A <=> B')) == {A: True, B: True}

# Some unsatisfiable examples
    assert SAT_solver(P & ~P) is False
    # The whole expression below is essentially just (A&~A)
    assert SAT_solver((A | B | C) & (A | B | ~C) & (A | ~B | C) & (A | ~B | ~C) & (
        ~A | B | C) & (~A | B | ~C) & (~A | ~B | C) & (~A | ~B | ~C)) is False

# This is the same example in the instructions.
    # Notice that SAT_solver's return value  is *Non-deterministic*, and *Non-exhaustive* when the expression is satisfiable,
    # meaning that it will only return *a* satisfying assignment when it succeeds.
    # If you run the same instruction multiple times, you may see different returns, but they should all be satisfying ones.
    result = SAT_solver((~(P | '==>' | Q)) | (R | '==>' | P))
    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), result)

    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), {P: True})
    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), {Q: False, R: False})
    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), {R: False})

# Some Boolean expressions has unique satisfying solutions
    assert SAT_solver(A & ~B & C & (A | ~D) & (~E | ~D) & (C | ~D) & (~A | ~F) & (E | ~F) & (~D | ~F) &
                      (B | ~C | D) & (A | ~E | F) & (~A | E | D)) == \
        {B: False, C: True, A: True, F: False, D: True, E: False}
    assert SAT_solver(A & B & ~C & D) == {C: False, A: True, D: True, B: True}
    assert SAT_solver((A | (B & C)) | '<=>' | ((A | B) & (A | C))) == {
        C: True, A: True} or {C: True, B: True}
    assert SAT_solver(A & ~B) == {A: True, B: False}

# The order in which the satisfying variable assignments get returned doen't matter.
    assert {A: True, B: False} == {B: False, A: True}
    print("No assertion errors found so far")
