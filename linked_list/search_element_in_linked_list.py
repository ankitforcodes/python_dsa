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



my_ll = SingleLinkedList()