##first lesson in udacity introduction to computer science

# quiz 

speed_of_light = 299792458.0 # meters per second
cycles_per_second = 2700000000.0 #2.7 GHz

#distance light travels in one processor cycle
cycle_distance = speed_of_light / cycles_per_second #result in meters

print cycle_distance * 100 #printed result in centimeters

# speed of light stays the same - constant
# upgraded processor
cycles_per_second = 2800000000.0 #2.8 GHz

#distance light travels in one processor cycle
cycle_distance = speed_of_light / cycles_per_second #result in meters

print cycle_distance *100 #printed result in centimeters

## counting down - "=" means assignment

days = 5

while(days > 0):
    
    days = days - 1

print days

## quiz 

hours = 9

hours = hours + 1

hours = hours * 2

print hours # value = 20

## quiz 
# What is the value of secons after running this code?

minutes = 1 #correction made to fix error

minutes = minutes + 1

seconds = minutes * 60

print seconds # value = error - minutes is not defined - correction made above

## quiz 
# Write code that defines "age" in years then prints out the number
# days you have been alive

age = 23

days_in_year = 365.25

days_alive = age * days_in_year

print days_alive

## quiz

name = "John"

print "Hello, " + name + "!" * 3

## quiz - indexing - zero-based - can be anything that evaulates to a number [0 * 21]

print name[0]
print name[3]
print name[-1] #starts from back of string

## quiz

s = "Show me the money" + "!" * 5

print s[3]
print s[1 + 1 + 1] #correct

print s[0]
print (s + s)[0] #correct

print s[0] + s[1]
print s[0 + 1]

print s[1]
print (s + "ity")[1] #wrong because if "s" has less than two characters, result will differ

print s[-1]
print (s + s)[-1] #correct

## quiz

word = "assume"

print word[3]
print word[3:4] #subsetting starts with first number and ends one before las => 3:4 is only one value in string
print word[4:6]
print word[4:]  #selects until end
print word[:2] #select first two -- zero based
print word[:] # entire

## quiz
# print "Udacity" - capitalizing "U" in subset

s = "audacity"

print s[1:].capitalize()

## quiz

s = "Which are always equivalent no matter what s was at the beginning?"

print s[:] #correct
print s + s[0:-1+1] #correct, second is an empty string
print s[0:] #correct
print s[:-1]
print s[:3] + s[3:] #correct

## quiz

pythagoras = "There is geometry in the humming of the strings, there is music in the spacing of the spheres."

print pythagoras.find("string") #returns "40"
print pythagoras[40:46] #checks result
print pythagoras.find("T")
print pythagoras.find("sphere")
print pythagoras[86:]
print pythagoras.find("alegbra") #value not found => returns "-1"

## quiz
# Which evaluates to the value -1

print 'test'.find('t')
print "test".find('st')
print "Test".find('te') #correct
print 'west'.find('test') #correct

## quiz
# which will always have the value 0

s = "any string"

print s.find(s) #correct
print s.find('s') 
print 's'.find('s') #correct
print s.find('') #correct - looking for an empty string no matter what
print s.find(s + '!!!') + 1 #correct

## quiz

danton = "De l'audace, encore de l'audace, toujours de l'audace."
print danton.find('audace')
print danton.find('audace', 0) #1st occurence - found 5
print danton.find('audace', 5) #1st occurence after 5 - found 5
print danton.find('audace', 6) #1st occurence after 6 - found 25
print danton[6:]
print danton[25:]
print danton.find('audace', 25) #1st occurence after 25 - found 25
print danton.find('audace', 26) #1st occurence after 26 - found 47
print danton[47:]
print danton.find('audace', 48) #1st occurence after 48 - found -1 - nothing

## quiz
# which is equivalent to s.find(t, i)
s = 'abcd'
t = 'd'
i = '1'

#s[i:].find(t)
#s.find(t)[:i]
#s[i:].find(t) + i
#s[i:].find(t[i:])
#none of these - correct - 














