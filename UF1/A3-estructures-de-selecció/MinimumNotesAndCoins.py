import decimal
money = float(input())

values = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
efectivo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


while money > 0:
    if money - 500 >= 0:
        money -= 500
        efectivo[0] += 1
    elif money - 200 >= 0:
        money -= 200
        efectivo[1] += 1
    elif money - 100 >= 0:
        money -= 100
        efectivo[2] += 1
    elif money - 50 >= 0:
        money -= 50
        efectivo[3] += 1
    elif money - 20 >= 0:
        money -= 20
        efectivo[4] += 1
    elif money - 10 >= 0:
        money -= 10
        efectivo[5] += 1
    elif money - 5 >= 0:
        money -= 5
        efectivo[6] += 1
    elif money - 2 >= 0:
        money -= 2
        efectivo[7] += 1
    elif money - 1 >= 0:
        money -= 1
        efectivo[8] += 1
    elif money - Decimal(0.50) >= 0:
        money -= Decimal(0.50)
        efectivo[9] += 1
    elif money - decimal(0.20) >= 0:
        money -= decimal(0.20)
        efectivo[10] += 1
    elif money - decimal(0.10) >= 0:
        money -= decimal(0.10)
        efectivo[11] += 1
    elif money - decimal(0.05) >= 0:
        money -= decimal(0.05)
        efectivo[12] += 1
    elif money - decimal(0.02) >= 0:
        money -= decimal(0.02)
        efectivo[13] += 1
    elif money - decimal(0.01) >= 0:
        money -= decimal(0.01)
        efectivo[14] += 1

print(efectivo[0])
print(efectivo[1])
print(efectivo[2])
print(efectivo[3])
print(efectivo[4])
print(efectivo[5])
print(efectivo[6])
print(efectivo[7])
print(efectivo[8])
print(efectivo[9])
print(efectivo[10])
print(efectivo[11])
print(efectivo[12])
print(efectivo[13])
print(efectivo[14])


