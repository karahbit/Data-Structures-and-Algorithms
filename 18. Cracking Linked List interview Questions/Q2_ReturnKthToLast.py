#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

from LinkedList import LinkedList


# def nthToLast(ll, n):
#     pointer1 = ll.head
#     pointer2 = ll.head

#     for i in range(n):
#         if pointer2 is None:
#             return None
#         pointer2 = pointer2.next

#     while pointer2:
#         pointer1 = pointer1.next
#         pointer2 = pointer2.next
#     return pointer1


# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(nthToLast(customLL, 3))


def kth_to_last(head, k):
    if head is None:
        return

    p1 = p2 = head

    for _ in range(k):
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next

    return p1.value


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(kth_to_last(customLL.head, 3))
