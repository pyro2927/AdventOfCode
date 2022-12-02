# them A, B, C
# me   X, Y, Z
def round_points(them, me):
  # X is chr(88)
  shape_score = ord(me) - 87

  # draw
  if ord(them) == ord(me) - 23:
    return shape_score + 3

  # win
  if ord(me) - 24 == ord(them) or (me == 'X' and them == 'C'):
    return 6 + shape_score

  # else, we lost
  return shape_score
    


score = 0

with open('input.txt', 'r') as file:
  for line in file:
    them, me = line.strip().split(" ")
    score += round_points(them, me)

print(score)