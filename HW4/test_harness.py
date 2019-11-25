import multiprocessing
import sys, os

TIMEOUT_SECS = 1  # default timeout for each testcase.

def LoadTestCases(testfile):
    f = open(testfile, 'r')
    testcases = [l.strip().split(";") for l in f.readlines()]
    f.close()
    return testcases

def WrapChecker(run_and_check, queue):
    def WrappedRunAndCheck(testcase):
        outputString = run_and_check(testcase)
        if outputString != "" and outputString != None:
            queue.put(outputString)

    return WrappedRunAndCheck

def RunTestHarness(
    testcases,
    run_and_check,
    max_test_failures,
    print_passed_tests,
    suppress_output,
    timeout_secs=TIMEOUT_SECS
):
    failed_test_counter = 0
    ran_test_counter = 0

    orig_out = sys.stdout
    if suppress_output: sys.stdout = open(os.devnull, 'w')

    output = ""

    for testcase in testcases:
        if max_test_failures > 0 and failed_test_counter >= max_test_failures:
            break
        ran_test_counter += 1
        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=WrapChecker(run_and_check, q), args=(testcase,))

        p.start()
        p.join(timeout=timeout_secs)

        if p.is_alive():
            # p timeouts
            p.terminate()
            output += ("==Test name: %s\n" % testcase[0])
            output += ("\tTimeout\n")
            failed_test_counter += 1
        elif not q.empty():
          failed_test_counter += 1
          output += ("==Test name: %s\n%s\n" % (testcase[0], q.get()))
        elif print_passed_tests:
          output += ("==Test name: %s:\n\tPassed\n" % testcase[0])

    output += ("Ran %d tests, of which %d failed\n" % (ran_test_counter,failed_test_counter))
    sys.stdout = orig_out
    print (output)
