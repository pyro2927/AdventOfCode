def set_from_string(in_val):
  i, j = in_val.split("-")
  # need to +1 because range is exclusive end
  return set([*range(int(i), int(j) + 1)])

contained = 0
overlap = 0

with open('input.txt', 'r') as file:
  for line in file:
    line = line.strip()
    first, second = line.split(",")
    first_set = set_from_string(first)
    second_set = set_from_string(second)

    if first_set.issubset(second_set) or second_set.issubset(first_set):
      contained += 1
      overlap += 1
    elif len(list(first_set & second_set)) > 0:
      overlap += 1

print(contained)
print(overlap)