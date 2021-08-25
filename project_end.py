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


def playing(player):
    graph = image()

    with open("./archivos/data.txt", "r") as f:
        word = f.readlines()[random.randint(1, 171)]
        word = word.strip()
    word_clave = ["_" for i in range(len(word))]
    lives = 0
    while lives <= 6:
        win = False
        os.system("clear")
        print(f"HOLA {player}, TE ESTAS JUGANDO LA VIDA")
        print(graph[lives])
        print("  ¿Adivinarás la palabra?")
        print("\t"+"".join(word_clave))
        letter = input("\nIngrese un letra: ")
        letter = letter.lower()
        
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
        print("FELICIDADES GANASTE")
        print(f"\nLa palabra era {word}")
    else:
        print("MORISTE AHORACADO ....")
        print(f"\nLa palabra era {word}")
    

def run():
    introduction()
    player = input("\nIngrese su alias: ")
    playing(player)



if __name__=='__main__':
    run()