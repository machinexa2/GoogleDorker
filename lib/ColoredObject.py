from termcolor import colored as cat
class Color:
    def __init__(self):
        self.colors = ['information', 'good', 'bad']
        self.information = cat('[!]', color='yellow')
        self.good = cat('[+]', color='green')
        self.bad = cat('[-]', color='red')
    
    def list(self):
        for color in self.colors:
            print('self' + '.' + color + '=' + eval('self' + '.' + color))

