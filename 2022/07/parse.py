class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.directories = {}
    self.files = {}
    self.parent = parent

  def add_subdirectory(self, name):
    self.directories[name] = Directory(name, self)

  def child_dir(self, name):
    return self.directories[name]

  def children(self):
    return self.directories.values()

  def add_file(self, filename, size):
    self.files[filename] = size

  def size(self):
    dir_sizes = 0
    for child_dir in self.directories.values():
      dir_sizes += child_dir.size()
    return sum(self.files.values()) + dir_sizes

root = Directory("/")
cur_dir = root

def parse_command(command_line):
  global cur_dir
  _, *command = command_line.split(" ")

  if command[0] == 'ls':
    return
  elif command[1] == '/':
    # Special-case our first command
    print("Starting...")
  elif command[0] == 'cd':
    if command[1] == '..':
      cur_dir = cur_dir.parent
    else:
      cur_dir = cur_dir.child_dir(command[1])

def process():
  with open('input.txt', 'r') as file:
    for line in file:
      line = line.strip()
      if line[0] == '$':
        parse_command(line)
      elif line[0:3] == "dir":
        cur_dir.add_subdirectory(line.split(" ")[1])
      else:
        size, filename = line.split(" ")
        cur_dir.add_file(filename, int(size))

def sum_dir_sizes_under(cutoff_size):
  total = 0
  dirs = [root]
  while len(dirs) > 0:
    d = dirs.pop()

    if d.size() <= cutoff_size:
      total += d.size()

    # check all our children
    dirs.extend(d.children())

  print(total)
    
def free_space(total, needed):
  m = root.size()
  unused = total - m
  dirs = [root]
  print("Root size: " + str(m))
  while len(dirs) > 0:
    d = dirs.pop()
    if unused + d.size() > needed:
      m = min(d.size(), m)
    # check all our children
    dirs.extend(d.children())

  print(m)

if __name__ == "__main__":
  process()
  sum_dir_sizes_under(100000)
  free_space(70000000, 30000000)