import json
import sys


class Dados_bancarios:
    def __init__(self, conta, senha, saldo=2000):
        self.conta = conta
        self.senha = senha
        self.saldo = saldo

    def sacar(self, valor):

        if valor > self.saldo:
            return False
        
        if valor > 1500:
            return False
        
        elif valor <= 0:
            return False
        
        else:
            self.saldo -= valor
    
    def depositar(self, valor):

        if valor <= 0:
            return False
        
        else:
            self.saldo += valor


    def transferir(self, valor):

        if valor > self.saldo:
            return False
        
        if valor <= 0:
            return False

        else:
            self.saldo -= valor



def cadast_banc():
    conta = int(input("Digite sua conta: "))
    senha = int(input("Digite sua senha: "))
    saldo = 2000

    return Dados_bancarios(conta, senha)

def valid_conta(conta):
    userenc = None
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    for banco in dados:
        if banco["Banco"]["Conta"] == conta:
            userenc = banco
            break
    
    if userenc is not None:
        
        senhacorr = userenc["Banco"]["Senha"]
        saldo = userenc["Banco"]["Saldo"]
        conta = userenc["Banco"]["Conta"]

        senha = str(input("Digite sua senha: "))

        while senha != senhacorr or senha == "" or senha.isnumeric() == False:
            print("Senha incorreta! Tente novamente.")
            senha = str(input("Digite sua senha: "))
    
    elif userenc == None:
        return False

    return Dados_bancarios(conta, senhacorr, saldo)

def transf(conta):
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()
    nvc = None

    for transf in dados:
        if transf["Banco"]["Conta"] == conta:
            nvc = transf
            break

    if nvc is not None:

        nvss = nvc["Banco"]["Senha"]
        nvm = nvc["Pessoais"]["Nome"]
        nvs = nvc["Banco"]["Saldo"]

    else:
        return False


    return Dados_bancarios(conta, nvss, nvs)

if __name__ == '__main__':
    cadast_banc()