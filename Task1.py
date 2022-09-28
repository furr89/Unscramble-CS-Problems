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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

numbers_list = []

#get all numbers, incoming and answering from calls and saving to a list
for call_num in range(len(calls)):
    numbers_list.append(calls[call_num][0])
    numbers_list.append(calls[call_num][1])

#get all numbers, incoming and answering from texts and saving it to a list
for text_num in range(len(texts)):
    numbers_list.append(texts[text_num][0])
    numbers_list.append(texts[text_num][1])

#and finally print the count (length) on list
numbers_list = list(set(numbers_list))
print("There are", len(numbers_list), "different telephone numbers in the records.")
