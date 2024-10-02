def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(1)
    curr = dummy

    while head1 and head2:
        if head1.data<head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2=head2.next
        curr = curr.next
        
    if head1:
        curr.next = head1
    elif head2:
        curr.next = head2

    return dummy.next