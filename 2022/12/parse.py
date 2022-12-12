
file = open('input.txt', 'r')
lines = file.readlines()

grid = []
tocheck = []
didcheck = []

START = "S"
start_pos = [0,0]
END = "E"
end_post = (0,0)

def letter_at(pos):
  return grid[pos[0]][pos[1]]

def scan(pos, steps=0):
  current = letter_at(pos)
  if current == START:
    upto = 'b'
  else:
    upto = chr(ord(current) + 1)

  adjacents = []
  for t in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    new_x = pos[0] + t[0]
    new_y = pos[1] + t[1]
    if new_x > 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
      new_pos = [new_x, new_y]
      if letter_at(new_pos) <= upto:
        adjacents.append([new_x, new_y])

  return adjacents


# build our grid and determine start/end
for l in lines:
  row = list(l.strip())
  if START in row:
    start_pos = [len(grid), row.index(START)]
  if END in row:
    end_pos = [len(grid), row.index(END)]
  grid.append(row)

tocheck.append((start_pos, 0))
didcheck.append(start_pos)

def process():
  while len(tocheck) > 0:
    pos, steps = tocheck.pop(0)
    nexts = scan(pos, steps)
    for n in nexts:
      if letter_at(n) == END:
        print("FOUND IT!")
        print(steps + 1)
        return
      # make sure we don't backtrack
      if n not in didcheck:
        tocheck.append((n, steps+1))
    didcheck.extend(nexts) # make sure we store everywhere we've been

process()
