import os

def get_file_strings(path):
    f = open(path, "r")
    strings = f.readlines()
    f.close()
    strings_list = []
    for i in range(len(strings)):
        strings_list.append(strings[i][: -1])
    return strings_list

def get_syllables_set(path):
    f = open(path, "r")
    strings = f.readlines()
    f.close()
    syllables_set = set()
    for i in range(len(strings)):
        syllables_set.add(strings[i][: -1])
    return syllables_set

def normalize(string): #eliminates whitespaces at the begining or at the end of the string
    iB = 0
    while iB < len(string) and string[iB] == ' ':
        iB += 1
    iE = len(string) - 1
    while iE > 0 and string[iE] == ' ':
        iE -= 1
    if iB == len(string):
        return string
    return string[iB : iE + 1]
    
