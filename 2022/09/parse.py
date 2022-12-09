spots = []
h = [0,0]
t = [0,0]

# Won't work for real data due to range
def debug():
  for x in reversed(range(5)):
    for y in range(6):
      if h == [x,y]:
        print("H", end="")
      elif t == [x,y]:
        print("T", end="")
      elif (x,y) in spots:
        print("#", end="")
      else:
        print(".", end="")
    print("")
  print("")


def move_head(direction):
  global h
  global t

  match direction:
    case "R":
      h[1] += 1
    case "L":
      h[1] -= 1
    case "U":
      h[0] += 1
    case "D":
      h[0] -= 1

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

  spots.append((t[0], t[1]))
  # Uncomment to see each step
  #debug()
    

with open('input.txt', 'r') as file:
  for line in file:
    direction, count = line.strip().split(" ")
    for _ in range(int(count)):
      move_head(direction)

#debug()
# Make this a set to uniq
print(len(set(spots)))
