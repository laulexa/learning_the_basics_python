def get_rounds(number):
    return [number, number + 1, number + 2]
    
    '''my_list = []
    print(type)
    my_number = number
    for new_number in my_number:
        new_number = [new_number, new_number + 1, new_number + 2]
        print(new_number)
        my_list.append(new_number)
    print(my_list)
    return my_list
    
get_rounds([0, 1, 10, 27, 99, 666])'''


def concatenate_rounds(rounds_1, rounds_2):
    #print (rounds_1)
    #print (rounds_2)
    return rounds_1 + rounds_2
concatenate_rounds([27, 28, 29], [35, 36])
#exercise 4
def card_average(hand):
    #print(hand)
    total = sum(hand) / len(hand)
    #print(total)
    return total

card_average([5, 6, 7])

#Exercise 5
def approx_average_is_average(hand):
    #print(hand)
    calculated_average = sum(hand) / len(hand)
    first_number = hand[0]
    #print(first_number)
    last_number = hand[-1]
    #print(last_number)
    case_one = (first_number + last_number) / 2
    #print(case_one)
    case_two = hand[int(len(hand)/2)]
    #print (case_two)
    if case_one == calculated_average or case_two == calculated_average:
        #print("True")
        return True
    return False

approx_average_is_average([1, 2, 3])
approx_average_is_average([1, 2, 3, 5, 9])
#exercise 6
def average_even_is_average_odd(hand):
    even = hand[1::2]
    total_even = sum(even) / len(even)
    #print('even:', even)
    odd = hand[::2]
    #print('odd', odd)
    total_odd = sum(odd) / len(odd)

    if total_even == total_odd:
        #print('true')
        return True
    #print('False')
    return False
average_even_is_average_odd([1, 2, 3])
average_even_is_average_odd([1, 2, 3, 4])

#exercise 7
def maybe_double_last(hand):
    last_card = hand[len(hand)-1]
    if last_card == 11:
        print(last_card)
        hand[len(hand)-1] = last_card * 2
        print (hand)
    return hand
    

maybe_double_last([5, 9, 11])