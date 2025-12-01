file_path = "input.txt"

place = 50
password = 0
try:
  with open(file_path, 'r') as file:
    for line in file:
      start = place
      direction = line[0]
      num = int(line[1:])
      if direction == 'L':
        place -= num
      else:
        place += num

      mod = abs(int(place / 100))

      if place < 0 and start != 0:
        password += 1

      print("Place ",place)
      place %= 100
      print("Place ",place)

      if mod > 0:
        password += mod
      elif place == 0:
        password += 1

      print("Password ",password)
      

except FileNotFoundError:
  print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
  print(f"An error occurred: {e}")

print(password)