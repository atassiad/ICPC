def problem2():
    def is_similar(sentence1, sentence2, similar_pairs):
        if (len(sentence1) != len(sentence2)):
            return False
        
        pairs = dict()

        for pair in similar_pairs:
            pairs[pair[0]] = pair[1]
            pairs[pair[1]] = pair[0]
        
        # {"on" : "in", "in" : "on"}
        for i in range(len(sentence1)):
            if (sentence1[i] == sentence2[i]):
                continue
            elif (sentence1[i] in pairs and pairs[sentence1[i]] == sentence2[i]):
                continue
            else:
                return False
        
        return True
    sentence1 = ["my", "type", "on", "paper"]
    sentence2 = ["my", "type", "in", "theory"]
    similar_pairs = [ ["on", "in"], ["paper", "theory"]]

    sentence3 = ["no", "tea", "no", "shade"]
    sentence4 = ["no", "offense"]
    similar_pairs2 = [["shade", "offense"]]

    sentence5 = ["no", "tea", "to", "spill"]
    sentence6 = ["no", "coffee", "to", "spill"]
    similar_pairs3 = [["coffee", "tea"]]

    print(is_similar(sentence1, sentence2, similar_pairs))
    print(is_similar(sentence3, sentence4, similar_pairs2))
    print(is_similar(sentence5, sentence6, similar_pairs3))

def problem3():
    def get_hint(secret, guess):
        bulls = 0
        cows = 0
        secret_map = {}
        guess_map = {}
        for i in range(len(secret)):
            if (secret[i] == guess[i]):
                bulls += 1
            else:
                if (secret[i] in secret_map):
                    secret_map[secret[i]] += 1 
                else:
                    secret_map[secret[i]] = 1
                if (guess[i] in guess_map):
                    guess_map[guess[i]] += 1
                else:
                    guess_map[guess[i]] = 1

        for common in secret_map.keys() & guess_map.keys():
            cows += min(secret_map[common], guess_map[common])
        
        return str(bulls)+"A"+str(cows)+"B"
    secret1 = "1807"
    guess1 = "7810"

    secret2 = "1123"
    guess2 = "0111"

    secret3 = "000111"
    guess3 = "111000"

    secret4 = "000000000"
    guess4 = "111111111"

    print(get_hint(secret1, guess1))
    print(get_hint(secret2, guess2))
    print(get_hint(secret3, guess3))
    print(get_hint(secret4, guess4))

import math
from collections import Counter
def problem4():
    def count_winning_pairings(star_power):
        pair_count = 0

        #create set for powers of 2
        two_set = set()
        for i in range(22):
            two_set.add(2**i)
        
        #create counter for star_power
        num_dict = Counter(star_power)
        for key in num_dict:
            for power_two in two_set:
                if (x := power_two-key) in num_dict:
                    if (x == key):
                        pair_count += int((num_dict[x]*(num_dict[x]-1))/2)
                    elif (x > key):
                        pair_count += num_dict[x]*num_dict[key]
        
        return pair_count
        
    star_power1 = [1, 3, 5, 7, 9]
    print(count_winning_pairings(star_power1))

    star_power2 = [1, 1, 1, 3, 3, 3, 7]
    print(count_winning_pairings(star_power2))

    star_power3 = [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64]
    print(count_winning_pairings(star_power3))

def problem5():
    def assign_unique_nicknames(nicknames):
        nick_dict = {}
        return_list = []
        for name in nicknames:
            if name[len(name)-1] == ")":
                name = name[:name.find("(")]
            if name in nick_dict:
                nick_dict[name] += 1
            else:
                nick_dict[name] = 1
            if (nick_dict[name] > 1):
                return_list.append(name + "(" + str(nick_dict[name]-1) + ")")
            else:
                return_list.append(name)
        return return_list
    nicknames1 = ["Champ","Diva","Champ","Ace"]
    print(assign_unique_nicknames(nicknames1))

    nicknames2 = ["Ace","Ace(1)","Ace","Maverick"]
    print(assign_unique_nicknames(nicknames2)) 

    nicknames3 = ["Star","Star","Star","Star","Star"]
    print(assign_unique_nicknames(nicknames3))
problem5()
