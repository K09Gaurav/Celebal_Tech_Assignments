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


"""
Q3

"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

"""
Q4
 
"""

def print_rangoli(s):
    # your code goes here
    ab='abcdefghijklmnopqrstuvwxyz'
    mid=((n+(n-1))*2)-1
    rev=[]
    for i in range(s):
        r=''
        k=''
        for j in range(i+1):
            if j==i:
                r+=ab[s-1-j]
                top=r+k[::-1]
                t=top.center(mid,"-")
                rev.append(t)
                print(t)
            else:
                r+=ab[s-1-j]+"-"
                k=r
    for i in range(s-1):
        print(rev[s-2-i])


"""
Q5

"""

def merge_the_tools(string, k):
    # your code goes here
    import textwrap
    
    s = textwrap.wrap(string, k)
    p = ""
    for i in s:
        for j in i:
            if j not in p:
                p+= j
        print(p)
        p=""

"""
Q6

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = input()
sizes = input()
sizes = map(int, sizes.split())
sizes_dict = Counter(sizes)
N = int(input())
total_sale = 0
for i in range(N):
    s, price = tuple(map(int, input().split()))
    if sizes_dict[s] > 0 : 
        total_sale += price
        sizes_dict[s] -= 1 
print(total_sale)

"""
Q7

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)

"""
Q8

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


t = int(input().rstrip())
for i in range(t):
    try:
        re.compile(input().rstrip())
        print(True)
    except re.error:
        print(False)

"""
Q9
"""

n = int(input())
s = set(map(int, input().split()))

d = {"pop":s.pop, "remove":s.remove, "discard": s.discard}
for _ in range(int(input())):
    c = input().split()
    d[c[0]](int(c[1])) if len(c)>1 else d[c[0]]()
print(sum(s))