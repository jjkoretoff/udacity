
# goal is to take a list of numbers, order them, then take the absolute
# value of those numbers and reorder them

w = [1, -2, 3, -4, 5, -6, 7, -8, 9]

x = sorted(w, key = int)

print x

y = map(abs, x)

z = sorted(y, key = int)

print z

