l=[]
arr=[1,3,2,5,6]
for i in range(len(arr)):
    if arr[i]<=3:
        l.append(i)
count=0
for i in range(len(l)-1):
    if l[i+1]-l[i]==1:
        count=count+0
    else:
        count=count+1
print(count)
