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
    pais = str(input('Digite seu país: '))
    while pais.replace(' ', '').isalpha() == False:
        print('Você digitou caracteres especiais e/ou números, digite somente letras!')
        pais = str(input('Digite seu país: '))

    return Residencia(uf, cidade, pais)



if __name__ == '__main__':
    cadast_resid()