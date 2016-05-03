#code for lesson 2

#web crawler for all links on a page

#def get_next_target(s):
    #start_link = s.find('a<href=')
    #start_quote = s.find('"', start_link)
    #end_quote = s.find('"', start_quote + 1)
    #url = s[start_quote + 1:end_quote]
    #return url, end_quote

#def rest_of_string(s):
    #return s[1:]

#print rest_of_string('audacity')

#PROBLEM#
# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

#def sum(a,b):
    #c = a + b
    #return c

#def square(a):
    #b = a ** 2
    #return B


# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

#print square(5)
#>>> 25    

#NEXT#
#PROBLEM#
# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

#def sum(a,b):
    #return a + b

#def sum3(a, b, c):
    #d = a + b + c
    #return d


#print sum3(1,2,3)
#>>> 6

#print sum3(93,53,70)
#>>> 216

#NEXT#
#PROBLEM#
# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

#def abbaize(a, b):
    #d = a + b + b + a
    #return d

#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'

#NEXT#
#PROBLEM#
# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

#def find_second(search_string, target_string):
    #first = search_string.find(target_string)
    #second = search_string.find(target_string, first +1)
    #return second

#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace')
#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13

#NEXT#
#PROBLEM#
#i = 21
#def absolute(x):
    #if x < 0:
        #x = -x
    #return x

#NEXT#
#PROBLEM#
# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

#def bigger(x, y):
    #if x < y:
        #return y
    #return x

#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3

#NEXT#
#PROBLEM#
# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

#def is_friend(friend):
    #if friend[0] == 'D':
        #return True
    #else:
        #return False
#print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False

#NEXT#
#PROBLEM#
# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

#def is_friend(friend):
    #if friend[0] == 'D':
        #return True
    #elif friend[0] == 'N':
        #return True
    #else:
        #return False

#print is_friend('Diane')
#>>> True

#print is_friend('Ned')
#>>> True

#print is_friend('Moe')
#>>> False

#NEXT#
#PROBLEM#
# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

#def biggest(a, b, c):
    #return max(a, b, c)
#OR

#def biggest(a, b, c):
    #if a > b:
        #if a > c:
            #return a
        #else:
            #return c
    #else:
        #if b > c:
            #return b
        #else: 
            #return c

#OR

#def bigger(a, b):
    #if a > b:
        #return a
    #else:
        #return b

#def biggest(a, b, c):
    #return bigger(bigger(a, b), c)
        
#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9

#NEXT#
#EXAMPLE#

#i = 0
#while i < 10:
    #print i
    #i = i + 1

#NEXT#
#PROBLEM#

#i = 0
#while i != 10:
    #i = i + 1
    #print i
# prints 1 through 10

#NEXT#
#PROBLEM#

#i = 1
#while i != 10:
    #i = i + 2
    #print i
#runs infinitely - it skips 10
#kill a program that runs infinitely by

#NEXT#
#PROBLEM#
# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

#def print_numbers(i):
    #n = i - i 
    #while n < i:
        #n = n +1
        #print n

#OR

#def print_numbers(n):
    #i = 1
    #while i <= n:
        #print i
        #i = i +1

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.


#print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

#NEXT#
#PROBLEM#
# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

#def factorial(n):
    #if (n <= 1):
        #return 1

    #i = 1
    #product = 1
    #while(i <= n):
        #product = product * i
        #i = i + 1

    #return product

#OR

#def #factorial(n):
    #result = 1
    #while n >= 1:
        #result = result * n
        #n = n - 1
    #return result

#print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720

#NEXT#
#PROBLEM#
#this is multiple assignment

#def get_next_target(page):
    #start_link = page.find('<a href=')
    #start_quote = page.find('"', start_link)
    #end_quote = page.find('"', start_quote + 1)
    #url = page[start_quote + 1 : end_quote]
    #return url, end_quote

#url, endpos = get_next_target('this is a <a href="http://udacity.com".link!</a>')
#print url
#print endpos

#test with no link
#url, endpos = get_next_target('good')
#print url
#print endpos

#CONTINUATION TO FIX OUTPUT WITH NO LINK#
#NEXT PORBLEM#
# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

#def get_next_target(page):
    #start_link = page.find('<a href=')

    #if start_link == -1:
        #return None, 0
    
    #start_quote = page.find('"', start_link)
    #end_quote = page.find('"', start_quote + 1)
    #url = page[start_quote + 1 : end_quote]
    #return url, end_quote

#url, endpos = get_next_target('good')
#if url:
    #print "Here!"
#else:
    #print "Not here!"

#test with no link
#url, endpos = get_next_target('good')
#print url
#print endpos

#NEXT#
#PROBLEM#
#def print_all_links(page):
    #while True:
        #url, endpos = get_next_target(page)
        #if url:
            #print url
            #page = page[endpos:]
        #else:
            #break

#print_all_links('this <a href="test1">link 1</a> is a <a href="test2">link 2</a> a <a href="test3"link 3</a>')

#IN CONCLUSION#
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
        
def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
        return None, 0
    
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break

print_all_links(get_page('https://www.eia.gov/petroleum/supply/weekly/'))
