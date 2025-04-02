def problem1():
    def count_layers(sandwich):
        if (len(sandwich) == 1):
            return 1
        return 1 + count_layers(sandwich[1])
    sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
    sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

    print(count_layers(sandwich1))
    print(count_layers(sandwich2))
problem1()

def problem2():
    def reverse_helper(orders):
        if (len(orders) == 1):
            return orders[0]
        return reverse_helper(orders[1:]) + " " + orders[0]
    def reverse_orders(orders):
        return reverse_helper(orders.split(" "))
    print(reverse_orders("Bagel Sandwich Coffee"))
problem2()