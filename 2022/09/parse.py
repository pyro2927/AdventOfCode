spots = []
rope = []

for _ in range(10):
  rope.append([0,0])

# Never call on head
def determine_move(knot):
  h = rope[knot - 1]
  t = rope[knot]
  # determine if we need to move diagonal
  move_diag = (abs(h[0] - t[0]) + abs(h[1] - t[1])) > 2
  if move_diag:
    offset = 0
  else:
    offset = 1
  # make the tail follow
  if t[0] < h[0] - offset:
    t[0] += 1
  elif t[0] > h[0] + offset:
    t[0] -= 1

  if t[1] < h[1] - offset:
    t[1] += 1
  elif t[1] > h[1] + offset:
    t[1] -= 1

def move_head(direction):
  head = rope[0]
  match direction:
    case "R":
      head[1] += 1
    case "L":
      head[1] -= 1
    case "U":
      head[0] += 1
    case "D":
      head[0] -= 1

  for i in range(1,10):
    determine_move(i)

  tail = rope[9]
  spots.append((tail[0], tail[1]))
    

with open('input.txt', 'r') as file:
  for line in file:
    direction, count = line.strip().split(" ")
    for _ in range(int(count)):
      move_head(direction)

# Make this a set to uniq
print(len(set(spots)))
