from aux_functions import *
import re

syllables_2_letters = get_syllables_set("lists/2_letter_syllables.txt")
syllables_3_letters = get_syllables_set("lists/3_letter_syllables.txt")
words = get_file_strings("lists/frequent_words.txt")

numbers = "0123456789"
mayus = "QWERTYUIOPASDFGHJKLZXCVBNM"
minus = "qwertyuiopasdfghjklzxcvbnm"
symbols = "`?:;|<>.,/!@#$%^&*()_~-'+={}[]\ "

def feature_return_one():
    def evaluate(string):
        return 1
    return evaluate

def feature_short_length():
    def evaluate(string):
        if len(string) < 8:
            return -1
        return 0
    return evaluate

def feature_some_mayus():
    def evaluate(string):
        cant = 0
        for i in range(len(string)):
            if string[i].isupper():
                cant += 1
        if cant > len(string) * 0.35 and cant < len(string) - 2:
            return -1
        return 0
    return evaluate

def feature_some_symbols():
    def evaluate(string):
        cant = 0
        for i in range(len(string)):
            if string[i] in symbols:
                cant += 1
        if cant > len(string) / 6:
            return -1
        return 0
    return evaluate

def feature_some_numbers():
    def evaluate(string):
        cant = 0
        for i in range(len(string)):
            if string[i] in numbers:
                cant += 1
        if cant > len(string) / 6:
            return -1
        return 0
    return evaluate

def feature_same_char_multiple_times():
    def evaluate(string):
        chars = [0] * 255
        for i in range(len(string)):
            chars[ord(string[i])] += 1
        for i in range(255):
            if chars[i] > len(string) * 0.24:
                return -1
        return 0
    return evaluate

def feature_some_vocals():
    def evaluate(string):
        cant = 0
        for i in range(len(string)):
            if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
                cant += 1         
        if cant > len(string) / 5:
            return 1
        return 0
    return evaluate

def feature_amount_of_syllables():
    def evaluate(string):
        amount = 0
        i = 0
        while i < len(string) - 1:
            if string[i: i + 2].lower() in syllables_2_letters:
                amount += 2
                i += 2
                if amount >= len(string) / 2:
                    return 1
            else:            
                i += 1
        return 0
    return evaluate

def feature_amount_of_3_letter_syllables():
    def evaluate(string):
        amount = 0
        i = 0
        while i < len(string) - 2:
            if string[i: i + 3].lower() in syllables_3_letters:
                amount += 3
                i += 3
                if amount >= len(string) / 2:
                    return 1
            else:            
                i += 1
        return 0
    return evaluate

def feature_equal_consecutive_chars():
    def evaluate(string):
        aparitions = 1
        last_Char = string[0] 
        for i in range(1, len(string)):
            if string[i] == last_Char:
                aparitions += 1
               	if (aparitions > len(string) * 0.35):
                    return -1
            else:
                last_Char = string[i]
                aparitions = 1 
        return 0
    return evaluate

def feature_less_than_syllables():
    def evaluate(string):
        amount = 0
        i = 0
        while i < len(string) - 1:
            if string[i: i + 2].lower() in syllables_2_letters:
                amount += 1
                i += 2
            else:            
                i += 1
        if amount < 2:
            return -1
        else:
            return 0
    return evaluate

def feature_more_than_syllables():
    def evaluate(string):
        amount = 0
        i = 0
        while i < len(string) - 1:
            if string[i: i + 2].lower() in syllables_2_letters:
                amount += 1
                i += 2
            else:            
                i += 1
        if amount > 2:
            return 1
        else:
            return 0
    return evaluate

def feature_possible_format():
    def evaluate(string):
        pos = string.find('.')
        if pos == -1:
            return 0
        if pos + 3 == len(string) - 1:
            return 1
        if pos + 4 == len(string) - 1:
            return 1
        else:
            return 0
    return evaluate

def feature_all_mayus():
    def evaluate(string):
        cant = 0
        for i in range(len(string)):
            if string[i].isupper():
                cant += 1
        if cant >= len(string) - 2:
            return 1
        return 0
    return evaluate

def feature_matching_brackets():
    def evaluate(string):
        cant = 0
        brackets = 0
        squareBrackets = 0
        found = 0
        for i in range(len(string)):
            if string[i] == '(':
                brackets += 1
                found += 1
            elif string[i] == ')':
                brackets -= 1
                found += 1
            if string[i] == '[':
                squareBrackets += 1
                found += 1
            elif string[i] == ']':
                squareBrackets -= 1
                found += 1
            if(brackets < 0 or squareBrackets < 0):
                return 0
        if found != 0 and (brackets == 0 and squareBrackets == 0):
            return 1
        else:
            return 0
    return evaluate

