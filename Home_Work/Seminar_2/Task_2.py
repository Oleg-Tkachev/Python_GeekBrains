
# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print("X | Y | Z | ¬(x∧y)∨z")
print("--------------------")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            sum = (int(not (x and y) or z))
            print(f'{x} | {y} | {z} |    {sum} ')


