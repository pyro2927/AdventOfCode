import ast

file = open('input.txt', 'r')
lines = file.readlines()
pairs = []

i = 0
while i < len(lines):
  left = ast.literal_eval(lines[i])
  right = ast.literal_eval(lines[i + 1])

  pairs.append((left, right))

  i +=3

# returns 1 if they're in the right order
# returns 0 if they're the "same" aka, continue
# returns -1 if they're in the wrong order

def compare(left, right):
  if type(left) != type(right):
    # type align
    if type(left) == int:
      return compare([left], right)
    else:
      return compare(left, [right])
  elif type(left) == int:
    # compare val
    if left == right:
      return 0
    elif left < right:
      return 1
    else:
      return -1
  elif type(left) == list:
    # loop
    for x in range(min(len(left), len(right))):
      val = compare(left[x], right[x])
      if val != 0:
        return val

    if len(right) < len(left):
      return -1
    elif len(right) == len(left):
      return 0
    else:
      return 1

  else:
    print("PROBLEM")


proper_order = []
for x in range(len(pairs)):
  pair = pairs[x]
  left = pair[0]
  right = pair[1]
  if compare(left, right) == 1:
    proper_order.append(x + 1)

print(proper_order)
print(sum(proper_order))