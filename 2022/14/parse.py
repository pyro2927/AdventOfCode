file = open('input.txt', 'r')
lines = file.readlines()

ROCK=[]
SAND=[]
START=(500,0)

WIDTH=1000
HEIGHT=0

def fill_rock(start, end):
  global HEIGHT
  for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
    for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
      new_rock = (x, y)
      if new_rock not in ROCK:
        ROCK.append(new_rock)
        HEIGHT = max(HEIGHT, new_rock[1])

# read in our lines and determine abyss
def parse():
  for line in lines:
    pairs = line.strip().split(" -> ")
    rock_points = []
    for pair in pairs:
      x, y = pair.split(",")
      # cast as ints
      rock_points.append((int(x), int(y)))
    for i in range(1,len(rock_points)):
      fill_rock(rock_points[i-1], rock_points[i])

def space_open(point):
  if point in ROCK:
    return False
  elif point in SAND:
    return False

  return True

def move_down(point):
  # center, left, right
  new_points_in_order = [(point[0], point[1] + 1), (point[0] - 1, point[1] + 1), (point[0] + 1, point[1] + 1)]
  for p in new_points_in_order:
    # check if we're in the abyss
    if p[1] > HEIGHT:
      return False
    if space_open(p):
      return move_down(p)

  SAND.append(point)

  # make sure we stop if it goes all the way up
  if point == START:
    return False
  return point

# MOAR SAND
def tick_sand():
  # start one step down
  while True:
    if not move_down(START):
      print("Done")
      break

# draw our board
def draw():
  # TODO: determine better size
  for y in range(0, HEIGHT):
    for x in range(0, 1000):
      point = (x,y)
      if point == START:
        print("+", end='')
      elif point in ROCK:
        print("#", end='')
      elif point in SAND:
        print("o", end='')
      else:
        print(".", end='')
    print("")


parse()
# Star 2, add our floor
old_height = HEIGHT + 2
fill_rock((-1000, old_height), (1500, old_height))
tick_sand()
draw()
print(len(SAND))