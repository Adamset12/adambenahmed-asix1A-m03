"""
Jofre Aleman Serra, Adam Ben Ahmed, Axel Benitez
23/02/24
Projecte: L'usuari introdueix una frase i el programa ha de randomatitzar les paraules i escriure-les randomaritzades
mantenint la lletra inicial i final en la mateixa posició, i printar la frase amb les paraules randomitzades.
"""
# region ----- IMPORTS -----
import crazy_words
import data_source
# endregion
# region ----- FUNCIÓ DEL PROGRAMA PRINCIPAL -----
def main():
    CYAN = "\033[36m"
    RESET = "\033[0m"
    exec = True
    while exec:
        resultat = [""]
        print(CYAN+"MENÚ:\n     1. Introduir text per pantalla\n     2. Introduir URL\n     3. Fer pregunta a ChatGPT\n "
                   "    4. EN PROCÉS\n     5. SORTIR"+RESET)
        eleccio = int(input())
        match eleccio:
            case "1": frase = data_source.get_data__from_keyboard()
            case "2":
                    frase = data_source.get_data_from_server(input())
                    #https://clientes.api.greenborn.com.ar/public-random-word
            case "3":
                    frase = data_source.get_data_from_chatGPT(input())
            case "4": print("Tranquilo gormiti, pronto se prende heavy.")
            case "5":
                    exec = False
                    print("Dew")
            case _: print("Fica un numero valid.\nDato: Sabias que los profes (Javi) no viven en el cole? raro vrd?")
        if eleccio in [1, 2, 3]:
            frase, frase_per_operar = crazy_words.arreglar_frase(frase)
            crazy_words.recorrer_frase(frase_per_operar, resultat)
            crazy_words.imprimir_resultat(frase, resultat)
# endregion
# region ----- PROGRAMA PRINCIPAL -----
main()
# endregion