file_path = "input.txt"

# build grid
password = 0

og_grid = []
with open(file_path, 'r') as file:
  for line in file:
    chars = list(line.strip())
    og_grid.append(chars)

# iterate
y_size = len(og_grid)
x_size = len(og_grid[0]) # assume all rows are uniform width

def process(grid):
  removed = 0
  new_grid = []
  for y in range(0, y_size):
    new_row = []
    for x in range(0, x_size):
      # only check for paper rolls
      if grid[y][x] != '@':
        new_row.append('.')
        continue

      # scan adjacent
      adjacent = 0
      for check_y in range(max(y-1, 0), min(y+2, y_size)):
        for check_x in range(max(x-1, 0), min(x+2, x_size)):
          if check_y == y and check_x == x: # don't count ourselves
            continue
          elif grid[check_y][check_x] == '@':
            adjacent += 1
      if adjacent < 4:
        new_row.append('.')
        removed += 1
      else:
        new_row.append('@')
    new_grid.append(new_row)
  return removed, new_grid

removed, next_grid = process(og_grid)
print("Part 1", removed)
while removed != 0:
  password += removed
  removed, next_grid = process(next_grid)
  
print("Part 2", password)