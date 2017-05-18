sodas = ['Pepsi', 'CocaCola', 'Sprite']
chips = ['Rufles', 'Cheetos', 'Sabritas']
candys = ['Paleta', 'Chocolate', 'Halls']

while True:
    choice = input('Te gustaria una SODA o CHIPS o un CANDY? ').lower()
    
    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candys.pop()
        else:
            print("No tengo ese producto")
            continue
    except IndexError:
        print("No tengo mas: {}. intenta con otro producto".format(choice))
        continue
    else:
        print("Aqui esta tu {}: {}".format(choice, snack))