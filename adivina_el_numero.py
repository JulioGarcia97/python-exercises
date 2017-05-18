import os
shopping_list = []

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

def show_help():
    clear_screen()
    print("Que queremos comprar en la tienda?")
    print("""
Ingresa 'DONE' para terminar la lista.
Ingresa 'HELP' para mostrar los comandos.
Ingresa 'SHOW' para mostrar lo que llevas en la lista.
Ingresa 'REMOVE' para eliminar un articulo de la lista
""")


def add_to_list(item):
    show_list()
    
    if len(shopping_list):
        position = input('Donde deseas agregar? {}?\n'
                         'Presiona ENTER para agregar al final de la lista\n'
                         '> '.format(item))
    else:
        position = 0
    
    try:
        position = abs(int(position))
        # abs retorna el valor absoluto del numero es decir si es negativo lo           retorna positivo
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()        

def remove_from_list():
    show_list()
    
    remove_item = input('Que articulo de la lista quieres eliminar? ')
    
    try:
        shopping_list.remove(remove_item.capitalize())
    except ValueError:
        pass
    
    show_list()


def show_list():
    clear_screen()
    
    print("Aqui esta tu lista:")
    
    for index, item in enumerate(shopping_list, start=1): # start le indica a enumerate desde donde empezar
        print('{}. {}'.format(index, item))
        
    print('-' * 20)


show_help()

while True:
    new_item = input("> ").capitalize()

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()