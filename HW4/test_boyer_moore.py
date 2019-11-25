import argparse
import run_and_check_boyer_moore
import os
from test_harness import RunTestHarness, LoadTestCases

BOYER_MOORE_TESTFILE = "testcases_boyer_moore.txt"

def main(args):
    run_and_check = run_and_check_boyer_moore.RunAndCheckBM
    if args.testcase_file == "":
        testcases_filename = BOYER_MOORE_TESTFILE
    else:
        testcases_filename = args.testcase_file

    testcases = LoadTestCases(testcases_filename)
    assert len(testcases) != 0, "Unable to load testcases."

    if args.run_one_test:
        testcases = [t for t in testcases if t[0] == args.run_one_test]
        assert len(testcases) == 1, "Unable to filter to just one test case, please make sure you have the correct unique testcase name."

    RunTestHarness(testcases, run_and_check, max_test_failures=args.max_test_failures, print_passed_tests=args.print_passed_tests, suppress_output=args.suppress_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run test harness')

    parser.add_argument(
        "--testcase_file",
        default = "",
        help = "Choose a testcase file. Defaults to appropriate file depending on the value of --which-test."
    )
    parser.add_argument(
        '--max-test-failures',
        type = int,
        default = 5,
        help='How many failures do you allow until the test stops?'
    )
    parser.add_argument(
        '--run-one-test',
        type = str,
        help= "Which specific one test do you want to run?"
    )
    parser.add_argument(
        '--print_passed_tests',
        type = bool,
        default = True,
        help = "Show output for passed tests",
    )
    parser.add_argument(
        '--suppress_output',
        type = bool,
        default = False,
        help = "Suppress console output when running tests.")

    args = parser.parse_args()
    main(args)
