def problem1():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_stack(head):
        current = head.front
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()

    class Stack:
        def __init__(self):
            self.front = None
        
        def is_empty(self):
            if (self.front):
                return False
            return True

        def push(self, value):
            new_node = Node(value=value)
            if (self.is_empty()):
                self.front = new_node
                new_node.next = None
                return
            new_node.next = self.front
            self.front = new_node
        
        def pop(self):
            if (self.is_empty()):
                return None
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        
        def peek(self):
            if (self.is_empty()):
                return None
            return self.front.value
    # Create a new Stack
    stack = Stack()

    # Add elements to the stack
    stack.push(('Educated', 'Tara Westover'))
    stack.push(('Gone Girl', 'Gillian Flynn'))
    stack.push(('Dune', 'Frank Herbert'))
    print_stack(stack)

    # View the front element
    print("Peek: ", stack.peek()) 

    # Remove elements from the stack
    print("Pop: ", stack.pop()) 
    print("Pop: ", stack.pop()) 

    # Check if the stack is empty
    print("Is Empty: ", stack.is_empty()) 

    # Remove the last element
    print("Pop: ", stack.pop()) 

    # Check if the queue is empty
    print("Is Empty:", stack.is_empty()) 

def problem2():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()

    def get_random(playlist):
        from random import randint
        pl_length = 0
        temp = playlist
        while (temp):
            pl_length += 1
            temp = temp.next
        
        rand_value = randint(0, pl_length-1)
        temp = playlist
        for i in range(rand_value):
            temp = temp.next
        
        return temp.value
    catalogue = Node(('Homegoing', 'Yaa Gyasi'), 
                    Node(('Pachinko', 'Min Jin Lee'),
                            Node(('The Night Watchman', 'Louise Erdrich'))))

    print(get_random(catalogue))

def problem3():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()

    def swap_books(shelf, k):
        #find kth element from beginning
        p1 = shelf
        for i in range(k-1):
            p1 = p1.next
        
        #create gap of k and find kth element from end
        p2 = shelf
        p3 = p1
        while (p3 and p3.next):
            p2 = p2.next
            p3 = p3.next
        
        #swap elements
        tempval = p1.value
        p1.value = p2.value
        p2.value = tempval
        return shelf
    shelf = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5')))))
    print_linked_list(swap_books(shelf, 4))
    shelf1 = Node('Book 1', Node('Book 2'))
    print_linked_list(swap_books(shelf1, 1))

def problem4():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()

    def spiralize_books(m, n, head):
        return_array = [[-1] * n for _ in range(m)]
        row_index = 0
        col_index = 0
        cur_book = head
        while(True):
            #increment col_index and row_index accordingly
            snapshot = [row_index, col_index]
            while (col_index + 1 < n and return_array[row_index][col_index+1] == -1):
                col_index += 1
                if (cur_book):
                    value = cur_book.val
                    cur_book = cur_book.next
                    return_array[row_index][col_index] = value
            while (row_index + 1 < m and return_array[row_index+1][col_index] == -1):
                row_index += 1
                if (cur_book):
                    value = cur_book.val
                    cur_book = cur_book.next
                    return_array[row_index][col_index] = value
            while (col_index -1 >= 0 and return_array[row_index][col_index-1] == -1):
                col_index -= 1
                if (cur_book):
                    value = cur_book.val
                    cur_book = cur_book.next
                    return_array[row_index][col_index] = value
            while (row_index -1 >= 0 and return_array[row_index-1][col_index] == -1):
                row_index -= 1
                if (cur_book):
                    value = cur_book.val
                    cur_book = cur_book.next
                    return_array[row_index][col_index] = value
            if (snapshot == [row_index, col_index]):
                break
        return return_array
    
    new_reads1 = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5', Node('Book 6', 
    Node('Book 7', Node('Book 8', Node('Book 9', Node('Book 10', Node('Book 11', Node('Book 12', Node('Book 13')))))))))))))
    new_reads2 = Node('Book 1', Node('Book 2', Node('Book 3')))

    print(spiralize_books(3, 5, new_reads1))
    print(spiralize_books(1, 4, new_reads2))
problem4()


