trees = []

with open('input.txt', 'r') as file:
  for line in file:
    row = [*line.strip()]
    trees.append(row)

height = len(trees)
width = len(trees[0])

# transpose a second grid for easier comparison
rotated = [[trees[j][i] for j in range(height)] for i in range(width)]

# edges are all visible
visible = (height * 2) + (width * 2) - 4

for i in range(1,width-1):
  row = trees[i]
  for j in range(1,height-1):
    tree = row[j]
    trow = rotated[j]
    # check to see if this is visible horizontally
       # left                    right
    if max(row[0:j]) < tree or max(row[j+1:width]) < tree:
      visible += 1
    # check to see if this is visible vertically using rotated
       # above                  # under
    elif max(trow[0:i]) < tree or max(trow[i+1:width]) < tree:
      visible += 1

      
print(visible)