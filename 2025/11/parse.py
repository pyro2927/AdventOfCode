from collections import defaultdict

file_path = "input.txt"
mesh = defaultdict(set)

with open(file_path, 'r') as file:
  for line in file:
    s = line.strip().split(' ')      
    node = s[0][:-1]
    for k in s[1:]:
      mesh[node].add(k)
      
def tick(node):
  if node == "out":
    return 1

  return sum(map(tick, mesh[node]))


print(tick("you"))