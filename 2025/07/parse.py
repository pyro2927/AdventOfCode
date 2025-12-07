file_path = "input.txt"

password = 0

ts = set()

with open(file_path, 'r') as file:
  for line in file:
    nt = set()
    c = list(line.strip())
    if len(ts) == 0:
      ts.add(c.index('S'))

    for t in ts:
      if c[t] == '^': # split
        nt.add(t - 1)
        nt.add(t + 1)
        password += 1
      else:
        nt.add(t)
        
    ts = nt

print(password)
