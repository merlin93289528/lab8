def count_x(id = 10):
    if id == 0:
        return 1
    else:
        return count_x(id - 1) + 2 * id

print(count_x())