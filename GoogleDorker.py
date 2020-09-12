#!/usr/bin/python3
from argparse import ArgumentParser
from termcolor import colored

from lib.ColoredObject import Color as Cobj
from lib.PathFunctions import PathFunction
from lib.GoogleDork import GoogleDork

def banner():
    from pyfiglet import print_figlet as puff
    puff('Google Dorker', font='larry3d', colors='BLUE')
    print(colored("An automated google dorking tool, just feed wordlist and see the magic!", color='red', attrs=['bold']))

def output_writer(dork_list: list) -> bool:
    output_file = open(str(fpath.slasher(argv.output_directory) + fpath.payloader(argv.domain) + '.google'), 'a')
    for dork_line in dork_list:
        output_file.write(dork_line)
    output_file.close()

parser = ArgumentParser(description=colored('Google Dorker', color="yellow"), epilog=colored('Enjoy hunting bugs', color="yellow"))
parser.add_argument('-d', '--domain', type=str, help='Domain to dork')
parser.add_argument('-w', '--wordlist', type=str, help='Path of wordlist to dork')
parser.add_argument('-oD', '--output-directory', type=str, help='Path to output data (No filename only directory path)')
parser.add_argument('-b', '--banner', action="store_true", help='Print banner and exit')
argv = parser.parse_args()


ColorObject = Cobj()
fpath = PathFunction()
GoogleApp = GoogleDork(argv.domain)
if argv.banner:
    banner()
if not argv.wordlist or not argv.output_directory or not argv.domain:
    print('{} Use --help'.format(ColorObject.bad))
    exit()
input_wordlist = [line.rstrip('\n') for line in open(argv.wordlist)]

def main():
    for line in input_wordlist:
        result = GoogleApp.search(line)
        output_writer(result)
main()
