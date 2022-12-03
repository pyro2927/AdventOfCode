import string

total = 0
letters = list(string.ascii_letters)

triplet = 0
badges = 0
# Potential badges for this group
potentials = letters

with open('input.txt', 'r') as file:
  for line in file:
    line = line.strip()
    # narrow down potential badges
    potentials = list(set(line) & set(potentials))
    triplet += 1

    if triplet == 3:
      if len(potentials) > 1:
        print("We have a problem")
      elif len(potentials) == 1:
        badges += letters.index(potentials[0]) + 1
        potentials = letters
        triplet = 0

    half = int(len(line)/2)
    first = line[0:half]
    second = line[half:len(line)]
    in_both = list(set(first) & set(second))
    for letter in in_both:
      total += (letters.index(letter) + 1)

print("Priority 1: " + str(total))
print("Badges 2: " + str(badges))
