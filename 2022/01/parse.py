m = 0
local = 0

elves = []

with open('input.txt', 'r') as file:
  for line in file:
    if len(line.strip()) == 0:
      elves.append(local)
      local = 0
    else:
      local += int(line.strip())

elves.sort(reverse=True)

print("Elf 1: {}".format(elves[0]))
print("Elfs 1-3: {}".format(sum(elves[0:3])))