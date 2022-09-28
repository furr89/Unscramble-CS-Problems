"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest_call time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest_call time, <total time> seconds, on the phone during 
September 2016.".
"""

longest_call = {}

#loop through calls and add it to a dictionary
for num in range(len(calls)):
    longest_call.update({calls[num][0]: 0})
    longest_call.update({calls[num][1]: 0})

#go though keys of dictionary, and go though calls
for k in longest_call.keys():
    for c in range(len(calls)):

        #if key equal to index of call, append value of that key
        if (k == calls[c][0]):
            longest_call[k] += int(calls[c][-1])
        if (k == calls[c][1]):
            longest_call[k] += int(calls[c][-1])

#sorting the dictionary by value, which is duration of call
call_li = sorted(longest_call.items(), key = lambda l: l[1])

#getting the last index's caller and duration
phone_num = call_li[-1][0]
duration = call_li[-1][1]

print(phone_num, "spent the longest_call time,", duration, "seconds, on the phone during September 2016.")
