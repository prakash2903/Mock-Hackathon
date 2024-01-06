
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

if __name__ == '__main__':

  with open('C:/21PT17/Student Handout/Input data/level1a.json') as f:
    data = json.load(f)

  output = create_delivery_slots(data)

  with open('level1a_output.json', 'w') as f: 
    json.dump(output, f)

