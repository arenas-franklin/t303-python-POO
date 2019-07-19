class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono
    
    def comer(self):
        print("Nhom nhom", self.nome)
    
class Gato(Animal):
        def __init__(self, nome,dono, raca):
            super().__init__(nome, dono)
            self.raca = raca
        
        def miar(self):
            print('Minhauuuuu')

class Cachorro(Animal):
        def latir(self):
            print('Au auuuuu')

gato = Gato('xuxuzinhho', 'Matheus', 'siames')
cachorro = Cachorro('rex', 'Barbara')
animal = Animal('toddy', 'gabriel')
  
cachorro.latir()  

print(cachorro.nome)
print(cachorro.dono)