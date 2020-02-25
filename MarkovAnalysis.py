# -*- coding: utf-8 -*-
"""
Markov Analysis
Created on Wed Nov 13 13:55:44 2019

@author: cerya
"""

import string
import random

def process_line(line, book):
    """
    This function takes a string as input and splits the string into a list of
    words. It also removes whitespace and punctuation from each word.
    """
    line = line.replace('-',' ')        #replaces dashes with spaces to
                                        #separate words
    for word in line.split():
        word = word.strip(string.whitespace + string.punctuation)
        word = word.lower()
        book.append(word)               #updates the list

def process_file(filename):
    """
    Takes a file as input and breaks each line into words, removing whitespace
    and punctuation. Also makes all words lower-case. It returns a tuple of
    the words in the file.
    """
    fp = open(filename)                 #opens the file
    book = list()                       #initializes a list
    for line in fp:
        process_line(line, book)
    book = tuple(book)
    return book

def markov_analysis(book, length):
    """
    Takes a tuple as input and outputs a dictionary with keys prefixes (tuples)
    of a given length and values as a list of possible suffixes.
    """
    markov = dict()
    for i in range(len(book)-length-1):
        markov[book[i:i+length]] = list()
    for i in range(len(book)-length-1):
        markov[book[i:i+length]].append(book[i+length])
    return markov
        
def random_text(book, length, words):
    """
    Takes a dictionary as input and outputs a computer-generated text of given
    number of words using Markov analysis with given prefix length to predict 
    the next word in the sequence.
    """
    markov = markov_analysis(book, length)
    paragraph = list()
    n = random.randint(0,len(book)-length-1)
    for i in range(length):
        paragraph.append(book[n+i])
    for i in range(words):
        paragraph.append(random.choice(markov[tuple(paragraph[i:i+length])]))
    return paragraph
    
book = process_file('TheGambler.txt')
print(random_text(book,2,50))



