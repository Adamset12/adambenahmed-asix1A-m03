floors = int(input())
aux = floors
columns = 1
for x in range(floors):
    for z in range(aux):
        print(end=" ")
    for y in range(columns):
        print("# ", end = "")
    columns += 1
    aux -= 1
    print("\n", end = "")