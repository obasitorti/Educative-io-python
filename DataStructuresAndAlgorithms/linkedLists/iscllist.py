from circularlinked import Node
from circularlinked import CircularLinkedList

def is_circular_linked_list(self, input_list):
    if not input_list.head:
        return False

    cur = input_list.head
    while cur.next:
        cur = cur.next
        if cur.next == input_list.head:
            return True

    return False

        