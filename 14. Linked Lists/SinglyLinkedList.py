#   Created by Elshad Karimov on 27/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode.next:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    #  Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next != self.tail:
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode.next.next:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                if nextNode.next == self.tail:
                    self.tail = tempNode
    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 10)
singlyLinkedList.insertSLL(3, 3)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(4, 6)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(5, 2)

print([node.value for node in singlyLinkedList]) 



singlyLinkedList.deleteNode(0)
print([node.value for node in singlyLinkedList]) 
print(singlyLinkedList.head.value, singlyLinkedList.tail.value)
singlyLinkedList.deleteNode(-1)
print([node.value for node in singlyLinkedList]) 
print(singlyLinkedList.head.value, singlyLinkedList.tail.value)
singlyLinkedList.deleteNode(2)
print([node.value for node in singlyLinkedList]) 
print(singlyLinkedList.head.value, singlyLinkedList.tail.value)
singlyLinkedList.deleteNode(10)
print([node.value for node in singlyLinkedList]) 
print(singlyLinkedList.head.value, singlyLinkedList.tail.value)
# singlyLinkedList.deleteEntireSLL()
# print([node.value for node in singlyLinkedList]) 






