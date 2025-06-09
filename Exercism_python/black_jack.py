#non efficient
def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card == 'J' or card == 'Q' or card == 'K' or card == 10:
        card = 10
        #print(type(card))
    elif card == 'A':
        card = 1
    elif card == 2:
        card = 2
    elif card == 3:
        card = 3
    elif card == 4:
        card = 4
    elif card == 5:
        card = 5
    elif card == 6:
        card = 6
    elif card == 7:
        card = 7
    elif card == 8:
        card = 8
    elif card == 9:
        card = 9
    return int(card)
value_of_card(10)

def new_value_of_card(card):
    if card in ['J', 'K', 'Q']:
        return 10
    elif card == 'A':
        return 1
    else: 
        return int(card)

new_value_of_card('K')


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_one in ['J', 'Q', 'K', '10'] and card_two in ['J', 'Q', 'K', '10']:
        print ('equal JQK10')
        return True
    elif card_one == card_two:
        print('equal card')
        return True
    else: 
        print('not equal')
        return False
    
'''can_split_pairs('Q', 'J')
can_split_pairs('1', '2')
can_split_pairs('A', 'A')
can_split_pairs('A', 'J')
can_split_pairs('3', '3')'''

def can_double_down(card_one, card_two):

    if card_one in ['J', 'K', 'Q']:
        card_one = 10
    elif card_one == 'A':
        card_one = 1
    else: 
        card_one = int(card_one)
    
    if card_two in ['J', 'K', 'Q']:
        card_two = 10
    elif card_two == 'A':
        card_two = 1
    else: 
        card_two = int(card_two)

    print('card One: ', card_one)
    print('card Two: ', card_two)

    sum = card_one + card_two
    print (type(card_one))
    print (type(card_two))

    if sum == 9 or sum == 10 or sum == 11:
        print('True')
        return True
    else:
        print('False')
        return False
    
can_double_down('A','J')
can_double_down('A','A')
can_double_down('K','J')
can_double_down('Q','J')
can_double_down('5','4')
can_double_down('3','2')



'''if card == 'J' or card == 'Q' or card == 'K' or card == 10:
        card = 10
    elif card == 'A':
        card = 1
    elif card == 2:
        card = 2
    elif card == 3:
        card = 3
    elif card == 4:
        card = 4
    elif card == 5:
        card = 5
    elif card == 6:
        card = 6
    elif card == 7:
        card = 7
    elif card == 8:
        card = 8
    elif card == 9:
        card = 9
    return int(card)'''