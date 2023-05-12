def stack_empty():
    stack=list()
    return stack
def isempty(stack):
    return len(stack)==0
def push(stack,n):
    stack.append(n)
    print("The elements are inserted "+n)
def pop(stack):
    if(isempty(stack)):
        return "stack is empty"
    else:
         return stack.pop()
def display(stack):
    print("The elemnets inserted are:")
    for i in stack:
        print(i)
stack=stack_empty()
push(stack,str(18))
push(stack,str(19))
push(stack,str(20))
push(stack,str(21))
pop(stack)
display(stack)

