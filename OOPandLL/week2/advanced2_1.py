def problem1():
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

    def merge_playlists(playlist1, playlist2, a, b):
        a_1 = playlist1
        b_1 = playlist1
        play2_end = playlist2
        for i in range(a-1):
            a_1 = a_1.next
            
        for i in range(b+1):
            b_1 = b_1.next
        
        while (play2_end and play2_end.next):
            play2_end = play2_end.next

        a_1.next = playlist2
        play2_end.next = b_1

        return playlist1
        

    playlist1 = Node(('Flea', 'St. Vincent'),
                    Node(('Juice', 'Lizzo'), 
                        Node(('Tenderness', 'Jay Som'),
                            Node(('Ego Death', 'The Internet'),
                                Node(('Empty', 'Kevin Abstract'))))))

    playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

    print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
problem1()