import banco

user = int(input("Digite a sua conta: "))


conta = banco.valid_conta(user)
print(conta)