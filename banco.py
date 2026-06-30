import json
import sys


def bancoCript(texto):
    '''
    Aqui é a função para passar os dados para um arquivo a parte, assim salvando eles
    '''
    with open('dados_bancarios.txt', 'a') as arquivo:
        arquivo.write('''
''')
        arquivo.write(texto)


class Dados_bancarios:
    def __init__(self, conta, senha, saldo=2000):
        self.conta = conta
        self.senha = senha
        self.saldo = saldo

    def sacar(self, valor):
        self.saldo -= valor
    
    def depositar(self, valor):
        self.saldo += valor


def cadast_banc():
    conta = int(input("Digite sua conta: "))
    senha = int(input("Digite sua senha: "))
    saldo = 2000

    bancoCript(f'Conta: {conta} | Senha: {senha}')

    dadosbanc = {
        "Conta":conta,
        "Senha":senha,
        "Saldo":saldo
    }

    return dadosbanc