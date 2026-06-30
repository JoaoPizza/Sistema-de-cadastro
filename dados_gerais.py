#inutilizado pois houve a separação de responsabilidades


def banco(texto):
    '''
    Aqui é a função para passar os dados para um arquivo a parte, assim salvando eles
    '''
    with open('dados_pessoais.txt', 'a') as arquivo:
        arquivo.write('''
''')
        arquivo.write(texto)



class Usuario:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        banco(self.nome)
        self.idade = idade
        banco(self.idade)
        self.sexo = sexo
        banco(self.sexo)


class Residencia:
    def __init__(self, uf, cidade, pais):
        self.uf = uf
        banco(self.uf)
        self.cidade = cidade
        banco(self.cidade)
        self.país = pais
        banco(self.país)


def cadast_usuar():
    nome = str(input('Digite seu nome: '))
    while nome.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        nome = str(input('Digite seu nome: '))
    idade = input('Digite sua idade: ')
    while idade.isdigit() == False:
        print('Você não digitou um número, tente novamente!')
        idade = (input('Digite sua idade: '))
    sexo = str.upper(input('Digite seu sexo (M ou F): '))
    while sexo not in ['M', 'F']:
        print('O sexo digitado não é válido, digite M ou F!')
        sexo = str(input('Digite seu sexo (M ou F): '))

    return Usuario(nome, idade, sexo)


def cadast_resid():
    uf = str(input('Digite sua UF: '))
    while uf.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        uf = str(input('Digite sua UF: '))
    cidade = str(input('Digite sua cidade: '))
    while cidade.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        cidade = str(input('Digite sua cidade: '))
    país = str(input('Digite seu país: '))
    while país.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        país = str(input('Digite seu país: '))
    return Residencia(uf, cidade, país)


if __name__ == '__main__':
    Usuario()
    print('-'*50)
    Residencia()
