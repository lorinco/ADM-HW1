#!/usr/bin/env python
# coding: utf-8

# # Introduction

# In[ ]:


#1) 'Say hello with Python'

print("Hello, World!")


# In[ ]:


#2) 'Python if-else'

#!/bin/python3


if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 0:
        if n>= 2 and n<=5:
            print('Not Weird')
        if n >= 6 and n <= 20:
            print('Weird')
        if n > 20:
            print('Not Weird') 
    else:
        print('Weird')       
        


# In[ ]:


#3) 'arithmetic operators'

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)


# In[ ]:


#4) 'Python: division'

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)


# In[ ]:


#5) 'Loops'

if __name__ == '__main__':
    n = int(input())
i=0
while i<n:
    print(i**2)
    i+=1


# In[ ]:


#6) 'Write a function'

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 100 ==0 and  year % 400 != 0:
        return False
    if year % 4 == 0:
        return True
    
    return leap

year = int(input())
print(is_leap(year))


# In[2]:


#7)'Print function'

if __name__ == '__main__':
    n = int(input())
a=''
for i in range(1,n+1):
    a=a+str(i)
print(a)


# # Data types

# In[ ]:


#1) 'Lists'

if __name__ == '__main__':
    l=[]
    n = int(input())
    for i in range(n):
        comando = input().split()
        if comando[0] == 'insert':
            l.insert(int(comando[1]),int(comando[2]))
        elif comando[0] == 'remove':
            l.remove(int(comando[1]))
            
        elif comando[0] == 'append':
            l.append(int(comando[1]))
        elif comando[0] == 'sort':
            l.sort()
        elif comando[0] == 'pop':
            l.pop()
        elif comando[0] == 'reverse':
            l.reverse()
        elif comando[0] == 'print':
            print(l)


# In[ ]:


#2) 'List Comprehensions'

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
a=[]
b=[]
for i in range(x+1):
     for j in range(y+1):
         for k in range(z+1):
             if i+j+k !=n:
                a=[i,j,k]
                b.append(a)
print(b)


# In[ ]:


#3) 'find the runner-up score!'

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
   
a=[]
for i in arr:
    if i != max(arr):
        a.append(i)
print(max(a))


# In[ ]:


#4) 'Nested Lists'

if __name__ == '__main__':
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        b.append(score)
    i=0
    while i<len(a):
        if b[i]!=min(b):
            c.append(a[i])
            d.append(b[i])
        i+=1
    i=0
    while i<len(c):
        if d[i]==min(d):
            e.append(c[i])
        i+=1
    e.sort()
   # print(e)
    print("\n".join(e))
 


# In[ ]:




#5) 'Finding the percentage'

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
 name, *line = input().split()
 scores = list(map(float, line))
 student_marks[name] = scores
    query_name = input()
a=student_marks[query_name]
print(format((sum(a)/len(a)),'.2f'))


# In[ ]:


#6) 'Tuples'
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
hashed_tuple = tuple(integer_list)
print(hashed_tuple)


# # Strings

# In[ ]:


#1) 'sWAP cASE'

def swap_case(s):
    a=[]
    for i in s:
        if i.isalpha()==True:
            if i == i.lower():
                a.append(i.upper())
            if i == i.upper():
                a.append(i.lower())
        else:
            a.append(i)
                
    a=''.join(a)
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:


#2) 'String Split and Join'

def split_and_join(line):
    a=line.split(" ")
    a="-".join(a)
    return a
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:


#3) 'What's your name?'

# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello "+ first +" "+last+"! You just delved into python.")
    # Write your code here

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


#4) 'Mutations'

def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


#5) 'Find a string'

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


#6) 'String Validators'

if __name__ == '__main__':
    s = input()
    n=False
    a=False
    b=False
    c=False
    d=False
    for i in range(len(s)):
        if s[i].isalnum()==True:
            n=True
        if s[i].isalpha()==True:
            a=True
        if s[i].isdigit()==True:
            b=True
        if s[i].islower()==True:
            c=True
        if s[i].isupper()==True:
            d=True
                   
    print(n)
    print(a)
    print(b)
    print(c)
    print(d)


