class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None


my_linked_list = SingleLinkedList()

n1 = Node(10)
n2 = Node(20)

my_linked_list.head = n1
my_linked_list.head.next = n2
my_linked_list.tail = n2