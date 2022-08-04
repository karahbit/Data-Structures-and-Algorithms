"""
	This file contains provides the implementation for a Binary Search Tree.
	It only supports integers.

	All expected standard operations are implemented, including add, remove,
	search, contains. An additional get_deepest is a useful function to get
	the deepest nodes in the tree.

"""

from typing import Union

class Node:
	""" This repreesnts a single Node in a Binary Search Tree """
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def add(self, value: int) -> bool:
		""" Add a value to the binary search tree """
		if self.value == value:
			return False
		elif value < self.value:
			if self.left is None:
				self.left = Node(value)
				return True
			else:
				return self.left.add(value)
		elif value > self.value:
			if self.right is None:
				self.right = Node(value)
				return True
			else:
				return self.right.add(value)

	def remove(self, value: int) -> 'Node':
		""" Remove a value from this sub-bst """
		if self.value == value:
			# No children
			num_children = 0
			if self.left:
				num_children += 1
			if self.right:
				num_children += 1
			
			if num_children == 0:
				return None
			elif num_children == 1:
				return self.left if self.left else self.right
			elif num_children == 2:
				# Find immediate successor
				successor = self.right
				while successor.left:
					successor = successor.left

				# Take successor's value to maintain structure.
				self.value = successor.value

				# Lets now delete the node we've stolen
				self.right = self.right.remove(successor.value)
				
				return self

		elif value < self.value:
			if self.left:
				self.left = self.left.remove(value)
			return self
		elif value > self.value:
			if self.right:
				self.right = self.right.remove(value)
			return self

	def get_deepest(self, current_lvl: int) -> tuple:
		"""
			Gets the deepest nodes and their depths of this Node
			The format is (NodeCSV, Depth)
			where NodeCSV is is a comma seperated list of the deepest nodes
			and Depth is the depth of those nodes
		"""
		if not self.left and not self.right:
			return ([self.value], current_lvl)
		
		left_result = self.left.get_deepest(current_lvl+1) if self.left else ([],current_lvl)
		right_result = self.right.get_deepest(current_lvl+1) if self.right else ([],current_lvl)

		if left_result[1] == right_result[1]:
			return (left_result[0] + right_result[0], left_result[1])
		elif left_result[1] > right_result[1]:
			return left_result
		else:
			return right_result

	def search(self, value: int) -> 'Node':
		""" Search this sub-tree for the value, returning the whole subtree """
		if self.value == value:
			return self
		elif value < self.value:
			if self.left:
				return self.left.search(value)
			else:
				return None
		elif value > self.value:
			if self.right:
				return self.right.search(value)
			else:
				return None

	def contains(self, value: int) -> bool:
		result = self.search(value)
		return True if result else False

	def __str__(self) -> str:
		return f'{self.value} {self.left} {self.right}'
				

class BinarySearchTree:
	""" This is a binary search tree supporting integers. """
	def __init__(self, values: Union[int,list]=None):
		""" Create a binary search tree """
		self.root = None
		if isinstance(values,list) and len(values)>0:
			self.root = Node(values[0])
			for val in values[1:]:
				self.root.add(val)
		elif isinstance(values, int):
			self.root = Node(values)

	def add(self, value: int) -> bool:
		""" Add a value to the binary search tree """
		if self.root == None:
			self.root = Node(value)
			return True
		else:
			return self.root.add(value)

	def remove(self, value: int) -> 'BinarySearchTree':
		""" Remove a value from the binary search tree """
		if self.root is None:
			return self
		else:
			self.root = self.root.remove(value)
			return self

	def contains(self, value: int) -> bool:
		""" Check if the binary search tree contains the value """
		if self.root:
			return self.root.contains(value)
		else:
			return False

	def search(self, value: int) -> 'BinarySearchTree':
		""" Get the subtree of a binary search tree by value """
		bst = BinarySearchTree()
		if self.root:
			bst.root = self.root.search(value)
		return bst

	def get_deepest(self) -> tuple:
		"""
			Gets the deepest nodes and their depths.
			The format is (NodeCSV, Depth)
			where NodeCSV is is a comma seperated list of the deepest nodes
			and Depth is the depth of those nodes
		"""
		if self.root is None:
			return ([], None)
		else:
			return self.root.get_deepest(current_lvl=0)

	def __str__(self) -> str:
		""" Return a simple string representation of the binary search tree """
		return str(self.root)

if __name__ == '__main__':
	bst = BinarySearchTree([20, 14, 25, 23, 30, 26, 27])
	print(bst)