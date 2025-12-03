file_path = "input.txt"

# part 1
password = 0
with open(file_path, 'r') as file:
  for line in file:
    chars = list(line.strip())
    max_num = max([int(x) for x in chars[:-1]])
    index = chars.index(str(max_num))
    second_max = max([int(x) for x in chars[index+1:]])
    password += (max_num * 10 + second_max)

print(password)

# part 2
password = 0
with open(file_path, 'r') as file:
  for line in file:
    chars = list(line.strip())
    temp_total = 0 
    next_index = 0
    for i in range(0, 12):
      temp_total *= 10
      temp_chars = chars[next_index:-(11 - i)]
      if i == 11:
        temp_chars = chars[next_index:]
      max_num = max([int(x) for x in temp_chars])
      next_index += temp_chars.index(str(max_num)) + 1
      temp_total += max_num

    password += temp_total

print(password)
