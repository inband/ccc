import difflib
import re
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]


def generate_diff(file1, file2):
    text1 = open(file1).readlines()
    text2 = open(file2).readlines()

    for line in difflib.unified_diff(text1, text2, lineterm=''):
        #print(line, end='')
        print(line, end='')



generate_diff(file1, file2)
