import string

total = 0
letters = list(string.ascii_letters)

with open('input.txt', 'r') as file:
  for line in file:
    line = line.strip()
    half = int(len(line)/2)
    first = line[0:half]
    second = line[half:len(line)]
    in_both = list(set(first) & set(second))
    for letter in in_both:
      total += (letters.index(letter) + 1)

print(total)
