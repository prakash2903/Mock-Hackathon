import json


def solve(data):
    start_dist = data['restaurants']['r0']['neighbourhood_distance']
    all_dists = {'r0': start_dist}
    dicti = {}

    for i in range(20):
        key = 'n' + str(i)
        dists = data['neighbourhoods'][key]['distances']
        all_dists[key] = dists

    path = []
    visited = []

    find_min_dist(path, visited, all_dists['r0'], dicti)
    
    for i in range(1, 21):
        if i == 1:
            find_min_dist(path, visited, all_dists['n0'], dicti)
        else:
            last_node = visited[-1]
            find_min_dist(path, visited, all_dists['n' + str(last_node)], dicti)

    routes = {}
    total_dist = sum(path[-2::-1])

    for i in range(len(path)-1):
        key = 'n' + str(visited[i])
        routes[key] = path[i]

    print(routes)

    converted_path = []

    for key in routes:
        converted_path.append(key)
    
    converted_path = ['r0'] + converted_path + ['r0']
    converted_output = {"v0": {"path": converted_path}}

    with open('output_0.json', 'w') as f:
        json.dump(converted_output, f)

    return converted_output

def find_min_dist(path, visited, distances, dicti):
    min_dist = float('inf')
    next_node = -1

    for i, dist in enumerate(distances):
        if dist != 0 and i not in visited:
            if dist < min_dist:
                next_node = i 
                min_dist = dist
    path.append(min_dist)
    visited.append(next_node)
    dicti[tuple(visited)] = min_dist
    

with open("C:/21PT17/Student Handout/Input data/level0.json") as f:
    data = json.load(f)
output = solve(data)

