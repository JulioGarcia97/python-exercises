shopping_list = []
def show_help():
    print('Escribe TERMINE para salir de la app')
    print('Escribe SHOW para mostrar los articulos que ya ingresaste')
    print('Escribe HELP para mostrar todos los comandos de la app')
    
show_help()

def show_list():
    print('Estos fueron los productos que ingresaste: ')
    for item in shopping_list:
        print('- ' + item.capitalize())
        
def shopping_app():
    
    print('Ingresa los articulos que deseas comprar.')
    
    while True:
        nuevo_producto = (input('Producto a llevar: ')).lower()
        
        if nuevo_producto == 'termine':
            break
        elif nuevo_producto == 'help':
            show_help()
            continue # previene de que sea guardado en el shopping_list
        elif nuevo_producto == 'show':
            show_list()
            continue # previene de que sea guardado en el shopping_list
            
        shopping_list.append(nuevo_producto)
    
    show_list()
    
shopping_app()