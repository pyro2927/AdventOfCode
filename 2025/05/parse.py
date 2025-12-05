file_path = "input.txt"

password = 0
fresh = set()

with open(file_path, 'r') as file:
  for line in file:
    stripped = line.strip()
    if '-' in stripped:
      first, last = map(int, stripped.split('-'))
      fresh.update(list(range(first, last + 1)))
    elif len(stripped) > 0:
      if int(stripped) in fresh:
        password += 1

print(password)