# In[6]:


#7) 'Text Alignment'

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

    print_hackerrank_logo(thickness)


# In[ ]:


#8) 'Text Wrap'

def wrap(string, max_width):
    return "\n".join(string[i:i + max_width] for i in range(0, len(string), max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[46]:


# 9) 'Designer Door Mat'

if __name__ == '__main__':
    n,m=map(int, input().split())
    for i in range(n):
        if i%2!=0:
            print(('.|.'*i).center(m,'-'))
    print('WELCOME'.center(m,'-'))
    for i in range(n-1,0,-1):
        if i%2!=0:
            print(('.|.'*i).center(m,'-'))


# In[69]:


# 10) 'String Formatting'
def print_formatted(number):
    spaces=len(bin(number)[2:])
    for i in range(number):
        a=i+1
        b=oct(i+1)[2:]
        c=(str(hex(i+1)[2:])).upper()
        d=bin(i+1)[2:]
        a=((spaces-len(str(a)))*' '+str(a))
        b=((spaces-len(str(b)))*' '+str(b))
        c=((spaces-len(str(c)))*' '+str(c))
        d=((spaces-len(str(d)))*' '+str(d))
        print(a,b,c,d)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[ ]:


#11) 'Alphabet Rangoli'


# In[ ]:


#12) 'Capitalize!'

def solve(s):
    l=re.split(r'(\s+)', s)
    stringa=""
    for i in range(len(l)):
        l[i] = l[i].capitalize()
    x="".join(l)
    return x.strip()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


#13) 'The minion game'


# In[ ]:


#14) ' Merge the Tools!'


# In[ ]:





# # SETS

# In[ ]:


#1) 'Introduction to sets'

def average(array):
    x=sum(set(array))/len(set(array))
    return round(x,3)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[ ]:


#2) 'Symmetric difference'
if __name__=="__main__":
    M=int(input())
    Mu=set(input().split())
    N=int(input())
    Nu=set(input().split())
    m=Mu.difference(Nu)
    n=Nu.difference(Mu)
    c=n.union(m)
    c=list(map(int,c))
    c.sort()
    for _ in range(0,len(c)):
        print(c[_])


# In[ ]:


#3) 'Set.add()'

n=int(input())
m=[input() for i in range(0,n)]
m=set(m)
print(len(m))


# In[ ]:


#4) 'Set .discard(), .remove() & .pop()'

n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(0,m):
    z=input().split()
    if z[0]=='pop':
        s.pop()
    elif z[0]=='remove':
        s.remove(int(z[1]))
    elif z[0]=='discard':
        s.discard(int(z[1]))
print(sum(s))


# In[ ]:


#5) 'Set .union() Operation'

n=input()
m=set(input().split())
a=input()
b=set(input().split())
print(len(m.union(b)))


# In[ ]:


#6) 'Set .intersection() Operation'

n=input()
m=set(input().split())
a=input()
b=set(input().split())
print(len(m.intersection(b)))


# In[ ]:


#7) 'Set .difference() Operation'

n=input()
m=set(input().split())
a=input()
b=set(input().split())
print(len(m.difference(b)))


# In[ ]:


#8) 'Set .symmetric_difference() Operation'

n=int(input())
m=set(map(int,input().split()))
a=int(input())
b=set(map(int,input().split()))
print(len(m.symmetric_difference(b)))


# In[ ]:


#9) 'Set Mutations'

n=int(input())
m=set(map(int,input().split()))
N=int(input())
for i in range(0,N):
    mutazioni=input().split()
    mutazione=mutazioni[0]
    B=set(map(int,input().split()))
    if mutazione=="update":
        m.update(B)
    elif mutazione=="difference_update":
        m.difference_update(B)
    elif mutazione=="intersection_update":
        m.intersection_update(B)
    elif mutazione=="symmetric_difference_update":
        m.symmetric_difference_update(B)
    
print(sum(m))


# In[ ]:


#10)'The Captain's Room'

from collections import Counter
n=int(input())
x=input().split()
Contatore=Counter()
for i in range(0,len(x)):
    Contatore[x[i]]+=1
for i in Contatore.keys():
    if Contatore[i] != n :
        print(i)


# In[ ]:


#11) 'Check Subset'

x=input()
for i in range(0,x):
    a=input()
    A=set(map(int,input().split()))
    b=input()
    B=set(map(int,input().split()))
    if A==A.intersection(B):
        print(True)
    else:
        print(False)
    


# In[ ]:


#12) 'Check Strict Superset'

a=set(map(int,input().split()))

n=int(input())

booleano=True
for i in range(0,n):
    B=set(map(int,input().split()))
    if B==a.intersection(B) and len(B) < len(a):
        continue
    booleano=False
print(booleano)


# In[ ]:


#13) 'No Idea'

nm=list(map(int,input().split()))
arr=list(map(int,input().split()))
a=tuple(map(int,input().split()))
b=tuple(map(int,input().split()))
z=0
from collections import Counter


c=Counter(arr)
a=Counter(a)
b=Counter(b)
for i in c.keys():
    if i in a.keys():
        z+=c[i]
    if i in b.keys():
        z-=c[i]
print(z)


# In[ ]:





# # COLLECTIONS

# In[ ]:


#1) collections.Counter()

from collections import Counter
x= int(input())
misure = list(map(int,input().split()))

n= int(input())
profit=0
for i in range(0,n):
    countermisure=Counter(misure)
    desiredss=list(map(int,input().split()))
    if desiredss[0] in countermisure.keys():
        misure.remove(desiredss[0])
        profit += desiredss[1]
print(profit)


# In[ ]:


#2)DefaultDict Tutorial

from collections import defaultdict,Counter
diz=list(map(int,input().split()))
n=diz[0]
m=diz[1]
A=defaultdict(list)
for i in range(0,n):
    x=input()
    A[x].append(str(i+1))
for b in range(0,m):
    y=input()
    if y in A:
        print(" ".join(A[y]))
    else:
        print("-1") 


# In[ ]:


#3)Collections.namedtuple()
from collections import namedtuple
n=int(input())

x=namedtuple('x',input().split())



y= [int(x(*input().split()).MARKS) for i in range(n)]

print(sum(y)/n)


# In[ ]:


#4)Collections.OrderedDict()

from collections import OrderedDict,Counter
n=int(input())
od=OrderedDict()
l=[]

profit=0
for i in range(0,n):
    x=list(map(str,input().split()))
    item_name=x[:-1]
    net_price=x[-1]
    l.append(' '.join(item_name))
    od[str(' '.join(item_name))]=int(net_price)

cd=Counter(l)  
for i in od.keys():
    print(i,cd[i]*od[i])


# In[ ]:


#5)Word Order

from collections import OrderedDict,Counter
n=int(input())
l=[]
od=OrderedDict()
for i in range(0,n):
    word=str(input())
    l.append(word)
    od[word]=i
cd=Counter(l)
print(len(od))
print(' '.join([str(i) for i in cd.values()]))


# In[ ]:


#6)Collections.deque()

from collections import deque
n=int(input())
d=deque()
for i in range(0,n):
    comandi=input().split()
    c=comandi[0].strip()
    if c=="append":
        d.append(int(comandi[1]))
    elif c=="appendleft":
        d.appendleft(int(comandi[1]))
    elif c=="pop":
        d.pop()
    elif c=="popleft":
        d.popleft()
    elif c=="remove":
        d.remove(int(comandi[1]))
    elif c=="reverse":
        d.reverse()
    elif c=="rotate":
        d.rotate(int(comandi[1]))
    elif c=="extend":
        d.extend(int(comandi[1]))
for i in d:
    print(i,end=" ")


# In[ ]:


#7)Company Logo


from collections import Counter


if __name__ == '__main__':
    s = input()
    cont=Counter()
    x=list(s)
    x.sort()
    x="".join(x)
    
    for i in range(0,len(x)):
        cont[x[i]] +=1
    e=cont.most_common(3)
    for i in range(len(e)):
        print(e[i][0],e[i][1])


# In[ ]:


#8)Piling Up!

from collections import deque
T=int(input())
for i in range(0,T):
    n=int(input())
    b=list(map(int,input().split()))
    d=deque()
    d.extend(b)
    l=[]
    for i in range(0,len(d)):
        if d[0]>=d[-1]:
            l.append(d[0])
            d.popleft()
        elif d[-1]> d[0]:
            l.append(d[-1])
            d.pop()
    b.sort(reverse=True)
    if b==l:
        print("Yes")
    else:
        print("No")


# # DATE AND TIME

# In[ ]:


#1) Calendar Module

import calendar

mm,dd,yyyy = input().split()

print(calendar.day_name[calendar.weekday(int(yyyy), int(mm), int(dd))].upper())


# In[ ]:


#2) Time delta

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    t1=datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2=datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta=t1-t2
    d=delta.total_seconds()
    d=abs(round(int(d),0))
    return str(d)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# # EXCEPTIONS

# In[ ]:


#1) Exceptions

T=int(input())
for i in range(0,T):
    try:
        n=list(map(int,input().split()))
    except ValueError as e:
        print("Error Code:",e)
        continue
    try:
        divisione=n[0]//n[1]
        print(divisione)
    except ZeroDivisionError as e:
        print("Error Code:",e)


# # BUILTINS

# In[ ]:


#1) Zipped!

inp=list(map(int,input().split()))
N=inp[0]
X=inp[1]
l=[]
for i in range(0,X):
    a=list(map(float,input().split()))
    l.append(a)
m=list(zip(*l))
for i in range(0,len(m)):
    avg=sum(m[i])/X
    print(round(avg,1))


# In[ ]:


#2) ginortS

s= str(input())
l,u,e,o=[],[],[],[]
for i in range(0,len(s)):
    if s[i].isupper()==True:
        u.append(s[i])
    elif s[i].islower()==True:
        l.append(s[i])
    else:
        n=int(s[i])
        if n % 2 == 0:
            e.append(str(n))
        else:
            o.append(str(n))
            
            
l.sort()
u.sort()
e.sort()
o.sort()
l.extend(u)
l.extend(o)
l.extend(e)
result="".join(l)
print(result)


# In[ ]:


#3) Athlete Sort

import math
import os
import random
import re
import sys
from collections import defaultdict


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

k = int(input())
d=defaultdict(list)
for i in range(0,len(arr)):
    c=str(arr[i][k])
    d[c].append(arr[i])
ci=list(map(int,list(d.keys())))
ci.sort()

for i in range(0,len(ci)):
    e=d[str(ci[i])]
    if len(e) >1 :
        for j in range(0,len(e)):
            ej=list(map(str,e[j]))
            print(" ".join(ej))
    else :
        ej=list(map(str,e[0]))
        print(" ".join(ej))


# # PYTHON FUNCTIONALS

# In[ ]:


# 1) Map and Lambda functions

cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        n = fib[i-1] + fib[i-2]
        fib.append(n)
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# In[ ]:





# # REGEX AND PARSING CHALLENGES

# In[ ]:


#1)Detect Floating Point Number
import re

pattern = r'^(?:-\d+|\+?\d*)\.\d+$'
t= int(input())
for i in range(0,t):
    
    n=str(input())
    if re.match(pattern, n):
        print(True)
    else:
        print(False)


# In[ ]:


#2) Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# In[ ]:


#3) Group(), Groups() & Groupdict()

import re
s = str(input())
m=re.search(r'(\w)\1', s)
if m:
    print(m.group(1))
else:
    print(-1)


# In[ ]:


#4) Re.findall() & Re.finditer()
import re
s=input()
m=re.findall(r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', s)
if m:
    for i in m:
        print(i[1])
else:
    print(-1)


# In[ ]:


#5)Re.start() & Re.end()


# In[ ]:


#6)Regex Substitution
import re
pattern = "(?<= )(\&\&|\|\|)(?= )"
x = lambda match: 'and' if match.group() == '&&' else 'or'

for i in range(int(input())):
    print(re.sub(pattern, x, input()))


# In[ ]:


#7)Validating Roman Numerals


# In[ ]:


#8)Validating phone numbers

import re
n=int(input())
for i in range(0,n):
    x=input()
    b=re.match(r"[789]{1}[\d]{9}",x)
    if len(x)==10 and bool(b)==True:
        print("YES")
    else:
        print("NO")


# In[ ]:


#9)Validating and Parsing Email Addresses

import re
n=int(input())
for i in range(0,n):
    x=input().split()
    user=x[0]
    email=x[1]
    y=re.match(r"<[a-zA-Z]{1}[a-zA-Z0-9-._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>",email)
    if bool(y)==True:
        print(user,email)


# In[ ]:


#10)Hex Color Code


# In[ ]:


#11)HTML Parser - Part 1


# In[ ]:


#12)HTML Parser - Part 2


# In[ ]:


#13)Detect HTML Tags, Attributes and Attribute Values


# In[ ]:


#14)Validating UID


# In[ ]:


#15)Validating Credit Card Numbers


# In[ ]:


#16)Validating Postal Codes


# In[ ]:


#17)Matrix Script


# In[ ]:





# # XML

# In[ ]:


#1) XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    a=0
    for i in node.iter(): 
        a += len(i.attrib)
    return a

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# In[ ]:


#2) XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree
lev=[]
maxdepth = 0
def depth(elem, level):
    if level<0:
        level = 0
    global maxdepth
    lev.append(level)
    maxdepth=max(lev)
    for i in elem:
        depth(i,level +1 )

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# In[ ]:





# # CLOSURES AND DECORATORS

# In[ ]:


#1)Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        z = []
        for i in l:
            z.append(f"+91 {i[-10:-5]} {i[-5:]}")
        f(z)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# In[ ]:


#2)Decorators 2 - Name Directory
mport operator

def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda x: int(x[2]))
        l=[f(i) for i in people]
        return l
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# # NUMPY

# In[ ]:


#1) Arrays

import numpy

def arrays(arr):
    l= []
    for i in range(len(arr)-1, -1, -1):
        l.append(arr[i])
    res= numpy.array(l, float)
    return res
        
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[ ]:


#2)Shape and Reshape

import numpy
l= list(map(int, input().strip().split(' ')))
arr=numpy.array(l)
arr.shape=(3,3)
print(arr)


# In[ ]:


#3)Transpose and Flatten

import numpy
a=[]
l= list(map(int, input().strip().split(' ')))
for i in range(0,l[0]):
    a.append(list(map(int, input().strip().split(' '))))
    
arr=numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten())


# In[ ]:


#4) Concatenate 

import numpy as np

l= list(map(int, input().strip().split(' ')))
n,m=[],[]
for i in range(0,l[0]):
    n.append(list(map(int, input().strip().split(' '))))
for i in range(0,l[1]):
    m.append(list(map(int, input().strip().split(' '))))
    
arrn=np.array(n)
arrm=np.array(m)
print(np.concatenate((arrn,arrm),axis=0))


# In[ ]:


#5)Zeros and Ones

import numpy

l= list(map(int, input().strip().split(' ')))
print(numpy.zeros((l),dtype = int))

print(numpy.ones((l),dtype = int))


# In[ ]:


#6)Eye and Identity

import numpy

l= list(map(int, input().strip().split(' ')))

numpy.set_printoptions(legacy='1.13')
print(numpy.eye(l[0],l[1]))


# In[ ]:


#7)Array Mathematics

import numpy

l= list(map(int, input().strip().split(' ')))
a,b=[],[]
for i in range(0, l[0]):
    a.append(list(map(int, input().strip().split(' '))))
for i in range(0, l[0]):
    b.append(list(map(int, input().strip().split(' '))))

a=numpy.array(a)
b=numpy.array(b)
print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))


