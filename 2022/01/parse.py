m = 0
local = 0

with open('input.txt', 'r') as file:
  for line in file:
    if len(line.strip()) == 0:
      m = max(m, local)
      local = 0
    else:
      local += int(line.strip())
    
print(m)