#Problem 2 
def problem2():
    def final_value_after_operations(operations):
        running_count = 1
        if_values = {"bouncy": 1, "flouncy": 1, "trouncy": -1, "pouncy": -1}
        for operation in operations:
            running_count += if_values.get(operation, 0)
        return running_count

    operations1 = ["trouncy", "flouncy", "flouncy"]
    operations2 = ["bouncy", "bouncy", "flouncy"]
    print(f"Operations1: {final_value_after_operations(operations1)}")
    print(f"Operations2: {final_value_after_operations(operations2)}")

#Problem 3
def problem3():
    def tiggerify(word):
        word = word.lower()
        letter_combos = ['t', 'i', 'gg', 'er']
        for combo in letter_combos:
            word = word.replace(combo, '')
        return word
    word1 = "Trigger"
    word2 = "Eggplant"
    word3 = "Choir"
    word4 = "Phiiiiiiiiiiter"
    print(f"Word1: {tiggerify(word1)}")
    print(f"Word2: {tiggerify(word2)}")
    print(f"Word3: {tiggerify(word3)}")
    print(f"Word4: {tiggerify(word4)}")

#Problem 4
def problem4():
    def non_decreasing(nums):
        return sum(nums[i] > nums[i+1] for i in range(len(nums)-1)) == 1
    nums = [4, 2, 3]
    print(non_decreasing(nums))
    nums = [4, 2, 1]
    print(non_decreasing(nums))

#Problem 5
def problem5():
    def find_missing_clues(clues, lower, upper):
        new_clues = [clue for clue in clues if clue >= lower and clue <= upper]
        ranges = []
        if (clues[0] > lower and clues[0]+1 > lower):
            ranges.append([clues[0]-1, lower+1])
        for i in range(len(new_clues)-1):
            if new_clues[i+1]-new_clues[i] > 1:
                ranges.append([clues[i]+1, clues[i+1]-1])
        if (clues[len(clues)-1] < upper and clues[len(clues)-1]+1 < upper):
            ranges.append([clues[len(clues)-1]+1, upper])
        return ranges
    clues = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(find_missing_clues(clues, lower, upper))

def problem6():
    def harvest(vegetable_patch):
        return sum(vegetable_patch[i][j] == 'c' for i in range(len(vegetable_patch)) for j in range(len(vegetable_patch[0])))
    vegetable_patch = [
        ['x', 'c', 'x'],
        ['x', 'x', 'x'],
        ['x', 'c', 'c'],
        ['c', 'c', 'c']
    ]
    print(harvest(vegetable_patch))

def problem7():
    def good_pairs(pile1, pile2, k):
        return sum((pile1[i] % (pile2[j]*k)) == 0 for i in range(len(pile1)) for j in range(len(pile2)))

    pile1x = [1, 3, 4]
    pile2x = [1, 3, 4]
    kx = 1
    print(good_pairs(pile1x, pile2x, kx))

    pile3 = [1, 2, 4, 12]
    pile4 = [2, 4]
    k1 = 3
    print(good_pairs(pile3, pile4, k1))

def problem8():
    def local_maximums(grid):
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        new_grid_rws = grid_rows-2
        new_grid_cols = grid_cols-2
        final_grid = [[0] * new_grid_cols for i in range(new_grid_rws)]
        for i in range(new_grid_rws):
            for j in range(new_grid_cols):
                temp_grid = [max(row[j:j+3]) for row in grid[i:i+3]]
                final_grid[i][j] = max(temp_grid)
        return final_grid
    grid = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
    print(local_maximums(grid))
    grid1 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
       [1, 1, 2, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]
    ]
    print(local_maximums(grid1)) #

def problem9():
    def words_with_char(words, x):
        return [i for i, word in enumerate(words) if x in word]
    words = ["batman", "superman"]
    x = "a"
    print(words_with_char(words, x))

    words = ["black panther", "hulk", "black widow", "thor"]
    x = "a"
    print(words_with_char(words, x))

    words = ["star-lord", "gamora", "groot", "rocket"]
    x = "z"
    print(words_with_char(words, x))
#problem9()

def problem11():
    def shuffle(message, indices):
        return ''.join([message[indice] for indice in indices])
    message = "evil"
    indices = [3, 1, 2, 0]
    print(shuffle(message, indices))

    message = "findme"
    indices = [0, 1, 2, 3, 4, 5]
    print(shuffle(message, indices))

def problem13():
    def wealthiest_customer(accounts):
        max_sum = max(sum(account) for account in accounts)  # Find max sum
        index = next(i for i, account in enumerate(accounts) if sum(account) == max_sum)  # Find index of max sum
        return [index, max_sum]
    accounts = [
        [1, 2, 3],
        [3, 2, 1]
    ]
    print(wealthiest_customer(accounts))

    accounts = [
        [1, 5],
        [7, 3],
        [3, 5]
    ]
    print(wealthiest_customer(accounts))

    accounts = [
        [2, 8, 7],
        [7, 1, 3],
        [1, 9, 5]
    ]
    print(wealthiest_customer(accounts))

def problem14():
    def smaller_than_current(nums):
        return [sum(1 for j in range(len(nums)) if nums[j] < nums[i]) for i in range(len(nums))]
    nums = [8, 1, 2, 2, 3]
    print(smaller_than_current(nums))

    nums = [6, 5, 4, 8]
    print(smaller_than_current(nums))

    nums = [7, 7, 7, 7]
    print(smaller_than_current(nums))

def problem15():
    def diagonal_sum(grid):
        return sum(grid[i][i] for i in range(len(grid)))+sum(grid[len(grid)-1-j][j] for j in range(len(grid)))
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(diagonal_sum(grid))

    grid = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print(diagonal_sum(grid))

    grid = [
        [5]
    ]
    print(diagonal_sum(grid))

def problem16():
    def defuse(code, k):
        new_code = [0]*len(code)
        if (k > 0):
            for i in range(len(code)):
                for j in range(1, k+1):
                    new_code[i] += code[(i+j) % len(code)]
            return new_code
        elif(k == 0):
            return new_code
        else:
            for i in range(len(code)):
                for j in range(1, abs(k)+1):
                    new_code[i] += code[(i-j) % len(code)]
            return new_code

    code = [5, 7, 1, 4]
    k = 3
    print(defuse(code, k))

    code = [1, 2, 3, 4]
    k = 0
    print(defuse(code, k))

    code = [2, 4, 9, 3]
    k = -2
    print(defuse(code, k))
problem16()
    
                

