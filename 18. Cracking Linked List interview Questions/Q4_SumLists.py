#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 4 - Sum Lists

from LinkedList import LinkedList, Node


# def sumList(llA, llB):
#     n1 = llA.head
#     n2 = llB.head
#     carry = 0
#     ll = LinkedList()

#     while n1 or n2:
#         result = carry
#         if n1:
#             result += n1.value
#             n1 = n1.next
#         if n2:
#             result += n2.value
#             n2 = n2.next
#         ll.add(result % 10)
#         carry = result // 10

#     if carry:
#         ll.add(carry)

#     return ll

def sumList(l1, l2):
    dummy = curr = Node()
    carry = 0

    while l1 or l2:
        result = carry
        if l1:
            result += l1.value
            l1 = l1.next
        if l2:
            result += l2.value
            l2 = l2.next
        curr.next = Node(result % 10)
        carry = result // 10
        curr = curr.next

    if carry:
        curr.next = Node(carry)

    return dummy.next


llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(2)
llB.add(9)
llB.add(5)
print(llA)
print(llB)
# print(sumList(llA, llB))
head = sumList(llA.head, llB.head)
print(head)
print(head.next)
print(head.next.next)
print(head.next.next.next)
print(head.next.next.next.next)
