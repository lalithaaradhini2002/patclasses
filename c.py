class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
def push(head_r,data):
    pointer1=Node(data)
    temp=head_r
    pointer1.data=data
    pointer.next=head_r
    if head_r != None:
        while temp_next != head_r:
            temp=temp.next
        temp.next=pointer1
    else:
        pointer1.next=pointer1
    
        
