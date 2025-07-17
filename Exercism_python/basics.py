animal = "Whale"
number = 1
name = "Laura"

#print(name, animal, number)

name = "Camilo"

#print(name, animal, number)
#print(type(name))

'''def sum (number1, number2):
    total = number1 + number2'''
    #print(total)

#sum(2,3)

#print(sum(3,3))
#comment

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
   # print(generated_power)
    percentage_value = (generated_power / theoretical_max_power)* 100
   # print(percentage_value)
    if percentage_value > 80:
        efficiency = 'green'
       # print(efficiency)
    elif percentage_value < 80 and percentage_value > 60:
        efficiency = 'orange'
       # print(efficiency)
    elif percentage_value < 60 and percentage_value > 30:
        efficiency = 'red'
       # print(efficiency)
    else:
        efficiency = 'black'
       # print(efficiency)
    return efficiency

#reactor_efficiency(10, 300, 10000)

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    temperature_neutrons = temperature * neutrons_produced_per_second
    print(temperature_neutrons)
    threshold_percentage_one = (threshold * 90)/100
    print(threshold_percentage_one)
    threshold_percentage_two = threshold+ ((threshold * 10)/100)
    print(threshold_percentage_two)
    if temperature_neutrons <= threshold_percentage_one:
        output_status = 'LOW'
        print(output_status)
    elif  temperature_neutrons >= threshold_percentage_one and temperature_neutrons <= threshold_percentage_two:
        output_status = 'NORMAL'
        print(output_status)
    else:
        output_status = 'DANGER'
        print(output_status)
    return output_status

#fail_safe(10, 1099, 10000)

#grains
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 **(number - 1)

def total():
    return 2 ** 64 - 1

'''print(square(1))   # 1
print(square(2))   # 2
print(square(3))   # 4
print(square(64))  # 9223372036854775808

print(total())     # 18446744073709551615'''

# Armstrong_number

def is_armstrong_number(number):
    count = 0
    string_number = str(number)
    sum_of_powers = 0
    for num in string_number:
        count += 1
    total_number = count
    for num in string_number:
        sum_of_powers = sum_of_powers + int(num)**total_number
        print(sum_of_powers)

    print("new n", sum_of_powers)
    print("Count:", count)

    if sum_of_powers == number:
        print("True")
        return True
    else:
        print("False")
        return False

is_armstrong_number(154)

#better solution
def is_armstrong_number2(number2):
    string_number2 = str(number2)
    count1 = len(string_number2)
    sum_of_powers1 = sum(int(digit) ** count1 for digit in string_number2)
    return sum_of_powers1 == number2

is_armstrong_number2(154)