from operator import add, mul, pow

file = open('input.txt', 'r')
lines = file.readlines()

monkeys = []

class Monkey:
  def __init__(self, lines):
    self.inspected_count = 0
    self.items = [int(i) for i in lines[0].strip().split(": ")[1].split(", ")]

    op_line = lines[1].strip().split(" ")
    # special handle pow 2
    if op_line[-1] == "old":
      self.op_func = pow
      self.op_val = 2
    else:
      self.op_val = int(op_line[-1])
      match op_line[-2]:
        case "*":
          self.op_func = mul
        case "+":
          self.op_func = add

    self.divisor = int(lines[2].strip().split(" ")[-1])
    self.truemonkey = int(lines[3].strip().split(" ")[-1])
    self.falsemonkey = int(lines[4].strip().split(" ")[-1])

  # returns the item and which monkey to throw it to
  def inspect_and_throw(self):
    self.inspected_count += 1
    item = self.items.pop(0)
    item = self.op_func(item, self.op_val)
    item = int(item / 3)
    return item, self.truemonkey if item % self.divisor == 0 else self.falsemonkey

  # receive an item from another monkey
  def receive(self, item):
    self.items.append(item)




i = 1

while i < len(lines):
  monkeys.append(Monkey(lines[i:i+5]))
  i += 7

for _ in range(20):
  for m in monkeys:
    while(len(m.items) > 0):
      item, mi = m.inspect_and_throw()
      monkeys[mi].receive(item)

c = [m.inspected_count for m in monkeys]
c.sort(reverse = True)
print(mul(*c[0:2]))