# In[ ]:


#8)Floor, Ceil and Rint

import numpy

l= list(map(float, input().strip().split(' ')))
my_array=numpy.array(l)
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))


# In[ ]:


#9)Sum and Prod
import numpy
a=[]
l= list(map(int, input().strip().split(' ')))
for i in range(0,l[0]):
    a.append(list(map(int, input().strip().split(' '))))
    
a=numpy.array(a)
b=(numpy.sum(a, axis = 0))        

print(numpy.prod(b))


# In[ ]:


#10)Min and Max

import numpy

a=[]
l= list(map(int, input().strip().split(' ')))
for i in range(0,l[0]):
    a.append(list(map(int, input().strip().split(' '))))
    
a=numpy.array(a)
b=(numpy.min(a, axis = 1))        

print(numpy.max(b))


# In[ ]:


#11)Mean, Var, and Std

import numpy

a=[]
l= list(map(int, input().strip().split(' ')))
for i in range(0,l[0]):
    a.append(list(map(int, input().strip().split(' '))))
    
a=numpy.array(a)
print(numpy.mean(a, axis = 1))        
print(numpy.var(a, axis = 0)) 
print(numpy.round(numpy.std(a, axis=None),11))       
       


# In[ ]:


#12)Dot and Cross

import numpy

n=int(input())
a,b=[],[]
for i in range(0,n):
    a.append(list(map(int, input().strip().split(' '))))
