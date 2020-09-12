# GoogleDorker
## Description
Dorks for sensitive stuff from wordlist. Enjoy.

## Features
1. Just feed wordlist and get the result with title and text.
2. Automatically sleeps to bypass google captcha.

## Usage
```
usage: GoogleDorker [-h] [-d DOMAIN] [-w WORDLIST] [-oD OUTPUT_DIRECTORY] [-b]

Google Dorker

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain name
  -w WORDLIST, --wordlist WORDLIST
                        Absolute path to wordlist
  -oD OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        Output directory
  -b, --banner          Print banner and exit

Enjoy hunting bugs
```

## Example
Simple dork
* ```GoogleDorker -w path/to/wordlist.txt -oD `pwd` -t 1 -d anyname.com```  

## Caveats
1. Is terribly slow
