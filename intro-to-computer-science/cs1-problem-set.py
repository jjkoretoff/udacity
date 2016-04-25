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












