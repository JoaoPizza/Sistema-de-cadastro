

def banco(texto):
    '''
    Aqui é a função para passar os dados para um arquivo a parte, assim salvando eles
    '''
    with open('dados_pessoais.txt', 'a') as arquivo:
        arquivo.write('''
''')
        arquivo.write(texto)


class Residencia:
    def __init__(self, uf, cidade, pais):
        self.uf = uf
        self.cidade = cidade
        self.país = pais


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

    banco(f'UF: {uf} | Cidade: {cidade} | Pais: {país}')

    resid = {
        "UF": uf,
        "Cidade": cidade,
        "Pais": país
        }

    return resid



if __name__ == '__main__':
    cadast_resid()