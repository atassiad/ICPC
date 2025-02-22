def problem1():
    def transpose(matrix):
        final_list = []
        for i in range(len(matrix[0])):
            list_part = []
            for j in range(len(matrix)):
                list_part.append(matrix[j][i])
            final_list.append(list_part)
        return final_list

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose(matrix))

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transpose(matrix))

def problem2_1():
    def add_matrices(matrix1, matrix2):
        #[matrix1[i][j] += matrix2[i][j] for i in range(len(matrix1) for j in range(len(matrix2)))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                matrix1[i][j] += matrix2[i][j]
        return matrix1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    print(add_matrices(matrix1, matrix2))

def problem2_2():
    def is_palindrome(word):
        i = 0
        j = len(word)-1
        while (i < j):
            if (word[i] != word[j]):
                return False
            i += 1
            j -= 1
        return True
    s = "madam"
    print(is_palindrome(s))

    s = "madamweb"
    print(is_palindrome(s))

    s = "racecar"
    print(is_palindrome(s))
    s = "aabbbbaa"
    print(is_palindrome(s))

def problem2_3():
    def squash_spaces(s):
        result=""
        for i in range(len(s)):
            if(s[i]!=" "):
                result+=s[i]
            if(s[i] == " " and s[i-1] != " "):
                result+=s[i]
        return result


    s = "   Up,     up,   and  away! "
    print(squash_spaces(s))
    s = "With great power comes great responsibility."
    print(squash_spaces(s))

def problem2_4():
    def two_sum(nums, target):
        #return list
        return_list = [0,0]

        #get dictionary mapping of each element
        cur_dict = {}
        for i in range(len(nums)):
            cur_dict.update({nums[i]:i})

        #iterate through each value and see if x + y pairing exists
        for i in range(len(nums)):
            target_num = target-nums[i]
            if (target_num in nums):
                return_list[0] = i
                return_list[1] = cur_dict[target_num]
                break

        return return_list
    
    nums = [3,3]
    print(two_sum(nums,6))

