class Villager:
        def __init__(self, name, species, personality, catchphrase, neighbor=None):
            self.name = name
            self.species = species
            self.personality = personality
            self.catchphrase = catchphrase
            self.furniture = []
            self.neighbor = neighbor

        def add_item(self, item_name):
             valid_items = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}
             if (type(item_name) == str and item_name in valid_items):
                  self.furniture.append(item_name)


def problem1():
    apollo = Villager("Apollo", "Eagle", "pah")
    print(apollo.name)
    print(apollo.species) 
    print(apollo.catchphrase)
    print(apollo.furniture)

def problem2():
    alice = Villager("Alice", "Koala", "guvnor")
    print(alice.furniture)

    alice.add_item("acoustic guitar")
    print(alice.furniture)

    alice.add_item("cacao tree")
    print(alice.furniture)

    alice.add_item("nintendo switch")
    print(alice.furniture)

def problem3():
    def of_personality_type(townies, personality_type):
        return_list = []
        for person in townies:
             if person.personality == personality_type:
                  return_list.append(person.name)
        return return_list
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

    print(of_personality_type([isabelle, bob, stitches], "Lazy"))
    print(of_personality_type([isabelle, bob, stitches], "Cranky"))

def problem4():
    def message_received(start_villager, target_villager):
        temp_villager = start_villager

        while (temp_villager.neighbor != None):
            if (temp_villager.neighbor == target_villager):
                return True
            temp_villager = temp_villager.neighbor
        return False
    
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
    kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
    isabelle.neighbor = tom_nook
    tom_nook.neighbor = kk_slider

    print(message_received(isabelle, kk_slider))
    print(message_received(kk_slider, isabelle))

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

    kk_slider = Node("K.K. Slider")
    harriet = Node("Harriet")
    saharah = Node("Saharah")
    isabelle = Node("Isabelle")
    kk_slider.next = harriet
    harriet.next = saharah
    saharah.next = isabelle
    isabelle.next = None
    print_linked_list(kk_slider)

def problem6():
    class Node:
        def __init__(self, fish_name, next=None):
            self.fish_name = fish_name
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.fish_name, end=" -> " if current.next else "\n")
            current = current.next

    def catch_fish(head):
        if (not head):
            print("Aw! Better luck next time!")
            return head
        print("I caught a ", head.fish_name)
        head = head.next
        return head
    
    fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
    empty_list = None

    print_linked_list(fish_list)
    print_linked_list(catch_fish(fish_list))
    print(catch_fish(empty_list))

def problem7():
    class Node:
        def __init__(self, fish_name, next=None):
            self.fish_name = fish_name
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.fish_name, end=" -> " if current.next else "\n")
            current = current.next

    def fish_chances(head, fish_name):
        total_fish = 0
        fish_appears = 0
        temp_head = head
        while (temp_head != None):
            if (temp_head.fish_name == fish_name):
                fish_appears += 1
            total_fish += 1
            temp_head = temp_head.next
        
        return round(fish_appears/total_fish, 2)
    
    fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
    print(fish_chances(fish_list, "Dace"))
    print(fish_chances(fish_list, "Rainbow Trout"))
problem7()