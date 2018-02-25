class Pessoa:
    # da classe
    olhos = 2

    # da instancia
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_attr_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    renzo = Homem(nome='Renzo', idade=30)
    luciano = Pessoa(renzo, nome='Luciano')

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
        print(filho.idade)
    # da instância
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)
    del luciano.sobrenome
    # __dict__ - da instância
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(f'antes da mudança luciano.olhos - {luciano.olhos}')
    # da classe - vai todas as instancias
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_attr_de_classe(), luciano.nome_e_attr_de_classe())
    print(isinstance(luciano, Pessoa))
    print(isinstance(luciano, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))


