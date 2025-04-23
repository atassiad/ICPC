def problem1():
    def is_mutual(celebrities):
        node_len = len(celebrities)
        for i in range(node_len):
            for j in range(i):
                if (i != j and celebrities[i][j] == 1):
                    if (celebrities[j][i] != 1):
                        return False
        
        return True
    celebrities1 = [
                    [0, 1, 1, 0],
                    [1, 0, 1, 0],
                    [1, 1, 0, 1],
                    [0, 0, 1, 0]]

    celebrities2 = [
                    [0, 1, 1, 0],
                    [1, 0, 0, 0],
                    [1, 1, 0, 1],
                    [0, 0, 0, 0]]

    print(is_mutual(celebrities1))
    print(is_mutual(celebrities2))

# while were checking all of them, if we find a new neighbor expand node[i][j]

def problem2():
    def get_adj_matrix(clients):
        #go through each celeb assign distinct value, expand adj matrix for those values [i][j]

        celeb_map = dict()
        adj_matrix = [[0]]
        celeb_map[clients[0][0]] = 0
        counter = 0
        for pair in clients:
            celeb_1 = pair[0]
            celeb_2 = pair[1]
            if celeb_1 not in celeb_map:
                counter += 1
                expand_matrix(adj_matrix)
                celeb_map[celeb_1] = counter
            if celeb_2 not in celeb_map:
                counter += 1
                expand_matrix(adj_matrix)
                celeb_map[celeb_2] = counter
            adj_matrix[celeb_map[celeb_1]][celeb_map[celeb_2]] = 1
            adj_matrix[celeb_map[celeb_2]][celeb_map[celeb_1]] = 1  
        return celeb_map, adj_matrix
    
    #expand matrix fun, increase dimensions by 1 on each side
    def expand_matrix(matrix):
        for i in range(len(matrix[0])):
            matrix[i].append(0)
        matrix.append(len(matrix[0]) * [0])
        return matrix

    clients = [
                ["Yalitza Aparicio", "Julio Torres"], 
                ["Julio Torres", "Fred Armisen"], 
                ["Bowen Yang", "Julio Torres"],
                ["Bowen Yang", "Margaret Cho"],
                ["Margaret Cho", "Ali Wong"],
                ["Ali Wong", "Fred Armisen"], 
                ["Ali Wong", "Bowen Yang"]]

    id_map, adj_matrix = get_adj_matrix(clients)
    print(id_map)
    print(adj_matrix)

def problem3(): #wrong
    def identify_celebrity(trust, n):
        celeb_candidate = set()
        not_celeb = set()

        for pair in trust:
            num1 = pair[0]
            num2 = pair[1]
            if num1 not in not_celeb:
                not_celeb.add(num1)
            if num1 in celeb_candidate:
                celeb_candidate.discard(num1)
            if num2 not in not_celeb:
                celeb_candidate.add(num2)
        
        if celeb_candidate:
            return list(celeb_candidate)[0]
        return -1
    trust1 = [[1,2]]
    trust2 = [[1,3],[2,3]]
    trust3 = [[1,3],[2,3],[3,1]]

    print(identify_celebrity(trust1, 2))
    print(identify_celebrity(trust2, 3))
    print(identify_celebrity(trust3, 3))
problem3()