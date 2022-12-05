ships = []

def setup():
  for x in range(9):
    ships.append([])

# Cargo ships are parsed top-down
def parse_cargo_ship_line(line):
  ship = 0
  for x in range(9):
    c = line[1 + (x*4)]
    if c != ' ':
      ships[x].insert(0, c)

# move 3 from 6 to 2
def move(instructions):
  _, num, _, f, _, t = instructions.split(" ")
  for _ in range(int(num)):
    ships[int(t)-1].append(ships[int(f)-1].pop())

def parse():
  with open('input.txt', 'r') as file:
    for line in file:
      if len(line.strip()) == 0:
        next
      if line[0] == '[':
        parse_cargo_ship_line(line)
      elif line[0] == ' ':
        next
      elif line[0] == 'm':
        move(line.strip())

if __name__ == '__main__':
  setup()
  parse()
  print("Tops")
  for x in range(len(ships)):
    print(ships[x][-1], end='')
