from datetime import date 

class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def name_pessoa(self):
        return self.nome

    def old_pessoa(self):
        curret_date = date.today()
        year_pessoa = self.idade.yaer
        old_pessoa =  year_pessoa - curret_date.yaer

class Pet(Pessoa):
    def __init__(self, nome_pet, nasci_pet):
        self.nome_pet = nome_pet
        self.nasci_pet = nasci_pet
    
    def info_pet(self):
        print(self.nome)
        print(self.nome_pet)

    def idade_pet(self):
        ano_atual = date.today().year
        old_pet = ano_atual - self.nasci_pet
        return old_pet

dono = Pessoa('Tadeu', 1993)
pet = Pet( 'mingal', 2007)

print(pet.nasci_pet())
