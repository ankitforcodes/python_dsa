class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	def insert(self, value, location):
		new_node = Node(value)

		# find if head is None; if it is, then your LL is empty and so the new node becomes the head as well as tail of the node
		if self.head == None:
			print("No head: Adding as head")
			self.head = new_node
			self.tail = new_node

		else:
			print("Head found")
			# if you want to insert in beginning, i.e. location = 0
			if location == 0:
				print("Making new head")
				new_node.head = self.head
				self.head = new_node

			# if you want to insert in the end, i.e. location = -1
			if location == -1:
				print("Making new tail")
				self.tail.next = new_node
				self.tail = new_node
			# Or else insert it at any numbered location (starting from 0)
			else:
				print("Inserting in middle")
				index = 0
				temp_node = self.head
				while index < location-1:
					temp_node = temp_node.next
					index = index + 1

				second_node = temp_node.next
				temp_node.next = new_node
				new_node.next = second_node 


my_ll = SingleLinkedList()

for nodes in my_ll:
	print(nodes.value)

print("####################")
my_ll.insert(10,0)
my_ll.insert(20,1)
my_ll.insert(30,2)
my_ll.insert(40,3)
my_ll.insert(50,4)
my_ll.insert(60,5)


for nodes in my_ll:
	print(nodes.value)

print("####################")
my_ll.insert(100,2)

for nodes in my_ll:
	print(nodes.value)

print("####################")
my_ll.insert(500,4)
for nodes in my_ll:
	print(nodes.value)
