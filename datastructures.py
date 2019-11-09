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


class Stack():

	def __init__(self):

		self.head = None


	def push(self, value):

		if not self.head:
			self.head = Node(value=value)

		else:
			new_node = Node(value=value, next=self.head)
			self.head = new_node


	def pop(self):

		if self.head:
			returnable_node = self.head
			self.head = self.head.next
			return returnable_node

		else:
			raise Exception('Stack Underflow')


	def isEmpty(self):

		return not self.head


	def peek(self):

		return self.head.value



class Queue():

	def __init__(self):

		self.head = None
		self.tail = None


	def isEmpty(self):

		return not self.head


	def enqueue(self, value):

		if self.isEmpty():
			self.head = Node(value=value)
			self.tail = self.head

		else:
			new_node = Node(value=value, previous=self.tail)
			self.tail.next = new_node
			self.tail = new_node


	def dequeue(self):

		if self.isEmpty():
			raise Exception("Empty queue")

		else:
			returnable = self.tail
			self.tail = self.tail.previous
			self.tail.next = None









		 	
