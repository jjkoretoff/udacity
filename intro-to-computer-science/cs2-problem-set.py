#QUESTION
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

#def udacify(x):
    #return 'U' + x

# Remove the hash, #, from infront of print to test your code.

#print udacify('dacians')
#>>> Udacians

#print udacify('turn')
#>>> Uturn

#print udacify('boat')
#>>> Uboat

#NEXT#
#QUESTION#
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

#def bigger(a,b):
    #if a > b:
        #return a
    #else:
        #return b

#def biggest(a,b,c):
    #return bigger(a,bigger(b,c))

#def median(a, b, c):
    #big = biggest(a, b, c)
    #if big == a:
        #return bigger(b, c)
    #elif big == b:
        #return bigger(a, c)
    #else:
        #return bigger(a, b)

#print(median(1,2,3))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7

#NEXT#
#QUESTION#
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

#def countdown(x):
    #while x > 0:
        #print x
        #x = x - 1
    #print 'Blastoff!'

#countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!


#NEXT#
#QUESTION#
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

#def find_last(search, target):
    #last = -1
    #while True:
        #position = search.find(target, last + 1)
        #if position == -1:
            #return last
        #last = position
    
#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0

#NEXT#
#Question#
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

#def weekend(day):
    #if day == 'Saturday':
        #return True
    #elif day == 'Sunday':
        #return True
    #else:
        #return False
    
#print weekend('Monday')
#>>> False

#print weekend('Saturday')
#>>> True

#print weekend('July')
#>>> False

#NEXT#
#QUESTION#
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps():
    # Your code here


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
