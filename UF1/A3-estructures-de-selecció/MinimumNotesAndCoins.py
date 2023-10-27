
try:
    import decimal
    money = decimal.Decimal(input())

    values = [
        decimal.Decimal('500'),
        decimal.Decimal('200'),
        decimal.Decimal('100'),
        decimal.Decimal('50'),
        decimal.Decimal('20'),
        decimal.Decimal('10'),
        decimal.Decimal('5'),
        decimal.Decimal('2'),
        decimal.Decimal('1'),
        decimal.Decimal('0.50'),
        decimal.Decimal('0.20'),
        decimal.Decimal('0.10'),
        decimal.Decimal('0.05'),
        decimal.Decimal('0.02'),
        decimal.Decimal('0.01')
    ]
    efectivo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i in range(len(values)):
        while money >= values[i]:
            money -= values[i]
            efectivo[i] += 1
        i += 1
    i = 0
    while i in range(len(efectivo)):
        if efectivo[i] != 0:
            if int(values[i]) > 2 and efectivo[i] > 1: print(str(efectivo[i]) + " bitllets de " + str(values[i]) + "€")
            elif int(values[i]) > 2 and efectivo[i] == 1: print(str(efectivo[i]) + " bitllet de " + str(values[i]) + "€")
            elif int(values[i]) > 0.50 and efectivo[i] > 1: print(str(efectivo[i]) + " monedes de " + str(values[i]) + "€")
            elif int(values[i]) > 0.50 and efectivo[i] == 1: print(str(efectivo[i]) + " moneda de " + str(values[i]) + "€")
            elif efectivo[i] > 1: print(str(efectivo[i]) + " monedes de " + str(values[i]) + " cèntims")
            else: print(str(efectivo[i]) + " moneda de " + str(values[i]) + " cèntims")
        i += 1
except ValueError or IndexError: print("Pon un valor vàlido")