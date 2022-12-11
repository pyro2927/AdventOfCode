x = 1
cycle = 0
signals = []

screen = []
row = []

cycles = [20, 60, 100, 140, 180, 220]

def check():
  if cycle in cycles:
    signals.append(x * (cycle + 1))
    print(x)

def genpixel():
  global row
  global screen
  if len(row) in [x-1, x, x+1]:
    row.append("#")
  else:
    row.append(".")

  if len(row) == 40:
    screen.append(row)
    row = []

with open('input.txt', 'r') as file:
  for line in file:
    genpixel()
    things = line.strip().split(" ")
    cycle += 1
    check()

    if len(things) > 1:
      genpixel()
      x += int(things[1]) 
      cycle += 1
      check()

print(sum(signals))

for r in screen:
  print("".join(r))