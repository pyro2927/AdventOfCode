def parse(line, sop=4):
  line = list(line.strip())
  chunk = []
  for i in range(len(line)):
    chunk.append(line.pop(0))
    if len(chunk) > sop:
      chunk.pop(0)
      if len(set(chunk)) == sop:
        print("Uniques")
        print(chunk)
        print(i + 1)
        return
    

with open('input.txt', 'r') as file:
  for line in file:
    parse(line)
    parse(line, 14)