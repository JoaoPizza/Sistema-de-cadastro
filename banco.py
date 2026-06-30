#inutilizado pois movi o salvamento para dentro dos dados gerais


from dados_gerais import Usuario
from dados_gerais import Residencia

usuario = Usuario()
residencia = Residencia()


def banco(texto):
    '''
    Aqui é a função para passar os dados para um arquivo a parte, assim salvando eles
    '''
    with open('dados_pessoais.txt', 'a') as arquivo:
        arquivo.write('''
''')
        arquivo.write(texto)


banco(usuario.nome)
banco(usuario.idade)
banco(usuario.sexo)
banco(residencia.uf)
banco(residencia.cidade)
banco(residencia.país)




'''
cadast = {
    'dadpessoa': {
        'nome': 0,
        'idade': 0,
        'sexo': 0
    },
    'local': {
        'UF': 0,
        'cidade': 0,
        'país': 0
    }
}



dados = dados_pessoais()

nome = dados[0]
idade = dados[1]
sexo = dados[2]

residencia = dados_residencia()

uf = residencia[0]
cidade = residencia[1]
país = residencia[2]



def passar_dicio():
    cadast['dadpessoa']['nome'] = nome
    banco('Nome: ',nome)
    cadast['dadpessoa']['idade'] = idade
    banco('Idade: ',idade)
    cadast['dadpessoa']['sexo'] = sexo
    banco('Sexo: ',sexo)
    cadast['local']['UF'] = uf
    banco('UF: ',uf)
    cadast['local']['cidade'] = cidade
    banco('Cidade: ',cidade)
    cadast['local']['país'] = país
    banco('País: ',país)


passar_dicio()'''
