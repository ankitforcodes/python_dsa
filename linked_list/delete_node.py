class Node():
	def __init__(self,value):
		self.value = value
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, value, location):
		new_node = Node(value)
		if self.head is None:
			#print("LL empty: Adding as first node")
			self.head = new_node
			self.tail = new_node

		else:
			#print("LL not empty")
			if location == 0:
				#print("Adding as new head")
				new_node.head = self.head
				self.head = new_node
			elif location == -1:
				#print("Adding as new tail")
				new_node.next = None
				self.tail.next = new_node
				self.tail = new_node
			else:
				#print("Adding in between")
				temp_node = self.head
				location_count = 0
				while location_count < (location-1):
					temp_node = temp_node.next
					location_count+=1

				end_node = temp_node.next
				temp_node.next = new_node
				new_node.next = end_node

				if temp_node == self.tail:
					self.tail = new_node

	def traversal(self):
		if self.head is None:
			print("Linked List empty")
		else:
			temp_node = self.head
			while temp_node is not None:
				print("LL Value: ", temp_node.value)
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
		print("######### Deleting Node at index: ",index,"##############")
		if self.head is None:
			print("Nothing to delete")
		else:
			if index == 0:
				if self.head == self.tail:
					print(self.head.value)
					print(self.tail.value)
					print("deleting head: head and tail same")
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
			else:
				location = 0
				prev_node = None
				next_node = None
				temp_node = self.head
				while location != index-1:
					prev_node = temp_node
					temp_node = temp_node.next
					location = location + 1

				prev_node.next = temp_node



			



my_ll = SingleLinkedList()
my_ll.insert(10,0)
my_ll.insert(20,-1)
my_ll.insert(30,2)
my_ll.insert(40,3)
my_ll.insert(50,4)
my_ll.insert(60,5)

print(my_ll.traversal())
my_ll.delete_node_by_index(0)
print(my_ll.traversal())
my_ll.delete_node_by_index(0)
print(my_ll.traversal())
my_ll.delete_node_by_index(0)
print(my_ll.traversal())
	