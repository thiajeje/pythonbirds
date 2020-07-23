class Pessoa:
    def __init__(self,  *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    thiago= Pessoa(nome='Thiago')
    luciano = Pessoa(thiago, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Nunes'
    del luciano.filhos
    print(luciano.__dict__)
    print(thiago.__dict__)