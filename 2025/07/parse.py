from collections import defaultdict

file_path = "input.txt"

password = 0

ts = defaultdict(int)

with open(file_path, 'r') as file:
  for line in file:
    nt = defaultdict(int)
    c = list(line.strip())
    if len(ts) == 0:
      ts[c.index('S')] += 1
      continue

    for k,v in ts.items():
      if c[k] == '^': # split
        nt[(k - 1)] += v
        nt[(k + 1)] += v
        password += 1
      else:
        nt[k] += v

    ts = nt
    #print(f"{sum(ts.values()):03d} ", end='')
    #print(''.join([str(nt[i] % 10) if i in nt else c[i] for i in range(0,15)])) # debug

print("Part 1", password)

print("Part 2", sum(ts.values()))
