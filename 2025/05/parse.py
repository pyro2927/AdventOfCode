file_path = "input.txt"

password = 0
ranges = []

# part 1

with open(file_path, 'r') as file:
  for line in file:
    stripped = line.strip()
    if '-' in stripped:
      first, last = map(int, stripped.split('-'))
      ranges.append((first, last))
    elif len(stripped) > 0:
      for r in ranges:
        i = int(stripped)
        if r[0] <= i and i <= r[1]:
          password += 1
          break

print(password)

# part 2
sorted_ranges = sorted(ranges, key=lambda x:x[0])

compressed_ranges = []
compressed_ranges.append(sorted_ranges.pop(0))

# compress
for r in sorted_ranges:
  last = compressed_ranges[-1]
  if r[0] <= last[1]: # see if we're within
    compressed_ranges[-1] = (last[0], max(r[1], last[1]))
  else:
    compressed_ranges.append(r)
      
fresh = len(compressed_ranges)

for r in compressed_ranges:
  fresh += (r[1] - r[0])

print(fresh)