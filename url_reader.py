#! /usr/bin/env python3
"""
    Documentation for url operations
"""
#from urllib.request import urlopen
#import sys
from sys import *
import urllib.request as req


def fetch_words(url: str) -> list:
    """
        Documentation for fetch words from URL
    """
    data = req.urlopen(url)
    words: list = []
    for line in data:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            words.append(word)
    data.close()
    return words


def print_items(item: list):
    """
           Documentation for printing words
       """
    for i in item:
        print(i, end=" ")


def main(url: str):
    words: list = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(argv[1])
