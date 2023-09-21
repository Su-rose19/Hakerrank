if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
    #print(student)
    lowest_score = min(student, key = lambda x: x[1])
    #print(lowest_score)
    student = [score for score in student if score[1] > lowest_score[1]]
    #print(student)
    second_lowest_score = min(student, key = lambda x: x[1])
    #print(second_lowest_score)
    second_lowest_students = [score for score in student if score[1]==second_lowest_score[1]]
    
    second_lowest_students.sort()
    #print(second_lowest_students)
    
    for student in second_lowest_students:
        print(student[0])
            
    
