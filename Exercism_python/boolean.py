#leap year
def leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("Leap Year")
            return True
    print("No Leap Year")
    return False

#leap_year(2015)

#Triangle
def equilateral(sides):
    first_side = sides[0]
    return all(x == first_side and x > 0 for x in sides)

#equilateral([2, 2, 2])
def isosceles(sides):
    #print(len(sides))
    first_side = sides[0]
    second_side = sides[1]
    third_side = sides[2]

    requirement1 = first_side + second_side >= third_side
    requirement2 = second_side + third_side >= first_side
    requirement3 = first_side + third_side >= second_side

    if len(sides) == 3 and requirement1 and requirement2 and requirement3:
        if first_side == second_side or first_side == third_side or second_side == third_side:
            print("Triangle")
            return True
        return False
    print("Not a Triangle")
    return "Not a triangle"


#isosceles([2, 1, 2])
#isosceles([1, 1, 3])

def scalene(sides):
    first_side = sides[0]
    second_side = sides[1]
    third_side = sides[2]

    requirement1 = first_side + second_side >= third_side
    requirement2 = second_side + third_side >= first_side
    requirement3 = first_side + third_side >= second_side

    if len(sides) == 3 and requirement1 and requirement2 and requirement3:
        if first_side != second_side and first_side != third_side and second_side != third_side:
            print("Scalene Triangle")
            return True
        print("Not scalene Triangle")
        return False
    print("Not a Triangle")
    return False

scalene([2,2,2])
scalene([2,1,2])
scalene([2,1,3])
scalene([11,13,31])
scalene([13,11,31])
scalene([31,13,31])