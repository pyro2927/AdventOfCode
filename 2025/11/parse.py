from collections import defaultdict

file_path = "input.txt"
mesh = defaultdict(set)
traversed = {}

with open(file_path, 'r') as file:
  for line in file:
    s = line.strip().split(' ')      
    node = s[0][:-1]
    for k in s[1:]:
      mesh[node].add(k)
      
def tick(node, end):
  if node == end:
    return 1
  elif node == "out":
    return 0
  elif len(mesh[node]) == 0:
    return 0
  elif node in traversed:
    return traversed[node]

  traversed[node] = sum(map(lambda x: tick(x, end), mesh[node]))
  return traversed[node]

step1 = tick("svr", "fft")
traversed.clear()
step2 = tick("fft", "dac")
traversed.clear()
step3 = tick("dac", "out")

print(step1 * step2 * step3)