def problem1():
    def blueprint_approval(blueprints):
        return sorted(blueprints)
    print(blueprint_approval([3, 5, 2, 1, 4])) 
    print(blueprint_approval([7, 4, 6, 2, 5])) 

def problem2():
    def build_skyscrapers(floors):
        skyscrapers = 1

        for i in range(len(floors)-1):
            if (floors[i] > floors[i+1]):
                skyscrapers += 1
        
        return skyscrapers

    print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
    print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
    print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

def problem3():
    def max_corridor_area(height):
        max_water = 0

        i = 0
        j = len(height)-1

        while (i < j):
            max_water = max(max_water, min(height[j], height[i])*(j-i))
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
    print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
    print(max_corridor_area([1, 1])) 

def problem4():
    def min_swaps(s):
        u_stack = []

        for letter in s:
            u_stack.append(letter)
            while (len(u_stack) >=2 and u_stack[-1] == "]" and u_stack[-2] == "["):
                u_stack.pop()
                u_stack.pop()
        
        if (len(u_stack) <= 2):
            return 1
        elif (len(u_stack)/2 % 2 == 0):
            return len(u_stack) // 4
        else:
            return (len(u_stack)+2)//4


    print(min_swaps("][][")) 
    print(min_swaps("]]][[[")) 
    print(min_swaps("[]"))  
    print(min_swaps("]]]][[[["))
    print(min_swaps("]]]]][[[[["))
    print(min_swaps("]]]]]][[[[[["))
    print(min_swaps("][]][[]["))

def problem5():
    def make_balanced_room(s): 
        index_stack = []
        index_map = set()

        for i in range(len(s)):
            if (s[i] == "("):
                index_stack.append(i)
            elif (index_stack and s[i] == ")"):
                index_stack.pop()
            elif (s[i] == "(" or s[i] == ")"):
                index_map.add(i)

        index_map = index_map | set(index_stack)
        return_string = ""
        for i in range(len(s)):
            if (i not in index_map):
                return_string += s[i]

        return return_string
    
    print(make_balanced_room("art(t(d)e)sign)")) 
    print(make_balanced_room("d)e(s)ign")) 
    print(make_balanced_room("))((")) 

def problem7():
    def next_greater_dream(dreams):
        dream_size = len(dreams)
        return_arr = []

        for i in range(dream_size):
            max_element = dreams[i]
            for j in range(1, dream_size):
                if ((max_element := max(max_element, dreams[(i+j)%dream_size])) != dreams[i]):
                    break
            if (max_element == dreams[i]):
                return_arr.append("-1")
            else:
                return_arr.append(max_element)
        
        return return_arr

    print(next_greater_dream([1, 2, 1])) 
    print(next_greater_dream([1, 2, 3, 4, 3])) 
problem7()