cabells = input()
ulls = input()
nas = input()
boca = input()

match cabells.lower():
    case "arrissats": print("@@@@@")
    case "llisos": print("VVVVV")
    case "pentinats": print("XXXXX")
    case _: print("Valor de cabells no vàlid")
match ulls.lower():
    case "aclucats": print(".-.-.")
    case "rodons": print(".o-o.")
    case "estrellats": print(".*-*.")
    case _: print("Valor de ulls no vàlid")
match nas.lower():
    case "aixafat": print("..0..")
    case "arromangat": print("..C..")
    case "agilenc": print("..V..")
    case _: print("Valor de nas no vàlid")
match boca.lower():
    case "normal": print(".===.")
    case "bigoti": print(".∼∼∼.")
    case "dents-sortides": print(".www.")
    case _: print("Valor de boca no vàlid")
