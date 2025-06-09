def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    #print(type(express_queue))
    #print(person_name)
    #print(express_queue)
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    
result = add_me_to_the_queue(
    express_queue=["Tony", "Bruce"],
    normal_queue=["RobotGuy", "WW"],
    ticket_type=1,
    person_name="RichieRich"
)

#print(result)  # This will print: ['Tony', 'Bruce', 'RichieRich']

def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """
    
    return queue.count(person_name)

how_many_namefellows(
    queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"],
    person_name="Natasha"
)

def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    queue.pop()
    #print(queue)
    return queue

remove_the_last_person(
    queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]
)

