#!/usr/bin/python3
from termcolor import colored
from argparse import ArgumentParser

from lib.Engine import Engine
from lib.Functions import starter, output_directory_writer, output_writer

parser = ArgumentParser(description=colored('Google Dorker', color="yellow"), epilog=colored('Enjoy hunting bugs', color="yellow"))
output_group = parser.add_mutually_exclusive_group()
parser.add_argument('-d', '--domain', type=str, help='Domain name')
parser.add_argument('-w', '--wordlist', type=str, help='Absolute path to wordlist')
output_group.add_argument('-oD', '--output-directory', type=str, help='Output directory')
output_group.add_argument('-o', '--output', type=str, help='Output file')
parser.add_argument('-b', '--banner', action="store_true", help='Print banner and exit')
argv = parser.parse_args()

starter(argv)
GoEngine = Engine(argv.domain)
input_wordlist = (line.rstrip('\n') for line in open(argv.wordlist) if line)

def main():
    for line in input_wordlist:
        result = GoEngine.search(line)
        if argv.output_directory:
            output_directory_writer(argv.output_directory, argv.domain, result)
        if argv.output:
            output_writer(argv.output, result)

if __name__ == "__main__":
    main()
