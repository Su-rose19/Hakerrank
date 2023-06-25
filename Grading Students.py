#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
# 
#  algorithm#1------
""" 
def gradingStudents(grades):
    # Write your code here
    for i in range(0,len(grades)):
        if (grades[i]<38):
            continue
        elif(grades[i]>=38 and grades[i]<=40):
            grades[i] = 40
        elif(grades[i]>40 and grades[i]<=45 and 45-grades[i]<3):
            grades[i] = 45
        elif(grades[i]>45 and grades[i]<=50 and 50-grades[i]<3):
            grades[i] = 50
        elif(grades[i]>50 and grades[i]<=55 and 55-grades[i]<3):
            grades[i] = 55
        elif(grades[i]>45 and grades[i]<=50 and 50-grades[i]<3):
            grades[i] = 50
        elif(grades[i]>50 and grades[i]<=55 and 55-grades[i]<3):
            grades[i] = 55
        elif(grades[i]>55 and grades[i]<=60 and 60-grades[i]<3):
            grades[i] = 60
        elif(grades[i]>60 and grades[i]<=65 and 65-grades[i]<3):
            grades[i] = 65
        elif(grades[i]>65 and grades[i]<=70 and 70-grades[i]<3):
            grades[i] = 70
        elif(grades[i]>70 and grades[i]<=75 and 75-grades[i]<3):
            grades[i] = 75
        elif(grades[i]>75 and grades[i]<=80 and 80-grades[i]<3):
            grades[i] = 80
        elif(grades[i]>80 and grades[i]<=85 and 85-grades[i]<3):
            grades[i] = 85
        elif(grades[i]>85 and grades[i]<=90 and 90-grades[i]<3):
            grades[i] = 90
        elif(grades[i]>90 and grades[i]<=95 and 95-grades[i]<3):
            grades[i] = 95
        elif(grades[i]>95 and grades[i]<=100 and 100-grades[i]<3):
            grades[i] = 100
        else:
            continue
    return grades
"""
#  algorithm#2------
def gradingStudents(grades):
    # Write your code here
    for i in range(0,len(grades)):
        if (grades[i]<38):
            continue
        else:
            remaider = grades[i] % 5
            subtract = 5 - remaider 
            if (subtract < 3):
                grades[i] = grades[i] + subtract
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
