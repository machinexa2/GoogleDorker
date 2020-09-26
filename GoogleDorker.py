#!/usr/bin/python3
from termcolor import colored
from argparse import ArgumentParser

from lib.PathFunctions import PathFunction
from lib.GoogleDork import GoogleDork
from lib.Functions import starter

parser = ArgumentParser(description=colored('Google Dorker', color="yellow"), epilog=colored('Enjoy hunting bugs', color="yellow"))
input_group = parser.add_mutually_exclusive_group()
parser.add_argument('-d', '--domain', type=str, help='Domain name')
parser.add_argument('-w', '--wordlist', type=str, help='Absolute path to wordlist')
input_group.add_argument('-oD', '--output-directory', type=str, help='Output directory')
input_group.add_argument('-o', '--output', type=str, help='Output file')
parser.add_argument('-b', '--banner', action="store_true", help='Print banner and exit')
argv = parser.parse_args()

starter(argv)
dork_object = GoogleDork(argv.domain)
input_wordlist = [line.rstrip('\n') for line in open(argv.wordlist)]

def main():
    for line in input_wordlist:
        result = dork_object.search(line)
        output_writer(result)
if __name__ == "__main__":
    main()
