floors = int(input())
floorsinverted = floors
aux = 0
for x in range(floorsinverted,0,-1):
    match floorsinverted:
        case value if value == floors: character = "⚪"
        case _: character = "#"
    for z in range(aux):
        print(end=" ")
    for y in range(floorsinverted):
        match y:
            case _ if floorsinverted == floors:
                character = "O"
            case 0:
                 character = "O"
            case _ if y == (floorsinverted - 1):
                character = "O"
            case _:
                character = "#"
        print(f"{character} ", end = "")
    aux += 1
    floorsinverted -= 1
    print("\n", end = "")
floorsright = floors
aux = floorsright - 2
columns = 1
for x in range((floorsright - 1)):
    for z in range(aux):
        print(end=" ")
    for y in range(columns + 1):
        match y:
            case _ if columns == (floors - 1):
                character = "O"
            case 0:
                character = "O"
            case _ if y == columns:
                character = "O"
            case _:
                character = "#"
        print(f"{character} ", end = "")
    columns += 1
    aux -= 1
    print("\n", end = "")