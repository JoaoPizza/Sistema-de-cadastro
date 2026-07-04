#pensei em um cadastro onde podemos colocar dados pessoais, dados de residência e etc
import json
import random
import string
import sys

from dados_pessoais import cadast_usuar
from dados_residen import cadast_resid
import banco

def salvar(dados):
    with open("dados.json", "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)



print("Olá! Seja bem vindo ao sistema.")
print("---------------------------------")
novo = str.lower(input("Você é usuário novo ou possui conta? "))
print("---------------------------------")

if novo != "novo":

    #Primeiro recebemos a conta e fazemos a abertura do JSON dentro da variável dados

    user = str(input("Digite a sua conta: "))
    
    #Validamos se o input não é um espaço vazio ou uma letra    
    while user == "" or user.isnumeric() == False:
        print("Você digitou caracteres não aceitos nesse campo. Digite somente números!")
        user = input("Digite a sua conta: ")

    conta = banco.valid_conta(user)

    #Fazemos a validação dentro do JSON para verificar se a conta existe
    while conta == False:
        print("Conta não encontrada! Tente novamente.")
        user = str(input("Digite a sua conta: "))
        conta = banco.valid_conta(user)

    print("---------------------------------")
    
    based = open("dados.json", "r")
    dados = json.load(based)
    based.close()

    for cbanco in dados:
        if cbanco["Banco"]["Conta"] == user:
            userenc = cbanco
            break
    
    #Apesar da validação da conta acontecer dentro da função, encontramos ela por fora para podermos manuseá-la

    oper = str.lower(input(f'''Escolha uma das opções abaixo: 
                                    
[1] Depositar
[2] Sacar
[3] Ver saldo
[4] Transferir para outra conta
[5] Sair
                                    
Digite o número desejado: '''))

    while oper != "5":

        if oper == "1":

            #Com o try estou primeiro tentando o input, caso ele retorne o erro ele dá o print e volta para o try isso impede qualquer caracter especial no campo

            while True:
                try:
                    valor = float(input("Digite o valor que deseja depositar: "))
                    break
                except ValueError:
                    print("Opção inválida! Por favor, digite apenas números.")

            while conta.depositar(valor) == False:
                print("Operação inválida. Tente novamente.")
                valor = float(input("Digite o valor que deseja depositar: "))
            print(f"Você depositou R$ {valor} e agora seu saldo é R$ {conta.saldo}")

            #Aqui fazemos a atualização do valor em saldo do usuário por meio da variável obtida dentro do for que roda ao inicio do programa

            userenc["Banco"]["Saldo"] += valor
            salvar(dados)

        elif oper == "2":

            while True:
                try:
                    valor = float(input("Digite o valor que deseja sacar: "))
                    break
                except ValueError:
                    print("Opção inválida! Por favor, digite apenas números.")
            

            #Antes de fazer a operação nós fazemos a validação do saldo em conta para ver se o valor desejado não é maior do que o em conta, isso ocorre dentro do método sacar e retorna False em caso de valores maiores que o saldo
            while conta.sacar(valor) == False:
                print("Operação inválida. Tente novamente.")
                valor = float(input("Digite o valor que deseja sacar: "))
            print(f"Você sacou R$ {valor} e agora seu saldo é R$ {conta.saldo}")

            userenc["Banco"]["Saldo"] -= valor
            salvar(dados)

        elif oper == "3":
            print(f"Você possui R${conta.saldo} de saldo!")
        
        elif oper == "4":
            destino = int(input("Digite a conta que deseja transferir: "))
            conta2 = banco.transf(destino)
            user2 = None

            #Aqui reutilizamos a abertura já feita para rodar e achar a conta destino
            for cbanco in dados:
                if cbanco["Banco"]["Conta"] == destino:
                    user2 = cbanco
                    break
            
            #Como não posso usar um método para localizar a conta, utilizo a função Transf que somente procura a conta e me retorna um objeto com todos dados da conta encontrada, ou me retorna False caso não seja localizada
            while banco.transf(destino) == False or destino == conta:
                print("A conta digitada é inválida. Tente novamente.")
                destino = int(input("Digite a conta que deseja transferir: "))
            
            valor = float(input("Digite o valor que deseja transferir: "))

            #Como se trata de uma transferência onde o saldo sai de uma conta e entra em outra, precisamos verificar se o saldo da conta remetente possui o saldo que deseja transferir, isso ocorre dentro do método de transferencia
            while conta.transferir(valor) == False:
                print("Operação inválida. Tente novamente.")
                valor = float(input("Digite o valor que deseja transferir: "))
            
            conta2.depositar(valor)

            print(f"Você transferiu R$ {valor} e agora seu saldo é R$ {conta.saldo}")

            #Por fim caso todos argumentos estejam válidos fazemos a alteração dos valores nas contas e salvamos o JSON com as novas informações.
            userenc["Banco"]["Saldo"] -= valor
            user2["Banco"]["Saldo"] += valor
            salvar(dados)


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


#Aqui estou gerando uma chave criptografada única para cada novo usuário para posterior validação.
tamanho = 10
letras_aleatorias = "".join(random.choices(string.ascii_letters, k=tamanho))
nalet = str(random.randint(0, 100))
cript = letras_aleatorias+nalet



with open("dados.json", "r", encoding="utf-8") as arquivo:
    lista = json.load(arquivo)

#Como todas as funções abaixo retornam objetos completos e para salvar em JSON preciso de uma lista, primeiro transformo todos os dados do usuário em dicionários pois são mais legíveis e com chaves claras, posteriormente compilo todos eles e passo para uma lista que é anexada ao JSON já existente

pessoais = cadast_usuar()
dadospesso = {
        "Nome":pessoais.nome,
        "Idade":pessoais.idade,
        "Sexo":pessoais.sexo
    }

residenc = cadast_resid()
dadosresid = {
        "UF": residenc.uf,
        "Cidade": residenc.cidade,
        "Pais": residenc.país
        }

bancario = banco.cadast_banc()
dadosbanc = {
        "Conta":bancario.conta,
        "Senha":bancario.senha,
        "Saldo":bancario.saldo
    }

usuario = {
    "Pessoais":dadospesso,
    "Residencial":dadosresid,
    "Banco":dadosbanc,
    "Cripto":cript
}

listafinal = [usuario]

lista.append(usuario)

with open("dados.json", "w", encoding="utf-8") as arq:
    json.dump(lista, arq, indent=4, ensure_ascii=False)


