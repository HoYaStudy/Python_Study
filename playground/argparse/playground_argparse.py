"""
Playground of argparse module

Tested:
* v3.8.0-amd64
"""
import argparse


# Step 1. Create parser
#
# prog - The name of the program
# usage - The string describing the program usage
# description - Text to display before the argument help
# epilog - Text to display after the argument help
parser = argparse.ArgumentParser(
    description="> Process arguments", usage="playground_argparse [options]", epilog="Bye Bye ~ !!!"
)

# Step 2. Add arguments
#
# action - The basic type of action to be taken when this argument is encountered
#          at the command line.
#   * 'store_true' - It creates default values of False respectively.
#   * 'store_false' - It creates default values of True respectively.
# nargs - The number of command-line arguments that should be consumed.
#   * # : N arguments from the command line will be gathered together into a list.
# choices - A container of the allowable values for the argument.
parser.add_argument("-a", help="A argument")
parser.add_argument("-b", help="B argument", action="store_true")
parser.add_argument("-c", help="C argument", nargs=1, choices=["C1", "C2", "C3"])
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

# Step 3. Parse arguments
args = parser.parse_args()

# Step 4. Process arguments
if args.a:
    print("Option A")
if args.b:
    print("Option B")
if args.verbose:
    print("Option Verbose")
