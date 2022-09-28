"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = set()
not_telemarketers = set()

#get all numbers that that are not telemarketers
for c in range(len(calls)):
    not_telemarketers.add(calls[c][1])

#also numbers that are not telemarketers
for t in range(len(texts)):
    not_telemarketers.add(texts[t][0])
    not_telemarketers.add(texts[t][1])

#loops through calls and check if the caller is not in the 'not_telemarketers' list
for tel in range(len(calls)):
    if (calls[tel][0] not in not_telemarketers):
        telemarketers.add(calls[tel][0])

#sorts telemarketers list
telemarketers_li = list(telemarketers)
telemarketers_li.sort()

print("These numbers could be telemarketers: ")
for t in telemarketers_li:
    print(t)
