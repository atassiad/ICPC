def problem1():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def find_max(head):
        max_var = float('-inf')
        while (head != None):
            max_var = max(max_var, head.value)
            head = head.next
        return max_var
    
    head1 = Node(5, Node(6, Node(7, Node(8))))

    # Linked List: 5 -> 6 -> 7 -> 8
    print(find_max(head1))

    head2 = Node(5, Node(8, Node(6, Node(7))))

    # Linked List: 5 -> 8 -> 6 -> 7
    print(find_max(head2))

    head3 = Node(5)
    print(find_max(head3))
problem1()

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

    def remove_tail(head):
        if head is None:
            return None
        if head.next is None:
            return None 
            
        current = head
        while current.next.next: 
            current = current.next

        current.next = None 
        return head
    head = Node("Isabelle", Node("Alfonso", Node("Cyd")))
    print_linked_list(remove_tail(head))

    head1 = Node("Isabelle", Node("Alfonso"))
    print_linked_list(remove_tail(head1))

def problem3():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def delete_dupes(head):
        seen_dict = dict()

        #go once through LL and update seen_dict
        temp_head = head
        while(temp_head):
            seen_dict[temp_head.value] = seen_dict.get(temp_head.value, 0) + 1
            temp_head = temp_head.next
        
        #go through again w/ temphead and remove dupes
        temp_head = Node("temp")
        temp_head.next = head

        prev = temp_head
        cur = head
        while (cur):
            if (seen_dict[cur.value] > 1):
                #update pointers
                cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        
        return temp_head.next
    
    head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
    head1 = Node(1, Node(1))
    head2 = None
    # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
    print_linked_list(delete_dupes(head))
    print_linked_list(delete_dupes(head1))
    print_linked_list(head2)

def problem4():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def has_cycle(head):
        slow = head
        fast = head

        while (slow and fast):
            slow = slow.next
            if (fast.next):
                fast = fast.next.next

            if (slow and fast and slow.value == fast.value):
                return True
        
        return False

    #peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))
    #print(has_cycle(peach))

def problem5():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def remove_nth_from_end(head, n):
        
        #find size of list
        size = 0
        temp_head = head
        while (temp_head):
            size += 1
            temp_head = temp_head.next
        
        n = size - n #want to remove nth node from front now
        size = 0

        temp_head = Node("temp")
        temp_head.next = head

        prev = temp_head
        cur = head
        while (cur and size != n):
            size += 1
            cur = cur.next
            prev = prev.next

        cur = cur.next
        prev.next = cur

        return temp_head.next
    
    def remove_nth_from_end_optimized(head, n):
        temp_head = Node("temp")
        temp_head.next = head

        slow = head
        fast = head
        prev = temp_head
        n_count = 0
        while (fast):
            n_count += 1
            if (n_count > n):
                slow = slow.next
                prev = prev.next
            fast = fast.next
        
        #remove slow pointer
        slow = slow.next
        prev.next = slow

        return temp_head.next

    head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
    head2 = Node("Rainbow Trout", Node("Ray"))
    head3 = Node("Rainbow Stag")


    print_linked_list(remove_nth_from_end_optimized(head1, 2))
    print_linked_list(remove_nth_from_end_optimized(head2, 1))
    print_linked_list(remove_nth_from_end_optimized(head3, 1))

def problem6():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next
            
    def reverse_first_k(head, k):
        if (not head or not head.next):
            return head
        
        new_tail = head

        cur = head
        next = head.next
        other_head = head.next.next # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        for i in range(k-1):
            if (next == None):
                break
            next.next = cur
            cur = next
            next = other_head
            if (other_head):
                other_head = other_head.next
        
        #merge seperated lists
        new_tail.next = next
        return cur
    head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
    print_linked_list(reverse_first_k(head, 6))
problem6()