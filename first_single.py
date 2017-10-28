
class ListNode:
    def __init__(self, val = 42):
        self.val = val
        self.left = None
        self.right = None


def print_node(node):
    while node:
        print(node.val, end=" ")
        node = node.right
    print()


def first(array):
    if not array:
        return None
    d = dict()
    head = ListNode()
    tail = head
    for char in array:
        print_node(head)
        if char not in d:
            newNode = ListNode(char)
            d[char] = newNode
            tail.right = newNode
            newNode.left = tail
            tail = newNode
        elif d[char]:
            node = d[char]
            if not node.right:
                tail = node.left
                node.left.right = None
                node.left = None
            else:
                node.left.right = node.right
                node.right.left = node.left
                node.right = None
                node.left = None
            d[char] = None
        else:
            d[char] = None
    if head.right:
        return head.right.val

if __name__ == "__main__":
    array = "aabbcc"
    print(first(array))