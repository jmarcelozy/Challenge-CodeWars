#link of challenge https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/python

def flick(lst):
    cont = 0
    lista = []
    t = True
    for c in range(0,len(lst)):
        if lst[c] == 'flick':
            t = False
            cont += 1
            print(f'{cont}a')
            if cont % 2 == 0:
                t = True
        lista.append(t)
    print(lista)
    

      


a = flick(['carro','computador','rodas','flick','gamepad','livro','flick','jogo','mouse','teclado','flick','celular','tekken','monitor'])


