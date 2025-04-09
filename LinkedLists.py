class node:
    def __init__(self , data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        curr=self.head
        while curr != None:
            print(curr.data,end=" -> ")
            curr=curr.next
        print("Null")
    def insertend(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next != None:
            last = last.next
        last.next = newnode
    def insertbeg(self,data):
        newnode = node(data)
        newnode.next= self.head
        self.head = newnode
        

ll = linkedlist()
ll.insertbeg(9)
ll.insertbeg(8)
ll.insertend(10)
ll.insertend(11)
ll.insertend(12)
ll.insertend(13)
ll.insertend(14)
ll.insertend(15)
ll.insertend(16)

ll.printlist()
