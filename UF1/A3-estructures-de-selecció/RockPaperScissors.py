try:
    RPS = input().split()
    if int(RPS[0]) in [1, 2, 3] and int(RPS[1]) in [1, 2, 3]:
        if int(RPS[0]) == int(RPS[1]): print("Empat")
        elif int(RPS[0]) < int(RPS[1]): print("Guanya el segon")
        else: print("Guanya el primer")
except ValueError or IndexError: print("Fica valors numérics vàlids")