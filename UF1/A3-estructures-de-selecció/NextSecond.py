try:
    hora = input().split()
    hora[2] = int(hora[2]) + 1
    hora[1] = int(hora[1])
    hora[0] = int(hora[0])
    if int(hora[2]) == 60:
        hora[2] = int(hora[2]) - 60
        hora[1] = int(hora[1]) + 1
    if int(hora[1]) == 60:
        hora[1] = int(hora[1]) - 60
        hora[0] = int(hora[0]) + 1
    if int(hora[0]) == 24:
        hora[0] = int(hora[0]) - 24
    print(f"{hora[0]:02d}:{hora[1]:02d}:{hora[2]:02d}")
except ValueError or IndexError: print("Posa valors vàlids")