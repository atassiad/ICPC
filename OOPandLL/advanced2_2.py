def problem1():
    class Player:
        def __init__(self, character, kart):
            self.character = character
            self.kart = kart
            self.items = []

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value.character, end=" -> " if current.next else "\n")
            current = current.next

    def arr_to_ll(arr):
        if (not arr):
            return None
        
        head = Node(arr[0])
        tempNode = head
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            tempNode.next = newNode
            tempNode = tempNode.next
        
        return head




    mario = Player("Mario", "Mushmellow")
    luigi = Player("Luigi", "Standard LG")
    peach = Player("Peach", "Bumble V")

    print_linked_list(arr_to_ll([mario, luigi, peach]))
    print_linked_list(arr_to_ll([peach]))

def problem2():
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    # Function with a bug!
    def remove_by_value(head, val):
        if not head:
            return None
        if head.value == val:
            return head.next  

        current = head
        while current.next:
            if current.next.value == val:
                current.next = current.next.next  
                return head  
            current = current.next

        return head
    
    head = Node("Daisy", Node("Mario", Node("Waluigi", Node("Baby Peach"))))
    print_linked_list(remove_by_value(head, "Mario"))
problem2()