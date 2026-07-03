#pensei em um cadastro onde podemos colocar dados pessoais, dados de residência e etc
import json
import random
import string
import sys

from dados_pessoais import cadast_usuar
from dados_residen import cadast_resid
import banco

print("Olá! Seja bem vindo ao sistema.")
print("---------------------------------")
novo = str.lower(input("Você é usuário novo ou possui conta? "))
print("---------------------------------")

if novo != "novo":
    user = int(input("Digite a sua conta: "))
    conta = banco.valid_conta(user)

    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    for banco in dados:
        if banco["Banco"]["Conta"] == user:
            userenc = banco
            break

    oper = str.lower(input(f'''Escolha uma das opções abaixo: 
                                    
[1] Depositar
[2] Sacar
[3] Ver saldo
[4] Transferir para outra conta
[5] Sair
                                    
Digite o número desejado: '''))

    while oper != "5":

        if oper == "1":
            valor = float(input("Digite o valor que deseja depositar: "))
            conta.depositar(valor)
            print(f"Você depositou R$ {valor} e agora seu saldo é R$ {conta.saldo}")

            userenc["Banco"]["Saldo"] += valor
            with open("dados.json", "w", encoding="utf-8") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)

        elif oper == "2":
            valor = float(input("Digite o valor que deseja sacar: "))
            while conta.sacar(valor) == "erro":
                print("O valor digitado é maior do que você possui de saldo. Tente novamente.")
                valor = float(input("Digite o valor que deseja sacar: "))
            print(f"Você sacou R$ {valor} e agora seu saldo é R$ {conta.saldo}")

            userenc["Banco"]["Saldo"] -= valor
            with open("dados.json", "w", encoding="utf-8") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)

        elif oper == "3":
            print(f"Você possui R${conta.saldo} de saldo!")
        
        elif oper == "4":
            destino = int(input("Digite a conta que deseja transferir: "))
            conta2 = banco.transf(destino)
            user2 = None

            for banco in dados:
                if banco["Banco"]["Conta"] == destino:
                    user2 = banco
                    break

            while banco.transf(destino) == "erro":
                print("A conta digitada não foi localizada. Tente novamente.")
                destino = int(input("Digite a conta que deseja transferir: "))
            
            valor = float(input("Digite o valor que deseja transferir: "))

            while conta.transferir(valor) == "erro":
                print("O valor digitado é maior do que você possui de saldo. Tente novamente.")
                valor = float(input("Digite o valor que deseja transferir: "))
            
            conta2.depositar(valor)

            print(f"Você transferiu R$ {valor} e agora seu saldo é R$ {conta.saldo}")

            userenc["Banco"]["Saldo"] += valor
            user2["Banco"]["Saldo"] += valor
            with open("dados.json", "w", encoding="utf-8") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)


        oper = str.lower(input(f'''
----------------------------------
Escolha uma das opções abaixo: 
                                        
[1] Depositar
[2] Sacar
[3] Ver saldo
[4] Transferir para outra conta
[5] Sair
                                        
Digite o número desejado: '''))

    print("Obrigado por utilizar nosso sistema.")
    sys.exit()

print("Bem vindo! Faça seu cadastro a seguir!")


tamanho = 10
letras_aleatorias = "".join(random.choices(string.ascii_letters, k=tamanho))
nalet = str(random.randint(0, 100))
cript = letras_aleatorias+nalet



with open("dados.json", "r", encoding="utf-8") as arquivo:
    lista = json.load(arquivo)

dadospessoais = cadast_usuar()
dadosresidenc = cadast_resid()
dadosbancario = banco.cadast_banc()

usuario = {
    "Pessoais":dadospessoais,
    "Residencial":dadosresidenc,
    "Banco":dadosbancario,
    "Cripto":cript
}

listafinal = [usuario]

lista.append(usuario)

with open("dados.json", "w", encoding="utf-8") as arq:
    json.dump(lista, arq, indent=4, ensure_ascii=False)


