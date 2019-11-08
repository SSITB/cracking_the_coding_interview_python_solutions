class Node():

	def __init__(self, value=None, next_=None, previous=None):

		self.value = value
		self.next = next_
		self.previous = previous

	def set_value(self, value):

		self.value = value


	def get_value(self):

		return self.value


	def set_next(self, node):

		self.next = node


	def get_next(self):

		return self.next


	def set_previous(self, node):

		self.previous = node


	def get_previous(self):

		return self.previous


class SinglyLinkedList():

	def __init__(self):

		self.head = None
		self.tail = None


	def insert(self, value):

		node = Node(value=value)
		if not self.head:
			self.head = node
			self.tail = node

		else:
			# node.previous = self.tail
			self.tail.next = node
			self.tail = node 


	def print_linked_list(self):

		current_node = self.head
		printable_string = "None->"

		while current_node:

			if current_node.next:
				printable_string = printable_string+"["+str(current_node.value)+"]->"
			else:
				printable_string = printable_string+"["+str(current_node.value)+"]->"+"None"

			current_node = current_node.next

		print(printable_string)


class DoublyLinkedList():

	def __init__(self):

		self.head = None
		self.tail = None


	def insert(self, value):

		node = Node(value=value)
		if not self.head:
			self.head = node
			self.tail = node

		else:
			node.previous = self.tail
			self.tail.next = node
			self.tail = node 


	def print_linked_list(self):

		current_node = self.head
		printable_string = "None->"

		while current_node:

			if current_node.next:
				printable_string = printable_string+"["+str(current_node.value)+"]->"
			else:
				printable_string = printable_string+"["+str(current_node.value)+"]->"+"None"

			current_node = current_node.next

		print(printable_string)



		 	
