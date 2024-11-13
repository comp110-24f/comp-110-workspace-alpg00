"""Practice with linked lists."""

from __future__ import annotations

class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"
    
two: Node = Node(2, None)
one: Node = Node(1, two)

def last(head: Node) -> int:
    """Return the last value of a non-empty list"""
    # Base Case: when head is the "last" node
    print(f"Enter last({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
    else:
        # Recursive case:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest

print(last(one))  # Expect to print 2
# print(last(courses)) # Expect to print 301