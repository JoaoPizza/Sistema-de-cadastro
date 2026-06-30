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
novo = str(input("Você é usuário novo ou possui conta? "))
print("---------------------------------")

if novo != "Novo":
    conta = banco.valid_conta()

    oper = str.lower(input(f'''Escolha uma das opções abaixo: 
                                    
[1] Depositar
[2] Sacar
[3] Ver saldo
[4] Transferir para outra conta
[5] Sair
                                    
Digite o número desejado: '''))

    if oper == "1":
        banco.depositar(conta)
    elif oper == "2":
        banco.sacar(conta)
    elif oper == "3":
        banco.saldo(conta)
    elif oper == "4":
        banco.transf(conta)
    elif oper == "5":
        print("Obrigado por utilizar nosso sistema.")
        sys.exit()

else:
    print("Conta não encontrada. Faça seu cadastro a seguir!")


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


