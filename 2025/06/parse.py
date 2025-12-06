from operator import add, mul
from functools import reduce

file_path = "input.txt"

password = 0
grid = []
lines = []

with open(file_path, 'r') as file:
  for line in file:
    grid.append(line.strip().split())
    lines.append(list(line.rstrip("\n"))) # need raw for part 2

operators = grid.pop()

# part 1
for i in range(0, len(operators)):
  numbers = map(lambda x: int(x.__getitem__(i)), (r for r in grid))
  op = add if operators[i] == '+' else mul
  password += reduce(op, numbers)

print("Part 1", password)

# part 2
password = 0

# matrix rotate, lazily
lines = list(zip(*lines))[::-1]
lines = list(zip(*lines))[::-1]
lines = list(zip(*lines))[::-1]

op = add

temp = 0

# putchyanamedownflipitandreverseit
def missy_elliott(chars):
  return int(''.join(reversed(list(filter(lambda x: x.strip(), chars)))))

for l in lines:
  if l[0] in ('+', '*'):
    op = add if l[0] == '+' else mul
    password += temp
    temp = missy_elliott(l[1:])
  elif len(''.join(l).strip()) > 0:
    temp = op(temp, missy_elliott(l))

password += temp
print("Part 2", password)