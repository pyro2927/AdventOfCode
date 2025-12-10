file_path = "input.txt"

password = 0
locations = []

with open(file_path, 'r') as file:
  for line in file:
    x, y = map(int, line.strip().split(','))
    locations.append((x, y))

lines = []
for i in range(0, len(locations)):
  l1 = locations[i]
  l2 = locations[(i+1) % len(locations)]

  # track lines, which are just flat rectangles
  lines.append((l1, l2))

rectangles = []
for l1 in locations:
  for l2 in locations:
    rectangles.append(tuple(sorted([l1, l2])))

def size(rec):
  return (abs(rec[0][0]-rec[1][0]) + 1) * (abs(rec[0][1]-rec[1][1]) + 1)

rectangles.sort(key=size, reverse=True)

print("Part 1", size(rectangles[0]))

def normalize(r):
  (x1, y1), (x2, y2) = r
  return ((min(x1, x2), min(y1, y2)),
          (max(x1, x2), max(y1, y2)))

def overlap(a, b):
    (ax1, ay1), (ax2, ay2) = normalize(a)
    (bx1, by1), (bx2, by2) = normalize(b)

    return not (ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2)

for r in rectangles:
  clear = True
  for l in lines:
    if overlap(r, l):
      clear = False
      break
  if clear:
    print("Part 2", size(r))
    print(r)
    break