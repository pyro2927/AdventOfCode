file_path = "input.txt"

password = 0
locations = []

def tick(state, end, button_sets, count):
  if state == end:
    return count
  elif len(button_sets) <= 0:
    return 99999999

  next_state_1 = list(state)  
  next_state_2 = list(state)  

  these_buttons = button_sets.pop(0)

  for b in these_buttons:
    next_state_1[b] ^= 1 # flip our switches

  return min(tick(next_state_1, end, list(button_sets), count + 1), tick(next_state_2, end, list(button_sets), count))


password = 0
with open(file_path, 'r') as file:
  for line in file:
    row = line.strip().split(' ')
    end_state = [True if x == '#' else False for x in row[0][1:-1]]
    joltage = row[-1]
    buttons = [list(map(int, x[1:-1].split(','))) for x in row[1:-1]]
    start = [False] * len(end_state)

    password += (tick(start, end_state, buttons, 0))

print(password)