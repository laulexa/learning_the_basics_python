name = input("Enter file:")
if len(name) < 1:
    name = "sample_data.txt"
handle = open(name)

for line in handle:
    line = line.rstrip()
    print(line)