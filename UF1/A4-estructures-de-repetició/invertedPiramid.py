floors = int(input())
aux = 0
for x in range(floors,0,-1):
    for z in range(aux):
        print(end=" ")
    for y in range(floors):
        print("# ", end = "")
    aux += 1
    floors -= 1
    print("\n", end = "")