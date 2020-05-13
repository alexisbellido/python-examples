import argparse

"""
Try it like this.

$ python regex.py --needle "tiger" --haystack "I am looking for a tiger in the jungle"
"""

parser = argparse.ArgumentParser()

# parser.add_argument("echo", help="enable echo with this positional parameter")

# arguments are treated as strings, convert to number
# parser.add_argument("number", help="display a square of a given number", type=int)

# optional arguments
parser.add_argument("--needle", help="needle")
parser.add_argument("--haystack", help="haystack")
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")

args = parser.parse_args()

# print(args)
# print(args.echo)
# print(args.number * 2)

# if args.verbosity:
#     print("Be verbose")
# else:
#     print("Don't be verbose")

# print('needle', args.needle)
# print('haystack', args.haystack)
print(f"""Needle: '{args.needle}'. Haystack: '{args.haystack}' """)

