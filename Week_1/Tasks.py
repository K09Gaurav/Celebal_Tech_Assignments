"""
Task
The provided code stub reads two integers from STDIN, and

. Add code to print three lines where:

    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)



#---------------------------------------------------------------------------------------------------------------------


"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . 
To read more about this function, Check this out .

You are given a string
. Suppose a character '' occurs consecutively times in the string.
Replace these consecutive occurrences of the character '' with in the string. 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as itt

if __name__ == '__main__':
    for k, c in itt.groupby(input()):
        print(f"({len(list(c))}, {k})", end=' ')

#--------------------------------------------------------------------------------------------------------------------

"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,
.
Both players have to make substrings using the letters of the string

.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string
.
"""

def minion_game(string):
    # your code goes here
    n = len(string)
    k,s = 0,0
    total_comb = (n*(n+1))/2
    for i in range(n):
        if string[i] in "AEIOU":
           k += (n - i) 
    s = int(total_comb - k)
    
    if (k==s):
        print("Draw")
    elif (k>s):
        print("Kevin", k)
    else:
        print("Stuart", s)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)



#--------------------------------------------------------------------------------------------------------------------
"""
In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

"""

def is_leap(year):
    leap = False
    if(year % 4 == 0):
        leap = True
        if (year % 100 == 0 and year % 400 != 0 ):
            leap = False
    
    return leap

year = int(input())
print(is_leap(year))

#--------------------------------------------------------------------------------------------------------------------

"""
You are given a list of lowercase English letters. For a given integer , you can select any indices (assume

-based indexing) with a uniform probability from the list.

Find the probability that at least one of the
indices selected will contain the letter: ''. 
"""

import itertools as it

if __name__ == '__main__':
    n = input()
    letters = input().split()
    k = int(input())
    letters.sort()
    comb = list(it.combinations(letters, k))
    
    no_of_a = 0
    for i in comb:
        if 'a' in i:
            no_of_a += 1
    
    print(no_of_a/len(comb))
    

#--------------------------------------------------------------------------------------------------------------------
"""
Given an integer,n, and space-separated integers as input, create a tuple of those integers. 
Then compute and print the result. 
"""

# DID NOT WORKS WITH PYTHON 3 
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))



#--------------------------------------------------------------------------------------------------------------------

"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal. 
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    ls = list(student_marks[query_name])
    total = sum(ls)
    print(f"{(total/len(ls)):.2f}")



#--------------------------------------------------------------------------------------------------------------------
"""

"""

def print_formatted(number):
    width = len(bin(number)) - 2  
    for i in range(1, number + 1):
        print(str(i).rjust(width), end=" ")
        print(oct(i)[2:].rjust(width), end=" ")
        print(hex(i)[2:].upper().rjust(width), end=" ")
        print(bin(i)[2:].rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)