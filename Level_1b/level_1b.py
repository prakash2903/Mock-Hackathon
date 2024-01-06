'''

import json

def create_delivery_slots(data):
    capacity = data['vehicles']['v0']['capacity']
    orders = sorted([n['order_quantity'] for n in data['neighbourhoods'].values()], reverse=True)
    neighs = list(data['neighbourhoods'].keys())

    paths = {}
    for i in range(1, 21):
        path = ['r0']
        remaining_capacity = capacity

        for order in orders:
            for j, neigh in enumerate(neighs):
                if (data['neighbourhoods'][neigh]['order_quantity'] == order 
                    and order <= remaining_capacity 
                    and neigh not in path):
                    path.append(neigh)
                    remaining_capacity -= order
                    neighs.pop(j)
                    break

        if len(path) > 2:
            paths[f'path{i}'] = path + ['r0']

    return {'v0': paths}

def create_delivery_slots_level1b(data):
    capacity = data['vehicles']['v0']['capacity']
    orders = sorted([n['order_quantity'] for n in data['neighbourhoods'].values()], reverse=True)
    neighs = list(data['neighbourhoods'].keys())

    paths = {}
    for i in range(1, 21):
        path = ['r0']
        remaining_capacity = capacity

        for order in orders:
            for j, neigh in enumerate(neighs):
                if (data['neighbourhoods'][neigh]['order_quantity'] == order 
                    and order <= remaining_capacity 
                    and neigh not in path):
                    path.append(neigh)
                    remaining_capacity -= order
                    neighs.pop(j)
                    break

        if len(path) > 2:
            paths[f'path{i}'] = path + ['r0']

    # Additional code for Level 1b: Include Sivananda colony in the paths
    sivananda_paths = {}
    for path_key, path_value in paths.items():
        sivananda_path = path_value + ['s0']  # Assuming 's0' is the neighborhood in Sivananda colony
        sivananda_paths[path_key] = sivananda_path

    return {'v0': sivananda_paths}

if __name__ == '__main__':
    with open('C:/21PT17/Student Handout/Input data/level1b.json') as f:
        data = json.load(f)

    output = create_delivery_slots_level1b(data)

    with open('level1b_output.json', 'w') as f: 
        json.dump(output, f)

'''

import json

def create_delivery_slots(data):

  capacity = data['vehicles']['v0']['capacity'] # 1120

  orders = sorted([n['order_quantity'] for n in data['neighbourhoods'].values()], reverse=True)

  neighs = list(data['neighbourhoods'].keys())

  # Sort neighs by distance from depot
  start_dist = data['restaurants']['r0']['neighbourhood_distance']
  neighs.sort(key=lambda n: start_dist[int(n[1:])])

  paths = {}
  vehicles_needed = (sum(orders) // capacity) + 1

  for i in range(1, vehicles_needed+1):
    
    path = ['r0']
    remaining_capacity = capacity

    for order in orders:
        for j, neigh in enumerate(neighs):
            if (data['neighbourhoods'][neigh]['order_quantity'] == order 
                and order <= remaining_capacity 
                and neigh not in path):
                path.append(neigh)
                remaining_capacity -= order
                neighs.pop(j)
                break

    paths[f'path{i}'] = path + ['r0']

  return {'v0': paths}

if __name__ == '__main__':

  with open("C:/21PT17/Student Handout/Input data/level1b.json") as f:
    data = json.load(f)

  output = create_delivery_slots(data)

  with open('level1b_output.json', 'w') as f:
    json.dump(output, f)


