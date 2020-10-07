from lib.Globals import ColorObj
from lib.PathFunctions import PathFunction

def banner():
    from pyfiglet import print_figlet as puff
    puff('Google Dorker', font='larry3d', colors='BLUE')
    print(colored("An automated google dorking tool, just feed wordlist and see the magic!", color='red', attrs=['bold']))

def output_directory_writer(filepath, filename, dork_list: list) -> bool:
    FPathApp = PathFunction()
    output_file = open(FPathApp.slasher(filepath) + FPathApp.payloader(filepath) + '.google', 'a')
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
            print(f'{ColorObj.bad} Output directory provided but not domain!')
    if not argv.wordlist or not argv.domain:
        print('{} Use --help'.format(ColorObj.bad))
        exit()
