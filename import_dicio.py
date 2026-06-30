#inutilizado com a nova versão


from dados_gerais import dados_pessoais
from dados_gerais import dados_residencia

espaço = 0

def banco(texto):
    '''
    Aqui é a função para passar os dados para um arquivo a parte, assim salvando eles
    '''
    with open('dados_pessoais.txt', 'a') as arquivo:
        arquivo.write('''
''')
        arquivo.write(texto)


'''
Aqui nós vamos passar os valores obtidos da captação de dados para dentro do dicionário
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
    '''
    Nessa função nós estamos pegando cada linha do dicionário e atribuindo o valor correspondente dela que sai direto do input!
    '''
    cadast['dadpessoa']['nome'] = nome
    banco(nome)
    cadast['dadpessoa']['idade'] = idade
    banco(idade)
    cadast['dadpessoa']['sexo'] = sexo
    banco(sexo)
    cadast['local']['UF'] = uf
    banco(uf)
    cadast['local']['cidade'] = cidade
    banco(cidade)
    cadast['local']['país'] = país
    banco(país)


passar_dicio()