for i in range(0,n):
    b.append(list(map(int, input().strip().split(' '))))

print(numpy.dot(a,b))


# In[ ]:


#13)Inner and Outer
import numpy

a= list(map(int, input().strip().split(' ')))
b= list(map(int, input().strip().split(' ')))

print(numpy.inner(a,b))
print(numpy.outer(a,b))


# In[ ]:


#14)Polynomials

import numpy

p= list(map(float, input().strip().split(' ')))
x=int(input())
print(numpy.polyval(p, x))


# In[ ]:


#15)Linear Algebra

import numpy

n=int(input())
a=[]
for i in range(0,n):
    a.append(list(map(float, input().strip().split(' '))))
print(round(numpy.linalg.det(a),2))


# # PYTHON CHALLENGES

# In[ ]:


#Birthday cake candles

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    c=candles.sort()
    m=max(candles)
    return candles.count(m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


# kangaroo

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    elif x1 < x2 and v1==v2:
        return "NO"
    p=(x2-x1)/(v1-v2)
    if p.is_integer()==False:
        return "NO"
    elif p >= 0:
        return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


# Strange advertising

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    pop=5
    z=0
    for i in range(0,n):
        likes=(pop//2)
        pop=likes*3
        z+=likes
    return z


# In[ ]:


# recursive digit sum

import math
import os
import random
import re
import sys


def superDigit(n, k):
    x=sum(list(map(int,n)))*k
    x=str(x)
    while len(x)>1:
        
        x=sum(list(map(int,x)))
        x=str(x)
    return x   # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:


# Insertion sort 1

import math
import os
import random
import re
import sys



def insertionSort1(n, arr):
    x = arr[-1]
    for i in range(0,n-1):
        if x < arr[n-i-2]:
            arr[n-i-1] = arr[n-i-2]
        else:
            arr[n-i-1] = x
            return(print(*arr))
        print(*arr)
    if arr[0] == arr[1]:
        arr[0] = x
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# In[ ]:


# insertion sort 2


import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    x=1
    while x < n:
        y = arr[x]
        i = x-1
        while y < arr[i] and i >=0 :
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = y
        s=list(map(str,arr))
        print(*s)
        x += 1
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


# In[ ]:





# In[ ]:




