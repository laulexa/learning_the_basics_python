# Use words.txt as the file name
'''fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    new_line = line.upper().rstrip()
    print(new_line)'''


#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average
# of those values and produce an output as shown below. Do not use the sum() function or a variable named
# sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    new_line = line.rstrip()
    fl_values = float(new_line[19:])
    total = total + fl_values
    print('Average spam confidence:', total)

    #print("Float numbers:", fl_values)
    #print("count:", count)
    #print("Whole line:", new_line)
    #verage_spam =
    #print("Average spam confidence:", average_spam )
final = total / count
print(count)
print('Average spam confidence:', final)
print("Done")

#23