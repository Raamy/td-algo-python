for i in range(4):
    print(i)
i = 4
print("-----")
for i in range(4, 8):
    print(i)
print("-----")
for i in range(2, 10, 2):
    print(i)

print("-----")
chose = [0, 1, 2, 3, 4, 5]

if chose.count(4) > 0:
    print("4 est un élément du tableau.")
else:
    print("4 n'est pas un élément du tableau.")
if chose.count(5) > 0:
    print("5 est un élément du tableau.")
else:
    print("5 n'est pas un élément du tableau.")
if chose.count(6) > 0:
    print("6 est un élément du tableau.")
else:
    print("6 n'est pas un élément du tableau.")
