class Node():
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
		if self.head is None:
			self.head = new_node
			self.tail = new_node

		else:
			if location == 0:
				new_node.head = self.head
				self.head = new_node
			elif location == -1:
				self.tail.next = new_node
				self.tail = new_node
			else:
				temp_node = self.head
				location_count = 0
				while location_count < (location-1):
					temp_node = temp_node.next
					location_count+=1

				end_node = temp_node.next
				temp_node.next = new_node
				new_node.next = end_node

	def traversal(self):
		if self.head is None:
			print("Linked List empty")
		else:
			temp_node = self.head
			while temp_node is not None:
				print(temp_node.value)
				temp_node = temp_node.next

	def find_node(self, value):
		if self.head is None:
			return "Not Found: as LL is empty"
		else:
			temp_node = self.head
			while temp_node is not None:
				if temp_node.value == value:
					return "Value Found"
				else:
					temp_node = temp_node.next

			return "Not found"

	def delete_node_by_index(self,index):
		if self.head is None:
			print("Nothing to delete")
		else:
			if index == 0:
				if self.head == self.tail:
					self.head = None
					self.tail = None
				else:
					self.head = self.head.next
			elif index == -1:
				if self.head == self.tail:
					self.head = None
					self.tail = None
				else:
					temp_node = self.head
					while temp_node is not None:
						if temp_node.next == self.tail:
							break
						else:
							temp_node = temp_node.next

					self.tail = temp_node
					temp_node.next = None



			



my_ll = SingleLinkedList()
my_ll.insert(10,0)
my_ll.insert(20,1)
my_ll.insert(30,2)
my_ll.insert(40,3)
my_ll.insert(50,4)
my_ll.insert(60,5)
print(my_ll.traversal())
print("####")
my_ll.delete_node(30)
print(my_ll.traversal())