import argparse
import re

"""
Try it like this.

$ python3 regex.py --needle "tiger" --haystack "I am looking for a tiger in the jungle"
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

str = 'an example word:cat!!'
# use raw string for pattern
# it’s highly recommended that you use raw strings for all but the simplest expressions
# match = re.search(r'word:\w\w\w', str)
match = re.search(r'\S\S\s\S', str)
# If-statement after search() tests if it succeeded
if match:
    print(f'found: [{match.group()}]')
else:
    print('did not find')

match = re.search(args.needle, args.haystack)
if match:
    print(match.group())

match = re.search(r'^p[i]{0,1}', 'piig')
if match:
    print(match.group())

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print('---')
    print(match.group())
# group match test with parentheses
# A common workflow with regular expressions is that
# you write a pattern for the thing you are looking for, adding
# parenthesis groups to extract the parts you want.
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print('---')
    print(match.group())
    print(match.group(1))
    print(match.group(2))

# Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher TEST@example.com'
# Here re.findall() returns a list of all the found email strings
# Using \. instead of . inside brackets. Backslash inhibits the specialness of a
# character and can be used safely if in doubt
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
print('---')
for email in emails:
    print(email)

# using parentheses to grout matching text will return list of tuples
# tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
# pattern with a-z looks for lowercase characters but re.IGNORECASE flag will find TEST@example.com
tuples = re.findall(r'([a-z\.-]+)@([\w\.-]+)', str, re.IGNORECASE)
print('---')
print(tuples) ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0], tuple[1])  ## username, host

str = '<b>foo</b> and <em>important</em> and <i>so on</i>'
print('--- greedy')
# greedy by default so it will go until the closing at the end of the string,
# the .* goes as far as is it can, instead of stopping at the first >
tags = re.findall(r'(<.*>)', str)
print(tags)
# make it non greedy with .*?
print('--- non greedy')
tags = re.findall(r'(<.*?>)', str)
print(tags)

print('--- substitute')
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub returns a new string with all replacements
# If - is escaped (e.g. [a\-z]) or if it’s placed as
# the first or last character (e.g. [-a] or [a-]), it will match a literal '-'.
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))

# from https://docs.python.org/3/library/re.html
str = 'aaa aaa bbb aaa'
tuples = re.findall(r'(a{3})', str)
print('-----')
print(tuples)

# str = 'superman is good'
# str = 'spiderman is okay'
str = 'but batman is the best'
# match = re.search(r'(superman|batman).*', str)
# match = re.search(r'\W(.*man).*', str)
match = re.search(r'\W(?P<name>.*man).*', str)
print('-----')
if match:
    # defaults to zero
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    try:
        print(match.group('name'))
    except IndexError:
        pass
else:
    print('nothing to say about that hero')

print('-----')
pattern = re.compile('(dog|cat)')
animals = ['dog', 'eagle', 'horse', 'cat']
for animal in animals:
    str = f'my black {animal}'
    print(str)
    match = pattern.search(str)
    if match:
        print('good:', match.group(1))


