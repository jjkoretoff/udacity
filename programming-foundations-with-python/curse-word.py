# step 1 - read text from a document
# step 2 - check text for curse words

import urllib

def read_text():
    quotes = open("/Users/johnkoretoff/code/udacity/programming-foundations-with-python/scan-text.rtf")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    #if "true" in output:
        #print("Profanity Alert!!")
    #elif "false" in output:
        #print("This document is clean!")
    #else:
        #sprint("Could not scan the document properly.")
    
read_text()
    
