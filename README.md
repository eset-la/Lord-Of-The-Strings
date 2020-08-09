# Lord Of The Strings (LOTS)

## Strings extraction tool for Linux systems 

This tool is designed to classify the strings extracted from a binary file, printing only the ones that can be considered relevant (i.e. not garbage or false positives). The string extraction process is performed by a call to the Linux command `strings` and then they are classified by the feature-based AI classification algorithm.
The purpose of this tool is to help malware analysts or reverse engineers to accelerate string analysis by removing the irrelevant strings. 

Note that you can add new features and that the weights used for each feature of the AI algorithm can be trained to match your specific needs.

 ## Use
The tool is executed by running the LOTS python script with a file path as the argument:
`python3 LOTS.py 'a_path/a_folder/a_file.extension'`

To print the output into a file:
`python3 LOTS.py 'a_path/a_folder/a_file.extension' >> a_file.txt`