def feature_mayus_number_symbol():
    def evaluate(string):
        symbolB = 0
        numberB = 0
        mayusB = 0
        for s in string:
            if s in symbols:
                symbolB = 1
            if s in numbers:
                numberB = 1
            if s in mayus:
                mayusB = 1		
        return (symbolB + numberB + mayusB) == 3
    return evaluate

def feature_mayus_number():
    def evaluate(string):
        symbolB = 0
        numberB = 0
        mayusB = 0
        for s in string:
            if s in symbols:
                symbolB = 1
            if s in numbers:
                numberB = 1
            if s in mayus:
                mayusB = 1	
        if symbolB == 0:
            return (numberB + mayusB) == 2
        return 0
    return evaluate

def feature_mayus_symbol():
    def evaluate(string):
        symbolB = 0
        numberB = 0
        mayusB = 0
        for s in string:
            if s in symbols:
                symbolB = 1
            if s in numbers:
                numberB = 1
            if s in mayus:
                mayusB = 1	
        if numberB == 0:	
            return (symbolB + mayusB) == 2
        return 0
    return evaluate

def feature_number_symbol():
    def evaluate(string):
        symbolB = 0
        numberB = 0
        mayusB = 0
        for s in string:
            if s in symbols:
                symbolB = 1
            if s in numbers:
                numberB = 1
            if s in mayus:
                mayusB = 1	
        if mayusB == 0:	
            return (numberB + symbolB) == 2
        return 0
    return evaluate

def feature_consecutive_mayus():
    def evaluate(string):
        max_consecutive_mayus = 0
        cant = 0
        for c in string:
            if c.isupper():
                cant += 1
            else:
                if cant > max_consecutive_mayus:
                    max_consecutive_mayus = cant
                cant = 0
        if max_consecutive_mayus > len(string) * 0.4:
            return 1
        return 0
    return evaluate

def feature_has_word():
    def evaluate(string):
        if len(string) < 200:
            string = string.lower()
            for i in range(len(string)):    
                for j in range(i + 1, len(string) + 1):
                    if string[i: j] in words:
                        return 1
        return 0
    return evaluate

regex_IP_address = re.compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
def feature_contains_ip_address():
    def evaluate(string):
        if len(string) < 300:
            matches = regex_IP_address.findall(string)
            if matches != []:
                return 1
        return 0
    return evaluate

regex_URL = re.compile("(?:http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+(?:[\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(?::[0-9]{1,5})?(\/.*)?")
def feature_contains_URL():
    def evaluate(string):
        if len(string) < 300:
            matches = regex_URL.findall(string)
            if matches != []:
                return 1
        return 0
    return evaluate

regex_alfanumeric = re.compile('^[A-Fa-f0-9]+$')
def feature_is_alfanumeric():
    def evaluate(string):
        matches = regex_alfanumeric.findall(string)
        if matches != []:
            return 1
        return 0
    return evaluate

vocals = "aeiouAEIOU"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYOPSDFGHJKLZXCVBNM"
regex_expression = '['+consonants+']['+vocals+']|['+vocals+']['+consonants+']|['+consonants+']['+vocals+']['+consonants+']|['+vocals+']['+consonants+']['+vocals+']'
first_regex = re.compile('\\b(?:' + regex_expression + ')+\\b')
second_regex = re.compile('\\B(?:' + regex_expression + ')+\\B')
third_regex = re.compile('(?:(?:' + regex_expression + ')+){2,}')

def feature_has_phonetic_pattern():
    def evaluate(string):
        matches = first_regex.findall(string)
        if matches != []:
            for s in matches:
                if len(s) >= 5:
                    return 1
        matches = second_regex.findall(string)
        if matches != []:
            for s in matches:
                if len(s) >= 5:
                    return 1
        matches = third_regex.findall(string)
        if matches != []:
            for s in matches:
                if len(s) >= 5:
                    return 1
        return 0
    return evaluate

def feature_doesnt_have_phonetic_pattern():
    def evaluate(string):
        match = 0
        matches = first_regex.findall(string)
        if matches != []:
            for s in matches:
                if len(s) >= 5:
                    match = 1
        matches = second_regex.findall(string)
        if matches != []:
            for s in matches:
                if len(s) >= 5:
                    match = 1
        matches = third_regex.findall(string)
        if matches != []:
            for s in matches:
                if len(s) >= 5:
                    match = 1
        if match == 1:
            return 0
        return -1
    return evaluate
