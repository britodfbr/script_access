# abbrev_example.py
import argparse

my_parser = argparse.ArgumentParser(allow_abbrev=False)   #Abbrev off
my_parser.add_argument('-i', '--input', action='store', type=int, required=True)

args = my_parser.parse_args()

print(args.input)