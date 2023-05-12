class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertion_sort(abc):
    sorted_list=None
    curr_list=abc
    while(curr_list != None):
        next=curr_list.next
        sorted_list=sort(sorted_list,curr_list)
        curr_list=next
    abc=sorted_list
    return abc
def sort(abc,node):
    current=None
    if(abc==None or abc.data >= node.data):
        node.next=abc
        abc=node
    else:
        current=abc
        while currenr.next!=None and current.next.data<node.data:
            current=current.next
        node.next=current.next
        current.next=node
    return abc
def outputlist(abc):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
def push(abc,data):
    node=Node(0)
    node.data=data
    node.next=abc
    abc=node
    return abc
a=None
a=push(a,12)
a=push(a,11)
a=push(a,3)
a=push(a,5)
a=push(a,8)
a=insertion_sort(a)
outputlist(a)
        
#creating and inserting into linked list      
"""class LinkedList:
  def __init__(self):  
    self.head = None
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  def insertion(self):
      curr=None
      temp=self.head
      while(temp):
          
  def printLL(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next
  def push(

if __name__ == '__main__':
    obj=Linkedlist()
    obj.insert(10)
    obj.insert(12)
    obj.insert(5)
    obj.insert(3)
    obj.insert(1)
    obj.insert(0)
    obj.insert(17)
    
"""
