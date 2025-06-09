animal = "Whale"
number = 1
name = "Laura"

#print(name, animal, number)

name = "Camilo"

#print(name, animal, number)
#print(type(name))

def sum (number1, number2):
    total = number1 + number2
    #print(total)

sum(2,3)

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

reactor_efficiency(10, 300, 10000)

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

fail_safe(10, 1099, 10000)