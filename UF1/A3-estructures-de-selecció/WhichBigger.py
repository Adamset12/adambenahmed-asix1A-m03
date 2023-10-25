try:
    Numeros = input().split()
    print(max(int(Numeros[0]), int(Numeros[1])))
except ValueError:
    print("Fica valors numérics")