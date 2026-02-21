def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        print("Fine. Be that way!")
        return "Fine. Be that way!"
    if hey_bob.isupper() == True and hey_bob.endswith('?'):
        print("Calm down, I know what I'm doing!")
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper() == True:
        print("Whoa, chill out!")
        return "Whoa, chill out!"
    if hey_bob.endswith('?') or hey_bob.endswith('?  '):
        print("Sure")
        return "Sure."
    print("Whatever.")
    return "Whatever."

#.isspace()



response("Okay if like my  spacebar  quite a bit?   ")

#Raindrops

def convert(number):
    result = ""
    if number % 3 == 0:
        result = result + "Pling"
        print('Pling')
    if number % 5 == 0: 
        result = result + "Plang"
        print('Plang')
    if number % 7 == 0:
        result = result + "Plong"
        print('Plong')
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0: 
        print(number)
        return str(number)
    print("result",result)
    return result

convert(160)

'''
improved
def raindrop_speak(number):
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    if result == "":
        return str(number)
    return result

or

def raindrop_speak(number):
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    return result if result else str(number)
'''