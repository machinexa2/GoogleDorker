from time import sleep
from requests import get 
from bs4 import BeautifulSoup
from termcolor import colored
from random import randint as ri

from lib.Globals import ColorObj

class Engine:
    def __init__(self, domain):
        self.U_A = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        self.MU_A = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
        self.domain = domain

    def search(self, query):
        returner = []
        const_query = str(query + " site:{}".format(self.domain)).replace(' ', '+')
        URL = "https://google.com/search?q={}".format(const_query)
        headers = {"user-agent": self.U_A}
        response = get(URL, headers=headers)
        print("{} Trying this payload after sleeping 7-15s: {}".format(ColorObj.information, colored(URL.split('?')[-1][2:], color='cyan')))
        sleep(ri(7,15))
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            for go_get in soup.find_all('div', class_='r'):
                anchors = go_get.find_all('a')
                if anchors:
                    link = anchors[0]['href']
                    title = go_get.find('h3').text
                    print("{} Obtained {} from dork {}".format(ColorObj.good, colored(title, color='cyan'), colored(query, color='cyan')))
                    returner.append("Title:{}, Link:{}, Dork:{}\n".format(title, link, query))
        else:
            print("{} Sleeping due to error for 30-40s".format(ColorObj.bad))
            sleep(ri(30,40))
        return returner
