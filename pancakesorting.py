def superflip(l):
    for i in l:
        e=[]
        k=max(l)
        e.append(k)
        l.remove(k)
        l.reverse()
def highestflip():
    if(l1.sort()!=e):
        superflip(e)

l=list(map(int,input().split()))
l1=l.copy()


print(superflip(l))
print(highestflip())

     
