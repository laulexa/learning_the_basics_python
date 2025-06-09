def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    
    if(tuple(combined_record_group[1]) == combined_record_group[3]):
        combined_coordinates = combined_record_group[3]
        #print(f"{combined_record_group[0]}, {combined_record_group[2]}, {combined_coordinates}, {combined_record_group[4]} ")
        return (f"{combined_record_group[0]}, {combined_record_group[2]}, {combined_coordinates}, {combined_record_group[4]} ")
    #print(f"{combined_record_group[0]}, {combined_record_group[1]}, {combined_record_group[2]}, {combined_record_group[3]}, {combined_record_group[4]} ")
    return (f"{combined_record_group[0]}, {combined_record_group[1]}, {combined_record_group[2]}, {combined_record_group[3]}, {combined_record_group[4]} ")

clean_up(
            (
                ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), 
                ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), 
                ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')
            )
        )

def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    print(record[1])

#get_coordinate(('Scrimshawed Whale Tooth', '2A'))

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    print(tuple(coordinate))
    return 
#convert_coordinate("2A")

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    #tuple(azara_record[1])
    #print(tuple(azara_record[1]))
    print('2', azara_record[1])
    print(rui_record[1])
    if tuple(azara_record[1]) == rui_record[1]:
        print('True')
        return True
    print('false')
    return False

'''compare_records(
    ('Brass Spyglass', '4B'), 
    ('Seaside Cottages', ('1', 'C'), 'blue')
    )'''

#compare_records(
    #('Scrimshawed Whale Tooth', '2A'), 
    #('Deserted Docks', ('2', 'A'), 'Blue')
    #)

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    new_tupla = []
    for element in combined_record_group:
        print (element[3])
        if(tuple(element[1])== element[3]):
            new_tupla.append(element[3])
        
        new_tupla.append(element)
        print('new_t', new_tupla)
    return new_tupla

clean_up(
    ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
    )