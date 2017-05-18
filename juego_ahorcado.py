import os
import random
import sys

word_list = [
    'rails',
    'python',
    'django',
    'react',
    'ruby',
    'angular'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def draw(incorrecto, correcto, secret_word):
    clear()
    
    print('Oportunidades: {}/7'.format(len(incorrecto)))
    print('')
    
    for letter in incorrecto:
        print(letter, end=' ')
    print('\n\n')
    
    for letter in secret_word:
        if letter in correcto:
            print(letter, end='')
        else:
            print('_', end='')
        # lo que hace end es dejar un espacio o lo que le pasemos despues de la lo que imprimimos
        
    print('')
        
def get_guess(incorrecto, correcto):
    while True:
        adivina = input('Adivina una letra: ').lower()
        
        if len(adivina) != 1:
            print('Solo puedes ingresar una letra.')
        elif adivina in incorrecto or adivina in correcto:
            print('ya has acertado esa letra')
        elif not adivina.isalpha(): # esto evalua que lo que hayamos ingresado sea una letra y no otro caracter
            print('Solo puedes adivinar con letras')
        else:
            return adivina
            
def welcome():
    clear()
    start = input('Presiona Enter/Return para empezar el juego, o Q para salir')
    if start.lower() == 'q':
        print('Bye!')
        sys.exit()
    else:
        return True

def play(done):
    clear()
    secret_word = random.choice(word_list)
    incorrecto = []
    correcto = []
    
    while True:
        draw(incorrecto, correcto, secret_word)
        adivina = get_guess(incorrecto, correcto)
        
        if adivina in secret_word:
            correcto.append(adivina)
            found = True
            for letter in secret_word:
                if letter not in correcto:
                    found = False
            if found:
                print('Ganaste!!')
                print('La palabra secreta era: {}'.format(secret_word))
                done = True
        else:
            incorrecto.append(adivina)
            if len(incorrecto) == 7:
                draw(incorrecto, correcto, secret_word)
                print('Perdiste!!')
                print('La palabra secreta era: {}'.format(secret_word))
                done = True
                
        if done:
            play_again = input('Jugar denuevo? (S/n)').lower()
            if play_again != 'n':
                return play(done = False)
            else:
                sys.exit()
        
print('Bienvenido a Adivina la Palabra!!!')

done = False

while True:
    clear()
    welcome()
    play(done)
        
    
