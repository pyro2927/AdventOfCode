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

# Find number of visible trees
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

def trees_visible(row, tree_index, direction = -1):
  score = 0
  tree = row[tree_index]
  t2_index = tree_index + direction

  while t2_index >= 0 and t2_index < len(row):
    score += 1
    # check for shorter
    if row[t2_index] < tree:
      t2_index += direction
    else:
      return score

  return score

# Find the highest scenic score
# score is visible trees each direction *
# edges have a scenic score of 0 so no point in calculating
max_scenic_score = 0
for i in range(1,height-1):
  row = trees[i]
  for j in range(1,width-1):
    tree = row[j]
    trow = rotated[j]

    scenic_score = trees_visible(row, j, -1) * trees_visible(row, j, 1) * \
                   trees_visible(trow, i, -1) * trees_visible(trow, i, 1)

    max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)