#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.
try:   
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        #print(type(num))
        if num == "done":
            print("done")
            break

        num1 = int(num)
        num = num1
         
        if largest is None:
            largest = num
            #print("here largest" , num)
            
        elif num > largest:
            largest = num
                
        if smallest is None:
            smallest = num
            #print("here smallest", num)

        elif num < smallest:
            smallest = num
            #continue

    print("Minimum is", smallest)
    print("Maximum is", largest)
        #print(num)           
except:
    print('Invalid input')
    print("Maximum is", largest)
    print("Minimum is", smallest)

#
w = len('banana')
print(type(w))

#
text = "X-DSPAM-Confidence:    0.8475"
first_num = text.find('0')
#print(first_num)
num = text[first_num:first_num+6]
print(float(num))