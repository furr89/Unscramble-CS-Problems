"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

#opens the csv then sets it to reader. then turns it into list
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#getting first index of texts
text_incoming = texts[0][0]
text_answering = texts[0][1]
text_time = texts[0][2]

#getting last index of calls
call_incoming = calls[-1][0]
call_answering = calls[-1][1]
call_time = calls[-1][2]
call_duration = calls[-1][3]

print("First record of texts,", text_incoming, "texts", text_answering, "at time", text_time)
print("Last record of calls,", call_incoming, "calls", call_answering, "at time", call_time, "lasting", call_duration, "seconds")
