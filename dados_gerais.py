class Usuario:
    def __init__(self):
        self.nome = str(input('Digite seu nome: '))
        while self.nome.replace(' ', '').isalpha() == False:
            print('Você digitou caracteres especiais e/ou números, digite somente letras!')
            self.nome = str(input('Digite seu nome: '))
        self.idade = input('Digite sua idade: ')
        while self.idade.isdigit() == False:
            print('Você não digitou um número, tente novamente!')
            self.idade = (input('Digite sua idade: '))
        self.sexo = str.upper(input('Digite seu sexo (M ou F): '))
        while self.sexo not in ['M', 'F']:
            print('O sexo digitado não é válido, digite M ou F!')
            self.sexo = str(input('Digite seu sexo (M ou F): '))


class Residencia:
    def __init__(self):
        self.uf = str(input('Digite sua UF: '))
        if self.uf.replace(' ', '').isalpha() == False:
            print('Você digitou caracteres especiais e/ou números, digite somente letras!')
            self.uf = str(input('Digite sua UF: '))
        self.cidade = str(input('Digite sua cidade: '))
        if self.cidade.replace(' ', '').isalpha() == False:
            print('Você digitou caracteres especiais e/ou números, digite somente letras!')
            self.cidade = str(input('Digite sua cidade: '))
        self.país = str(input('Digite seu país: '))
        if self.país.replace(' ', '').isalpha() == False:
            print('Você digitou caracteres especiais e/ou números, digite somente letras!')
            self.país = str(input('Digite seu país: '))
