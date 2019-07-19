# #-*- 
# def  imprimirItens(a,*args):
#     print(type(args))
#     for item in args:
#         print(item)
    

# imprimirItens("banana","pera","uva","abacate")

# imprimirItens("pera","chocolate", "maça", "melancia")

def lista_de_compras(**kwargs):
    print(type(kwargs))
    fruta = kwargs.get('verdura')
    if fruta is not None:
        print(f'Na lista de conpras há uma fruta: {fruta}')

lista_de_compras(fruta='banana', massa='nhoque', verdura='alface')