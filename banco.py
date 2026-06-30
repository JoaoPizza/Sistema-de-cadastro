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

def valid_conta():
    user = int(input("Digite o número de sua conta: "))
    userenc = None
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    for banco in dados:
        if banco["Banco"]["Conta"] == user:
            userenc = banco
            break
    
    if userenc is not None:
        print(f"Usuário encontrado!")
        
        nome = userenc["Pessoais"]["Nome"]
        senhacorr = userenc["Banco"]["Senha"]
        saldo = userenc["Banco"]["Saldo"]
        conta = userenc["Banco"]["Conta"]

        senha = int(input("Digite sua senha: "))
        if senha == senhacorr:
            print(f"Bem vindo {nome}!")
    
    else:
        print("Conta não encontrada!")

    return conta

def depositar(var):
    userenc = None
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    for banco in dados:
        if banco["Banco"]["Conta"] == var:
            userenc = banco
            break
    
    val = int(input("Digite o valor que deseja depositar: "))
    userenc["Banco"]["Saldo"] += val
    print("Operação realizada com sucesso!")
    print(f"Agora você tem R$ {userenc["Banco"]["Saldo"]} de saldo.")
    with open("dados.json", "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)
    sys.exit()

def sacar(var):
    userenc = None
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    for banco in dados:
        if banco["Banco"]["Conta"] == var:
            userenc = banco
            break
    
    val = int(input("Digite o valor que deseja sacar: "))
    while val > userenc["Banco"]["Saldo"]:
        print("O valor solicitado é maior do que você possui em conta, tente novamente!")
        val = int(input("Digite o valor que deseja sacar: "))
    userenc["Banco"]["Saldo"] -= val
    print("Operação realizada com sucesso!")
    print(f"Agora você tem R$ {userenc["Banco"]["Saldo"]} de saldo.")
    with open("dados.json", "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)
    sys.exit()

def saldo(var):
    userenc = None
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    for banco in dados:
        if banco["Banco"]["Conta"] == var:
            userenc = banco
            break
    
    saldo = userenc["Banco"]["Saldo"]
    nome = userenc["Pessoais"]["Nome"]

    print(f"{nome}, você possui R$ {saldo} de saldo.")
    sys.exit()

def transf(var):
    userenc = None
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()
    nvc = None


    for banco in dados:
        if banco["Banco"]["Conta"] == var:
            userenc = banco
            break
    
    nvc = int(input("Digite o número da conta desejada: "))
    for transf in dados:
        if transf["Banco"]["Conta"] == nvc:
            nvc = transf
            break
    if nvc is not None:
        print("Conta localizada!")

        nvm = nvc["Pessoais"]["Nome"]
        nvs = nvc["Banco"]["Saldo"]

        val = int(input("Digite o valor desejado para transferir: "))
        while val > userenc["Banco"]["Saldo"]:
            print("Valor digitado maior do que você possui de saldo. Tente novamente!")
            val = int(input("Digite o valor desejado para transferir: "))
        userenc["Banco"]["Saldo"] -= val
        nvc["Banco"]["Saldo"] += val

        print("Operação realizada com sucesso!")
        print(f"Você transferiu R$ {val} para {nvm}")
        with open("dados.json", "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
        sys.exit()
    else:
        print("Conta não localizada. Tente novamente.")


if __name__ == '__main__':
    cadast_banc()