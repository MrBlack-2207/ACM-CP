def removeDuplicates(llist):
    # Write your code here
    if not llist:
        return None
    current = llist
    while current and current.next:
            if current.data==current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    return llist

'''Approach:
Firstly , handling the case where the linked list is empty , i.e. the head is None.
And then we initialise a pointer named current to the head of the linkedlist , and keep iterating until the current and current.next are not None.
If the data of the current node is equal to the data of the next node , then we skip that node by changing the next pointer of the current node to the next of the next node.
If the data of two consecutive nodes is not equal , then we move the current pointer to the next node normally,without skipping any node in between.
We finally return the head of the linked list after dealing with the duplicates.'''