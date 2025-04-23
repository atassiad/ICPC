def problem1():
    def check_stock(inventory, part_id):
        left = 0
        right = len(inventory)-1

        while (left <= right):
            mid = (right+left) // 2
            if (inventory[mid] == part_id):
                return True
            elif (inventory[mid] < part_id):
                left = mid+1
            else:
                right = mid
        
        return False

    print(check_stock([1, 2, 5, 12, 20], 20))
    print(check_stock([1, 2, 5, 12, 20], 100))

def problem2():
    def check_stock(inventory, part_id):
        left = 0
        right = len(inventory)-1

        if (left > right):
            return False
        
        mid = (left + right) // 2
        if (inventory[mid] == part_id):
            return True
        elif (inventory[mid] < part_id):
            left = mid + 1
            return check_stock(inventory[left:], part_id)
        else:
            right = mid
            return check_stock(inventory[:right], part_id)

    print(check_stock([1, 2, 5, 20, 12], 20))
    print(check_stock([1, 2, 5, 20, 12], 100))
problem2()