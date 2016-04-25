# step 1 - read text from a document
# step 2 - check text for curse words

def read_text():
    quotes = open("/Users/johnkoretoff/code/udacity/programming-foundations-with-python/scan-text.rtf")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    
read_text()
    
