import random
import os


def introduction():
    print("""           BIENVENIDO AL JUEGO DE TU VIDA..jajaj
          ----------------------------------------
(Este es el proyecto final del curso de Python Intermedio)

INSTRUCCIONES: 
    Se asignara palabras aleatorias para que usted intente
    adivinarlas. Debera adivinar la palabra ingresando una
    unica letra por cada intento, debe adivinar la palabra
    antes de que se llegue a formar la figura del hombre
    por completo para ganar el juego. Buena Suerte""")

def image():
    DATA = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']
    return DATA

def input_letter(letters):
    while True:
        try:
            letter = input("\nIngrese una letra: ")
            if not letter.isalpha():
                raise ValueError("\nTienes que ingresar una letra..")
            letter = letter[0]
            letter = letter.lower()
            if letter in letters:
                raise ValueError("\nYa ingresaste esa letra, Ingrese otra")
            
            return letter
        except ValueError as ve:
            print(ve)


def run():
    introduction()
    player = input("\nIngrese su alias: ")
    
    graph = image()

    #OJO: Colocar el data.txt en una carpea archivos
    with open("./archivos/data.txt", "r") as f:
        word = f.readlines()[random.randint(1, 171)]
        word = word.strip()
    word_clave = ["_" for i in range(len(word))]

    lives = 0
    letter_enter = []
    while lives < 6:
        win = False
        os.system("clear")
        print(f"HOLA {player}, TE ESTAS JUGANDO LA VIDA")
        print(f"\n\t\tLives: {6-lives}")
        print(graph[lives])
        print("  ¿Adivinarás la palabra?")
        print("\t"+"".join(word_clave))
        print("\nLetras Ingresadas: "+" - ".join(letter_enter))
        letter = input_letter(letter_enter)
        letter_enter.append(letter)

        for x in range(len(word)):
            if letter == word[x]:
                word_clave[x] = word[x]
                win = True
        
        if not win:
            lives += 1
            win = False

        if word == "".join(word_clave):         
            win = True
            break
    if win:
        os.system("clear")
        print(f"HAS SALVADO TU VIDA {player}!!!")
        print(f"\n\t\tLives: {6-lives}")
        print(graph[lives])
        print(f'\t"{word}"')
        print("\nFelicitaciones y Adios...")
    else:
        os.system("clear")
        print(f"{player} LAMENTABLEMENTE TE AUTOAHORCARSTE :( !!!")
        print(f"\n\t\tLives: {6-lives}")
        print(graph[lives])
        print("\t"+"".join(word_clave))
        print("\nBuena suerte a la próxima...")
        print(f'\nLa palabra era "{word}"')

if __name__=='__main__':
    run()