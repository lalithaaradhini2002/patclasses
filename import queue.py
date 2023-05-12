import queue
q=queue.Queue()
q.put(14)
q.put(15)
q.put(16)
q.put(17)
q.put(18)
q.put(19)
q.put(20)
n=q.size()
for i in range(n):
    x=q.get()
    for j in range(n-1):
        y=q.get()
        if x>y:
            q.put(y)
        else:
            q.put(x)
            x=y
while(q.empty()==False):
    print(q.queue[0],end=" ")
    q.get()
