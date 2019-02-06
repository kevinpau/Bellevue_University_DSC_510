# File:   DSC510_Assignment_8.py
# Name:   Kevin Paulovici
# Date:   1/27/19
# Course: DSC 510 - Introduction to Programming
# School: Bellevue University
# Desc:   This module is for week 8 programming assignment.

import string

# Function: main
#
# Desc: Function opens a file and passes each line and
#       a dictionary to Process_line.
#       When the file is done reading it will send the
#       dictionary to be printed.
#
# Pre:  The function requires a valid file.
#
# Post: None
def main():
    # define dictionary of words and frq
    word_dict = {}

    with open('Gettysburg.txt') as file_in:
        for line in file_in:
            Process_line(line, word_dict)

    # print out the dict
    Pretty_print(word_dict)


# Function: Add_word
#
# Desc: Function takes a word and dictionary from Process_line.
#       The word is checked if it is in the dictionary. If yes,
#       the count is incremented. If no, the value is added and
#       incremented.
#
# Pre:  The function requires a line from a file.
#
# Post: None
def Add_word(word, word_dict):
    # add words to dictionary
    word_dict[word] = word_dict.get(word, 0) + 1


# Function: Process_line
#
# Desc: Function takes a line read from a file and a dictionary
#       from main. The line is cleaned to remove punctuation and
#       set to lower case. Each word in the line is sent to the
#       Add_word function.
#
# Pre:  The function requires a line from a file.
#
# Post: None
def Process_line(line, word_dict):
    # clean up the line
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    # pass word and dict to be added
    for word in line.split():
        Add_word(word, word_dict)


# Function: Pretty_print
#
# Desc: Functions prints out a dictionary.
#       The dictionary is converted to a list of tuples
#       to be sorted by frequency of use (high to low)
#
# Pre:  The function requires the dictionary to be set.
#
# Post: None
def Pretty_print(word_dict):
    # add dict to list of tuples and sort
    word_list = []
    for key, val in word_dict.items():
        word_list.append((val, key))
    word_list.sort(reverse=True)

    print("Length of dictionary: {}".format(len(word_dict)))
    print('{:15} {}'.format('Word', 'Count'))
    print('-' * 22)

    for item in word_list:
        print('{0[1]:17} {0[0]}'.format(item))

    print(word_list)
main()
