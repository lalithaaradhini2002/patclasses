#Cross pattern printing

"""n=int(input())
for i in range(0,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
for k in range(i,n-1):
    print("*",end=" ")
print()
"""

#Anagram
from itertools import permutations
def Anagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        return True
    else:
        return False
if(Anagram):
    print("Anagram")
    k=permutations(s1)
    for i in k:
        print(i)
else:
    print("Not an Anagram")
s1=input()
s2=input()
print(Anagram(s1,s2))
        
