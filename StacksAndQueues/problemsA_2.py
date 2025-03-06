from collections import deque

def problem1():
    def predictAdoption_victory(votes):
        cat_queue = deque()
        dog_queue = deque()

        for vote in votes:
            if (vote == "C"):
                cat_queue.appendleft("C")
            else:
                dog_queue.appendleft("D")

        for vote in votes:
            if (vote == "C" and len(dog_queue) != 0):
                dog_queue.popleft()
                if (len(dog_queue) == 0):
                    return "Cat Lovers"
            elif (vote == "D" and len(cat_queue) != 0):
                cat_queue.popleft()
                if (len(cat_queue) == 0):
                    return "Dog Lovers"

    print(predictAdoption_victory("CD")) 
    print(predictAdoption_victory("CDD")) 
    print(predictAdoption_victory("CCDD"))
    print(predictAdoption_victory("DDCCC"))

def problem3():
    def rearrange_animal_names(s):
        #walk a poitner down s, when we see a close parenthesis we pop off until we get open
        letter_stack = []

        for i in range(len(s)):
            if (s[i] == ")"):
                temp_string =""
                x = letter_stack.pop()
                while (x != "("):
                    temp_string += x
                    x = letter_stack.pop()
                
                #reappend rearranged letters onto letter stack
                for i in range(len(temp_string)):
                    letter_stack.append(temp_string[i])
            else:
                letter_stack.append(s[i])
        
        return "".join(letter_stack)
    print(rearrange_animal_names("(dribtacgod)"))
    print(rearrange_animal_names("(!(love(stac))I)")) 
    print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 
    print(rearrange_animal_names("(abcd)"))
    print(rearrange_animal_names("(u(love)i)"))
    print(rearrange_animal_names("(ed(et(oc))el)"))
problem3()
