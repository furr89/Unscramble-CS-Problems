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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

callers = []
bangalore_nums = []
answerers = set()

#loop through calls, getting only the callers starting with (080)
for call in range(len(calls)):

  #check if caller is (080) and add it to a list
  if (calls[call][0][0:5] == '(080)'):
    callers.append(calls[call][0])

    #if answerers are from bangalore, save it in another list
    if (calls[call][1][0:5] == '(080)'):
      bangalore_nums.append(calls[call][1])

    #add to list:
    #if answerer is from a fixed line
    if (calls[call][1][0] == '('):

      #finds the last bracket and gets the index
      last_bracket = calls[call][1].find(')')
      answerers.add(calls[call][1][0:last_bracket + 1])

    #if is a mobile number (starts with 7, 8, or 9)
    elif (calls[call][1][0] == '7' or calls[call][1][0] == '8' or calls[call][1][0] == '9'):
      answerers.add(calls[call][1][0:4])
    #if is a telemarketer
    elif (calls[call][1][0:3] == '140'):
      answerers.add(calls[call][1][0:3])

answerer_li = list(answerers)
answerer_li.sort()

print("The numbers called by people in Bangalore have codes:")
for i in answerer_li:
  print(i)

#get percentage of answerers from bangalore in callers and rounds it to 2 places
percentage = len(bangalore_nums) / len(callers) * 100
percentage = round(percentage, 2)
print(percentage, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
