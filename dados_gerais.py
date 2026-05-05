import os

def dados_pessoais():
    '''
    Essa função capta dados pessoais inseridos pelo usuário, de forma pré-definida para str, int e etc e valida ela conforme necessário!
    '''
    nome = str(input('Digite seu nome: '))
    if nome.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        nome = str(input('Digite seu nome: '))
    idade = (input('Digite sua idade: '))
    while idade.isdigit() == False:
        print('Você não digitou um número, tente novamente!')
        idade = (input('Digite sua idade: '))
    sexo = str.upper(input('Digite seu sexo (M ou F): '))
    while sexo not in ['M', 'F']:
        print('O sexo digitado não é válido, digite M ou F!')
        sexo = str(input('Digite seu sexo (M ou F): '))
    return [nome, idade, sexo]



def dados_residencia():
    '''
    Essa função capta os dados residencias inseridos pelo usuário e valida ela conforme necessário!
    '''
    uf = str(input('Digite sua UF: '))
    if uf.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        uf = str(input('Digite sua UF: '))
    cidade = str(input('Digite sua cidade: '))
    if cidade.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        cidade = str(input('Digite sua cidade: '))
    país = str(input('Digite seu país: '))
    if país.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        país = str(input('Digite seu país: '))
    return [uf, cidade, país]

if __name__ == '__main__':
    dados_pessoais()
    print('-'*50)
    dados_residencia()
