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

    def edit_dna_sequence(dna_strand, m, n):
        cur = dna_strand
        if (m <= 0):
            return None
        if (n <= 0):
            return dna_strand
        
        while (cur):
            for i in range(m-1):
                if (not cur):
                    break
                cur = cur.next
            
            prev = cur
            for j in range(n+1): #1 -> 2 -> 6 -> 7 -> 11 -> 12
                if (not cur):
                    break
                cur = cur.next
            prev.next = cur

        return dna_strand

    dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))
    print_linked_list(edit_dna_sequence(dna_strand, 1, 1))
    dna_strand2 = Node(1)
    print_linked_list(edit_dna_sequence(dna_strand2, 1,5))
problem1()