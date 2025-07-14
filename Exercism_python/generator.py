
'''def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    seat_letters = ['A', 'B', 'C', 'D']
    for i in range(number):
        yield seat_letters[i % 4]  # Use modulo to loop back to A after D'''


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    seat_letters = ['A', 'B', 'C', 'D']
    index = 0

    for i in range(number):
        if index == len(seat_letters):
            index = 0  # reset back to A
        yield seat_letters[index]
        index += 1

#letters = generate_seat_letters(4)
#next(letters)

#Exercise #2
def generate_seats(number):
    seat_letters = ['A', 'B', 'C', 'D']
    index = 0
    row_number = 1
    for _ in range(number):
        if index == len(seat_letters):
            index = 0
            row_number += 1
            if row_number == 13:
                row_number += 1
        yield str(row_number) + seat_letters[index]
        index += 1

'''letters= generate_seats(60)
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))'''

#Exercise 3
def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    return {passenger: next(seats) for passenger in passengers}

#passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']
#assign_seats(passengers)

#exercise 4
def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        #print(seat)
        ticket_number = str(seat) + flight_id
        print(ticket_number)
        total_number = 12 - len(ticket_number)
        print(total_number)
        ticket_code = ticket_number + ("0" * total_number)
        print(ticket_code) 
        yield ticket_code

seat_numbers = ['1A', '17D']
flight_id = 'CO1234'
ticket_ids = generate_codes(seat_numbers, flight_id)
next(ticket_ids)
next(ticket_ids)