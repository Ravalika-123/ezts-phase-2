#STACK
stack=[]
def push_element():
    if len(stack)==n:
        print("stack is full")
    else:
        element=input("enter the element to be inserted in the stack:")
        stack.append(element)
        print(stack)
def pop_element():
    if not stack:
        print("stack is empty,add an element")
    else:
        d=stack.pop()
        print(d,"removed")
        print(stack)
n=int(input("enter size of the stack:"))
while True:
    print("select the operation 1.push,2.pop,3.quit:")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break3
        
    else:
        print("enter correct number")
