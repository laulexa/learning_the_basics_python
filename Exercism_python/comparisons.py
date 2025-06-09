'''def higher_card(card_one, card_two):

    if card_one in ['J', 'K', 'Q']:
        number_one = 10
    if card_two in ['J', 'K', 'Q']:
        number_two = 10
    
    if card_one == 'A':
        print(card_one)
        number_one = 1
        print(number_one)
        print(type(number_one))
    if card_two == 'A':
        number_two = 1
        print(number_two)
        print(type(number_two))

    if card_one in [2, 3, 4, 5, 6, 7, 8, 9]:
        number_one = card_one
        print(number_one)
        print('type number 1',type(number_one))
        
    if card_two in [2, 3, 4, 5, 6, 7, 8, 9]:
        number_two = card_two
        print(number_two)
        print('type number 2',type(number_two))
    
    return  print(number_one, number_two)

    if(number_one > number_two):
        return print(card_one)
    elif(number_two > number_one):
        return print(card_two)
    elif (number_one == number_two):
        return print(card_one, card_two)
    
higher_card(2, 3)
'''

def higher_card(card_one, card_two):

    # Evaluar el valor de card_one
    if card_one in ['J', 'Q', 'K']:
        value_one = 10
    elif card_one == 'A':
        value_one = 1
    else:
        value_one = int(card_one)

    # Evaluar el valor de card_two
    if card_two in ['J', 'Q', 'K']:
        value_two = 10
    elif card_two == 'A':
        value_two = 1
    else:
        value_two = int(card_two)

    # Comparar y devolver la carta ganadora o ambas si son iguales
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)
    
# Exercise 3

def value_of_ace(card_one, card_two):
    print('card_one: ', card_one)
    print(type(card_one))
    print('card_two: ',card_two)
    print(type(card_two))

    if card_one == 'A' or card_two == 'A':
        new_card_A = 1
        print('A: ', new_card_A)
        return new_card_A
    elif card_one in ['J', 'Q', 'K'] or card_two in ['J', 'Q', 'K']:
        new_card_A = 1
        print('JQK',new_card_A)
        return new_card_A
    elif card_one in ['6','7','8','9'] and  card_two in ['6','7','8','9'] :
        new_card_A = 1
        print('numbers 6 a 9 ', new_card_A)
        return new_card_A
    elif card_one in ['9', '10'] or  card_two in ['9', '10'] :
        new_card_A = 1
        print('numbers 6, 7 y 8', new_card_A)
        return new_card_A
    else:
        new_card_A = 11
        print('Menor que 5: ', new_card_A)
        return new_card_A
    
#print(value_of_ace('8', '2'))
#print(value_of_ace('10', '2'))

#exercise 4

def is_blackjack(card_one, card_two):
    if card_one == 'A' and card_two in ['J', 'Q', 'K', '10']:
        blackjack = True
        print('A and JQK: ', blackjack)
        return blackjack
    elif card_one in ['J', 'Q', 'K', '10'] and card_two == 'A':
        blackjack = True
        print('JQK and A: ', blackjack)
        return blackjack
    else:
        blackjack = False
        print('False: ', blackjack)
        return blackjack
    
is_blackjack('A','J')
is_blackjack('A','Q')
is_blackjack('A','K')  
is_blackjack('J','A')
is_blackjack('J','A')
is_blackjack('J','A')
is_blackjack('J', '2')
is_blackjack('4', 'K')
is_blackjack('Q', '9')
is_blackjack('5', 'A')
    