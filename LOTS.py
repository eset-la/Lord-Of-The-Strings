#########################################################################################
#                                                                                       #
#                                ~ Lord Of The Strings ~                                #
#                                         (LOTS)                                        #
#                                   ESET Latinoamerica                                  #
#                       Author: Daniel N. Kundro, Malware Researcher                    #
#                                                                                       #
#########################################################################################

import sys
sys.path.insert(0, './code')
from classifier import Classifier
from features import *
from subprocess import run
import random
import os
import tempfile

if len(sys.argv) != 2:
    print("Invalid argument, use -h to see usage instructions")
    sys.exit()
if sys.argv[1][0] == "-":
	if sys.argv[1] == "-h":
	    print("Use: ")
	    print("    LOTS.py <path>")
	    print("    Example: \"python3 LOTS.py '/a_folder/a_file.extension'\"")
	    sys.exit()
	else:
	    print("Invalid argument, use -h to see usage instructions")
	    sys.exit()

input_file = ""
if not os.path.isfile(sys.argv[1]):
    print("Invalid argument: File doesnt exist")
    sys.exit()

input_file = sys.argv[1]
tmp_file_path = tempfile.NamedTemporaryFile().name

# extracts the strings of the file using the strings command
os.system("strings " + input_file + " >> " + tmp_file_path)

# initialization of features to be used
features = [
	feature_some_mayus(), 
	feature_short_length(), 
	feature_some_symbols(), 
	feature_some_numbers(), 
	feature_same_char_multiple_times(), 
	feature_some_vocals(), 
	feature_amount_of_syllables(), 
	feature_less_than_syllables(), 
	feature_equal_consecutive_chars(), 
	feature_more_than_syllables(), 
	feature_possible_format(),
	feature_all_mayus(), 
	feature_matching_brackets(), 
	feature_mayus_number_symbol(),
	feature_mayus_number(), 
	feature_mayus_symbol(), 
	feature_number_symbol(), 
	feature_consecutive_mayus(), 
	feature_amount_of_3_letter_syllables(), 
	feature_has_word(), 
	feature_has_phonetic_pattern(),
	feature_doesnt_have_phonetic_pattern(), 
	feature_contains_ip_address(), 
	feature_contains_URL(), 
	feature_is_alfanumeric(), 
	feature_return_one()
	]

# weight of each feature
weights = [0.5830878526085327, 0.8167982800840952, 0.3031047660898954, 0.3511025100953228, 0.08460372684249068, 0.0363302151126953, 0.49587266527259477, -0.009270349058004501, 0.5216758594802852, 1, 0.8797926196893331, 0.17716305217302822, 0.31185985998822036, -0.300290355587177, -0.11932957590453366, -0.4276757164508339, -0.47858112684824683, -0.011643302695850843, -0.09211047787285304, 0.9789467719911682, 0.09540640163658995, -0.21767492536516123, 1, 0.5960137905622195, 0.35667642091833507, -0.017654033234247662]

# classifier initialization
classifier = Classifier(features, weights)

# extracted strings classification
for s in get_file_strings(tmp_file_path):
    string = normalize(s)
    if classifier.is_relevant(string):
        print(string) # prints just the relevant strings

os.remove(tmp_file_path)
sys.exit()
