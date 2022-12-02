# them A, B, C
# me   X, Y, Z
# Part 2
# X Lose
# Y Draw
# Z Win
def round_points(them, me):
  shift = 0
  outcome_points = 3
  if me == 'X':
    shift = -1
    outcome_points = 0
  elif me == 'Z':
    shift = 1
    outcome_points = 6

  return ((ord(them) - 65 + shift) % 3) + 1 + outcome_points
    


score = 0

with open('input.txt', 'r') as file:
  for line in file:
    them, me = line.strip().split(" ")
    score += round_points(them, me)

print(score)