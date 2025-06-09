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