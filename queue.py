class queue:
    def __init__(self):
        self.queue=list()
    def add_element(self,num):
        if num not in self.queue:
            self.queue.insert(0,num)
            return True
        return False
    def size(self):
        return len(self.queue)
    def delete(self):
        self.queue.pop()
    def display(self):
        for i in self.queue:
            print(i)
hello=queue()
hello.add_element("1")
hello.add_element("2")
hello.add_element("3")
hello.add_element("4")
hello.delete()
hello.display()
print("The lenght of the queue is",hello.size())

    
