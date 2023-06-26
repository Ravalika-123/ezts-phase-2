class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
        
        while temp:
            print(temp.data,"->",end="")
            temp=temp.next
        
node_1=Node("Ravalika")
SL=SLL()
SL.head=node_1
node_2=Node("Charitha")
print(node_1.next)
node_1.next=node_2
print(node_1.next)
#SL.head=node_2
node_3=Node("Sadwika")
node_4=Node("Raju")
node_2.next=node_3
print(node_2.next)
node_3.next=node_4
print(node_3.next)

SL.Insert_begining("abc")
SL.display()
print(SL.head.data)


def Insert_begining(self,data):
    new_node=Node(data)
    new_node=Node
SL.display()
def insert_position(self,pos,data):
    new_node=Node(data)
    temp=self.head
    for i in range(pos-1):
        temp=temp.next
    new_node.next=temp.next
    temp.next=new_node

