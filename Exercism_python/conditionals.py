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

