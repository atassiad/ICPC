def question1():
    def filter_sustainable_brands(brands, criterion):
        return [brand["name"] for brand in brands if criterion in brand["criteria"]]

    brands = [
        {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
        {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
        {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
        {"name": "TrendyStyle", "criteria": ["trendy designs"]}
    ]

    brands_2 = [
        {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
        {"name": "FastStyle", "criteria": ["mass production"]},
        {"name": "NatureWear", "criteria": ["eco-friendly"]},
        {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
    ]

    brands_3 = [
        {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
        {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
        {"name": "FastCloth", "criteria": ["cheap production"]}
    ]

    print(filter_sustainable_brands(brands, "eco-friendly"))
    print(filter_sustainable_brands(brands_2, "ethical labor"))
    print(filter_sustainable_brands(brands_3, "carbon-neutral"))

def question2():
    def count_material_usage(brands):
        return_dict = dict()

        for brand in brands:
            for material in brand["materials"]:
                if material in return_dict:
                    return_dict[material] += 1
                else:
                    return_dict[material] = 1
        
        return return_dict
    brands = [
        {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
        {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
        {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
    ]

    brands_2 = [
        {"name": "NatureWear", "materials": ["hemp", "linen"]},
        {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
        {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
    ]

    brands_3 = [
        {"name": "OrganicThreads", "materials": ["organic cotton"]},
        {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
        {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
    ]

    print(count_material_usage(brands))
    print(count_material_usage(brands_2))
    print(count_material_usage(brands_3))

def problem3():
    def find_trending_materials(brands):
        return_dict = dict()

        for brand in brands:
            for material in brand["materials"]:
                if material in return_dict:
                    return_dict[material] += 1
                else:
                    return_dict[material] = 1

        return_list = []
        for material in return_dict:
            if (return_dict[material] > 1):
                return_list.append(material)
            
        return return_list
            
    brands = [
        {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
        {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
        {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
    ]

    brands_2 = [
        {"name": "NatureWear", "materials": ["hemp", "linen"]},
        {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
        {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
    ]

    brands_3 = [
        {"name": "OrganicThreads", "materials": ["organic cotton"]},
        {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
        {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
    ]

    print(find_trending_materials(brands))
    print(find_trending_materials(brands_2))
    print(find_trending_materials(brands_3))

def problem4():
    def find_best_fabric_pair(fabrics, budget):
        fabrics = sorted(fabrics, key=lambda x: x[1])
        i = 0
        j = len(fabrics)-1

        difference = fabrics[i][1] + fabrics[j][1] - budget
        while (i < j):
            newdifference = fabrics[i][1] + fabrics[j][1] - budget
            if (abs(newdifference) > abs(difference)):
                break
            if (newdifference > 0):
                difference = newdifference
                j -= 1
            elif (newdifference < 0):
                difference = newdifference
                i += 1
            else:
                break
        
        return [fabrics[i][0], fabrics[j][0]]
    
    fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
    fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
    fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

    print(find_best_fabric_pair(fabrics, 45))
    print(find_best_fabric_pair(fabrics_2, 70))
    print(find_best_fabric_pair(fabrics_3, 60))

from collections import deque

def problem5():
    def organize_fabrics(fabrics):
        fabrics = sorted(fabrics, key= lambda x: x[1])

        return_list = deque()

        for fabric in fabrics:
            return_list.appendleft(fabric[0])
        
        return return_list
    fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
    fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
    fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

    print(organize_fabrics(fabrics))
    print(organize_fabrics(fabrics_2))
    print(organize_fabrics(fabrics_3))

def problem7():
    def calculate_fabric_waste(items, fabric_rolls):
        rolling_sum = 0
        for item, roll in zip(items, fabric_rolls):
            rolling_sum += roll - item[1]
        return rolling_sum
    items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
    fabric_rolls1 = [5, 5, 5]

    items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
    fabric_rolls2 = [4, 4, 4]

    items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
    fabric_rolls3 = [7, 5, 5]

    print(calculate_fabric_waste(items, fabric_rolls1))
    print(calculate_fabric_waste(items_2, fabric_rolls2))
    print(calculate_fabric_waste(items_3, fabric_rolls3))

problem7()