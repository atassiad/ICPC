def problem1():
    def analyze_library(library_catalog, actual_distribution):
        output_dict = {}
        for key1, key2 in zip(library_catalog, actual_distribution):
            output_dict[key1] = actual_distribution.get(key2)-library_catalog.get(key1)
        return output_dict
    library_catalog = {
        "Room A": 150,
        "Room B": 200,
        "Room C": 250,
        "Room D": 300
    }

    actual_distribution = {
        "Room A": 150,
        "Room B": 190,
        "Room C": 260,
        "Room D": 300
    }


    print(analyze_library(library_catalog, actual_distribution))

def problem2():
    def find_common_artifacts(artifacts1, artifacts2):
        set1 = set(artifacts1)
        set2 = set(artifacts2)
        return list(set1 & set2)
        
        # return_list = []
        # artifact_dict = set()
        # for art1, art2 in zip(artifacts1, artifacts2):
        #     if (art1 in artifact_dict):
        #         return_list.append(art1)
        #     else:
        #         artifact_dict.add(art1)
        #     if (art2 in artifact_dict):
        #         return_list.append(art2)
        #     else:
        #         artifact_dict.add(art2)
        # return return_list
    artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
    artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

    print(find_common_artifacts(artifacts1, artifacts2))

def problem3():
    def declutter(souvenirs, threshold):
        return_list = []
        freq_map = {}
        for souvenir in souvenirs:
            if (souvenir in freq_map):
                freq_map[souvenir] +=1
            else:
                freq_map[souvenir] = 1
        
        for key in freq_map:
            if (freq_map[key] < threshold):
                for i in range(freq_map[key]):
                    return_list.append(key)
        return return_list
    souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
    threshold1 = 3
    print(declutter(souvenirs1, threshold1))
    souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
    threshold = 2
    print(declutter(souvenirs2, threshold))

from collections import Counter
def problem4():
    def num_of_time_portals(portals, destination):
        portal_map = Counter(portals)
        running_total = 0
        for portal in portals:
            if (destination.replace(portal, '', 1) in portal_map and portal + destination.replace(portal, '', 1) == destination):
                running_total += max(1, portal_map[portal]-1)
        return running_total
    portals1 = ["777", "7", "77", "77"]
    destination1 = "7777"
    portals2 = ["123", "4", "12", "34"]
    destination2 = "1234"
    portals3 = ["1", "1", "1"]
    destination3 = "11"

    print(num_of_time_portals(portals1, destination1))
    print(num_of_time_portals(portals2, destination2))
    print(num_of_time_portals(portals3, destination3))
problem4()