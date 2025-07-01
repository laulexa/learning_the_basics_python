def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagon_id = list(args)
    print(wagon_id)
    return wagon_id
#return list(args) better solution
#get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    a,b,c,*last = each_wagons_id
    d = missing_wagons
    total = c, *d,*last,a,b
    print(list(total))
    return list(total)

#fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])

#Exercise 3
def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # Unpack nested dictionaries if present
    print(route)
    route["stops"] = list(stops.values())
    return route

#add_missing_stops({"from": "New York", "to": "Miami"},
 #                   stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
  #                  stop_4="Jacksonville", stop_5="Orlando")\
                    
#Exercise 4
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    combined_routes = {**route, **more_route_information}
    print(combined_routes)
    return combined_routes

#return {**route, **more_route_information}


#extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"})

#exercise 5

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    cosa = [list(row) for row in zip(*wagons_rows)]
    print(cosa)
    return cosa
        
fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                ])

