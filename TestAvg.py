##Programmer: Joselyne Guillen
##File Name: TestAvg.py 
##Date: 1/31/21
##Version: 1.6
##Explanation of Program: 
##This program asks the user to enter
##four test scores for 5 students. It
##then calculates the average test grade
##for each student and displays their
##average in the form of a letter grade.

total = 0 ##initialize accumulator 

for students in[1,2,3,4,5]: ##loop to get each student

    print('Enter the test scores for Student ',students)##tells user which student

    for tests in[1,2,3,4]: ##loop to get each test score

        print('Test ',tests)## tells user which test
        t = float(input()) ## gets test score from user
    
        while t < 0 or t > 100: ##input validation- the score has to be between 0 and 100
            print('Enter a score between 0 and 100')

            print('Test ',tests)
            t = float(input())
        

        total+=t ## adds each test score

    avg = total/4 ##gets the average test score

    if avg >= 90 and avg <= 100: ##if the average is between 90 and 100, the student's testing average is an A
        print('--------------------------------------------') ##displays border
        print('Student ',students,' has a test average of A')
        print('--------------------------------------------')
    if avg >= 80 and avg < 90:  ##if the average is between 80 and 89, the student's testing average is a B
        print('--------------------------------------------') 
        print('Student ',students,' has a test average of B')
        print('--------------------------------------------')
    if avg >= 70 and avg < 80: ##if the average is between 70 and 79, the student's testing average is a C
        print('--------------------------------------------')
        print('Student ',students,' has a test average of C')
        print('--------------------------------------------')
    if avg >= 60 and avg < 70: ##if the average is between 60 and 69, the student's testing average is a D
        print('--------------------------------------------')
        print('Student ',students,' has a test average of D')
        print('--------------------------------------------')
    if avg < 60: ##if the average is less than 60, the student's testing average is an F
        print('--------------------------------------------')
        print('Student ',students,' has a test average of F')
        print('--------------------------------------------')

    total = 0 ##resets the accumulator for next student

    

    
