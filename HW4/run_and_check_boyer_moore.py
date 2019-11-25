from boyer_moore import BoyerMooreMajority
from test_harness import RunTestHarness
import traceback

def RunAndCheckBM(testcase):
    outputString = ""
    (test_name, symbols, expected_guess, expected_counter) = testcase
    expected_counter = int(expected_counter)
    if len(symbols) > 0: symbols = symbols.split(",")
    else: symbols = []
    try:
      bmm = BoyerMooreMajority()
    except:
        outputString += "Exception encountered when calling BoyerMooreMajority constructor:\n"
        outputString += traceback.format_exc()
        return outputString
    for (i,s) in enumerate(symbols):
        try:
          bmm.add_next_element(s)
        except:
          outputString += "Exception encountered when calling add_next_element on symbol number %d\n:"%i
          outputString += traceback.format_exc()
          return outputString

    if bmm.counter != expected_counter:
      outputString += "BMM counter not equal to expected counter. bmm.counter was %d, expected was %d. \n"%(bmm.counter, expected_counter)
    
    if expected_counter == 0: return outputString
    if bmm.guess == expected_guess: return outputString
    if bmm.guess == None and expected_guess == '!': return outputString

    guess_formatted = "None" if bmm.guess == None else bmm.guess
    expected_guess_formatted = "None" if expected_guess == '!' else expected_guess
    outputString += "BMM guess not equal to expected guess. bmm.guess was %s, expected was %s."%(guess_formatted, expected_guess_formatted)

    return outputString