#read a file line by line
'''with open('caperucita.txt','r') as file:
    for lineas in file:
        print(lineas.strip())'''

#read all lines in a list
'''with open('caperucita.txt','r') as file:
    lines = file.readlines()
    print(lines)'''

#add text
'''with open('caperucita.txt','a') as file:
    file.write("\n\nBy:ChatGPT")
'''
#overwrite text
'''with open('caperucita.txt','w') as file:
    file.write("\n\nBy:ChatGPT")'''

#deletes everything and adds the text 

#count lines
with open('caperucita.txt','r') as file:
    lines = file.readlines()
    print(len(lines))