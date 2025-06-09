def student_ranking(student_scores, student_names):
    print(enumerate(student_names))
    print(enumerate(student_scores))
    
student_ranking (student_scores = [100, 99, 90, 84, 66, 53, 47], student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred'])

def round_scores(student_scores):

    return [round(number) for number in student_scores]
   

round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])



def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    my_list = []
    #rank + '. '+ student_names + ": " + student_scores
    for index, word in enumerate(student_names):
        rank = index + 1
        total = f"{rank}. {word}: {student_scores[index]}"
        my_list.append(total)
        print(my_list)
    return  my_list

#student_ranking([88, 73], ['Paul', 'Ernest'])


'''for student in student_names:
        my_list.append(student)
    print(my_list)'''


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    '''my_second_list = []
    print(student_info[0][1])
    for index, word in enumerate(student_info):
        #print('index', index)
        #print('word', word)
        if(word[0][1] == 100):
            print(my_second_list)
            return my_second_list.append(student_info)
    return my_second_list
    '''
    print(student_info)
    for student in student_info:
        print(student[1])
        if student[1] == 100:
            print(student)
            return student
    return []

perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 0]])

