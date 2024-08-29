def new_add_table(size):
  table = []
  for i in range(-size // 2 + 1, size // 2 + 1):
    row = []
    for j in range(-size // 2 + 1, size // 2 + 1):
      row.append(i + j)
    table.append(row)
  return table

size = 7

add_table = new_add_table(size)

for row in add_table:
  for num in row:
    print(f"{num:3}", end="")
  print()