def problem1():
    def arrange_guest_arrival_order(arrival_pattern):
        return_string = ""
        order_stack = []

        for i in range(len(arrival_pattern)+1):
            order_stack.append(i)

            if (i == len(arrival_pattern) or arrival_pattern[i] == "I"):
                while(order_stack):
                    return_string += str(order_stack.pop()+1)
        
        return return_string
    print(arrange_guest_arrival_order("IIIDIDDD"))  
    print(arrange_guest_arrival_order("DDD"))  
problem1()
