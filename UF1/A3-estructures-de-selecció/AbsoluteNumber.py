try:
    nmb = int(input())
    if nmb < 0: nmb *= -1
    print(nmb)
except ValueError:
    print("Fica valors numérics")
