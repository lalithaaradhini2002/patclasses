#for checking prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def outputlist(self):
        temp=self.head
        while(temp):
            if not(isPrime(temp.data)):
                print(temp.data,end="-->")
            temp=temp.next
        

if __name__ == '__main__':
    llist=linkedlist()
    llist.head=Node(1)
    second=Node(15)
    third=Node(16)
    fourth=Node(11)
    fifth=Node(7)
    llist.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    llist.outputlist()
    
            
