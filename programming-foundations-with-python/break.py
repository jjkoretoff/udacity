# the objective of this program was to create a loop that would
# cycle through a given time interval and open a web browser
# once that time interval was finished

# access time library in py
import time

# access webbrowswe library in py
import webbrowser

# assign variables for loop
total_breaks = 3
break_count = 0

# show the user the current time at the beginning of the loop
print("This program started on " + time.ctime())

# run a while loop with a function that uses variables from above
# to set parameters
while(break_count < total_breaks):

    # assign a time in seconds that you want the function to wait 
    time.sleep(10)

    # assign a url that you want to open after sleep time
    webbrowser.open("https://www.youtube.com/watch?v=gq2ZJ418ad8")

    # specifiy how the variables count after each iteration 
    break_count = break_count + 1
