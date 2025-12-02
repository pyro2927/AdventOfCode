file_path = "input.txt"

password = 0
with open(file_path, 'r') as file:
  for line in file:
    for idset in line.strip().split(','):
      first, last = idset.split('-')
      for product in range(int(first), int(last) + 1): # range is exclusive of stop
        product_string = str(product)
        half = int(len(product_string) / 2)
        if product_string[0:half] == product_string[half:]:
          password += product

print(password)