if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(query_name)
    #print(student_marks[query_name])
    
    result = 0.0
    for i in range(3):
        result = result + student_marks[query_name][i]
        #print(result)
    result = result/3.0
    print("%.2f" % result)
    
