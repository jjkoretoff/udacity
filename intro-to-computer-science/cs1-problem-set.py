#extracting links and problem set

#extracting links from a page
#view source code on page with control + mouse click
#looking for <a href="<url>">

#EXAMPLE OF EXTRACTING WEB PAGE 1ST URL

#page = contents of a web page
#start_link = page.find('<a href =')
#start_quote = page.find('"', start_link)
#end_quote = page.find('"', start_quote + 1)
#url = page[start_quote + 1: end_quote]

## PROBLEM SET
# number of hours in seven weeks
total_weeks = 7 #weeks
week = 7 #days
day = 24 #hours

hours_in_seven_weeks = total_weeks * week * day

print hours_in_seven_weeks

# store distance in meters that light travels in one nanosecond
speed_of_light = 299800000.0 #meters per second
nano_per_sec = 1000000000.0 #one billion

nanodistance = speed_of_light / nano_per_sec

print nanodistance # meters

# write code that prints "udacious"
s = 'udacity'
t = 'bodacious'

print s[:-2] + t[-3:]

# print out position of first occurence if it exists in variable, text
text = "I am hooping with the boys."
print text.find('hoo')

# write code that pulls second occurence of a phrase in a string
text = "all zip files are zipped"

def find_2nd(string, substring):
    return text.find('zip', text.find('zip') + 1)

print find_2nd('zip', 'zip')

# rounding numbers without leaving ".0" at the end

x = 345.341231

x1 = round(x, 0)

print '{0:g}'.format(x1)


# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!


# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

replaced = line.replace(marker, replacement)

print replaced

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

replaced = line.replace(marker, replacement)

print replaced
# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.


# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"

is_palindrome = word.find(word[::-1])

# TESTING
print is_palindrome

# test case 2
word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###

is_palindrome = word.find(word[::-1])

# TESTING
print is_palindrome
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"











