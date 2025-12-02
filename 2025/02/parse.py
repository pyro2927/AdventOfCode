file_path = "input.txt"

password = 0
with open(file_path, 'r') as file:
  for line in file:
    for idset in line.strip().split(','):
      first, last = idset.split('-')
      for product in range(int(first), int(last) + 1): # range is exclusive of stop
        product_string = str(product)
        for chunksize in range(1, int(len(product_string) / 2) + 1):
          # if it can't be evenly split, skip
          if len(product_string) % chunksize != 0:
            continue
          chunks = set([product_string[i:i + chunksize] for i in range(0, len(product_string), chunksize)]) 
          if len(chunks) == 1: # set() automatically strips duplicates
            password += product
            break
print(password)