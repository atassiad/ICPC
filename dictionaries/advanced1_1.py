def problem1():
    def total_treasures(treasure_map):
        rolling_sum = 0
        for value in treasure_map.values():
            rolling_sum += value
        return rolling_sum
    treasure_map1 = {
        "Cove": 3,
        "Beach": 7,
        "Forest": 5
    }

    treasure_map2 = {
        "Shipwreck": 10,
        "Cave": 20,
        "Lagoon": 15,
        "Island Peak": 5
    }

    print(total_treasures(treasure_map1)) 
    print(total_treasures(treasure_map2)) 
problem1()

def problem2():
    def can_trust_message(message):
        message = message.lower()
        return_dict = dict()
        for letter in message:
            if letter in return_dict:
                return_dict[letter] += 1
            else:
                return_dict[letter] = 1  
        if (len(return_dict.keys()) >= 26):
            return True
        return False
    message1 = "sphinx of black quartz judge my vow"
    message2 = "trust me"

    print(can_trust_message(message1))
    print(can_trust_message(message2))