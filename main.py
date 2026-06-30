#pensei em um cadastro onde podemos colocar dados pessoais, dados de residência e etc
import json
import random
import string
import sys

from dados_pessoais import cadast_usuar
from dados_residen import cadast_resid
import banco


novo = str(input("Você é usuário novo ou possui conta? "))

if novo != "Novo":
    user = int(input("Digite o número de sua conta: "))
    userenc = 0

    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    # encontrada = any(banco["Banco"]["Conta"] == user for banco in dados)

    for banco in dados:
        if banco["Banco"]["Conta"] == user:
            userenc = banco
            break

    if userenc is not None:
        print("Usuário encontrado!")

        nome = userenc["Pessoais"]["Nome"]
        senhacorr = userenc["Banco"]["Senha"]

        senha = int(input("Digite sua senha: "))

        if senha == senhacorr:
            print(f"Bem vindo {nome}!")

    sys.exit()



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


