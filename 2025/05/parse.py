file_path = "input.txt"

password = 0
ranges = []

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