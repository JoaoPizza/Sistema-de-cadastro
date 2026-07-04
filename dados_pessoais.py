class Usuario:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo



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



if __name__ == '__main__':
    cadast_usuar()