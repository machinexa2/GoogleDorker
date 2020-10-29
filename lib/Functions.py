from termcolor import colored

from lib.Globals import Color
from lib.PathFunctions import ender, unstarter

def banner():
    banner = '\x1b[5m\x1b[1m\x1b[40m\x1b[31m   ______                  __        ____             __            \n  / ____/___  ____  ____ _/ /__     / __ \\____  _____/ /_____  _____\n / / __/ __ \\/ __ \\/ __ `/ / _ \\   / / / / __ \\/ ___/ //_/ _ \\/ ___/\n/ /_/ / /_/ / /_/ / /_/ / /  __/  / /_/ / /_/ / /  / ,< /  __/ /    \n\\____/\\____/\\____/\\__, /_/\\___/  /_____/\\____/_/  /_/|_|\\___/_/     \n                 /____/                                             \n\x1b[0m'
    print(banner)
    print(colored("Dork to discover vulnerabilites and secrets!", color='red', attrs=['bold']))

def output_directory_writer(filepath, filename, dork_list: list) -> bool:
    output_file = open(ender(filepath, '/') + unstarter(filepath, '/') + '.google', 'a')
    for dork_line in dork_list:
        output_file.write(dork_line)
    output_file.close()

def output_writer(filename, dork_list: list) -> bool:
    output_file = open(filename, 'a')
    for dork_line in dork_list:
        output_file.write(dork_line)
    output_file.close()

def starter(argv):
    if argv.banner:
        banner()
    if argv.output_directory:
        if not argv.domain:
            print(f'{Color.bad} Output directory provided but not domain!')
    if not argv.wordlist and not argv.domain:
        print('{} Use --help'.format(Color.bad))
        exit()
