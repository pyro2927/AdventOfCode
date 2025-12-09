from math import dist, prod

file_path = "input.txt"
password = 0
boxes = []
circuits = [] # nested sets
distances = {} # calculate them all once

with open(file_path, 'r') as file:
  for line in file:
    x, y, z = map(int, line.strip().split(','))
    boxes.append((x,y,z))

# sort em
for j1 in boxes:
  for j2 in boxes:
    if j1 == j2: # avoid dupes
      continue
    distances[dist(j1, j2)] = (j1, j2)

sorted_dist = sorted(distances.keys())

count = 0
for k in sorted_dist:
  j1, j2 = distances[k]
  found = []
  duplicate = False

  for c in circuits:
    if j1 in c and j2 in c:
      # we've made a circle
      duplicate = True
      break
    elif (j1 in c) or (j2 in c): # only one found
      found.append(c)

  if duplicate:
    continue
  elif len(found) == 1:
    found[0].add(j1)
    found[0].add(j2)
    print(j1[0] * j2[0])
  elif len(found) == 0:
    circuits.append({j1, j2})
  elif len(found) == 2: # we need to combine these for tracking
    found[0].update(found[1])
    circuits.remove(found[1])
    print(j1[0] * j2[0])
