"""
Q1

"""

def solve(s):
    s1 = s.split(' ')
    for i, w in enumerate(s1):
        if w:
            if not w[0].isdigit():
                s1[i] = w.capitalize()
    s = ' '.join(s1)
    
    return s
    

"""
Q2

"""

def average(array):
    # your code goes here
    s = set(array)
    sumd = 0
    tno = 0
    for i in s:
        sumd += i
        tno += 1
    
    return (sumd/tno)
        