import os
import json

if not os.path.exists('dados.json'):
    with open('dados.json', 'w') as file:
        json.dump({}, file)

def carregar_dados():
    with open('dados.json', 'r') as file:
        return json.load(file)
    
def salvar_dados(dados):
    with open('dados.json', 'w') as file:
        return json.dump(dados, file)
    
def criar_conta():
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    
    dados = carregar_dados()

    if nome in dados:
        print('Usuário já existe. Tente fazer login.')
        return
    

    dados[nome] = {'senha': senha, 'saldo': 0}
    salvar_dados(dados)
    print("Contra criada com sucesso!\nBem vindo ao Daniel's Bank")

def fazer_login():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    dados = carregar_dados()
    if nome not in dados or dados[nome]['senha'] != senha:
        print("Nome de usuário ou senha incorretos.")
        return None
    return nome

def realizar_trasacao(usuario):
    dados = carregar_dados()
    while True:
        print("\nOpções de Transação:")
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")

        escolha = input("O que você quer fazer: ")

        if escolha == "1":
            print(f"Seu saldo é: ${dados[usuario]['saldo']}")
        
        elif escolha == "2":
            valor = float(input(f"Digite o valor para depósito: "))
            dados[usuario]['saldo'] += valor
            salvar_dados(dados)
            print(f"Depósito de ${valor} realizado com sucesso!")
        elif escolha == "3":
            valor = float(input("Digite o valor para saque: "))
            if valor != 0:
                if valor > dados[usuario]['saldo']:
                    print("Saldo insuficiente.")
                else:
                    dados[usuario]['saldo'] -= valor
                    salvar_dados(dados)
                    print(f"Saque de ${valor} realizado com sucesso!")
            else:
                print(f"Não é possível sacar este valor!")
        elif escolha == "4":
            print('Saindo...')
            break
        else:
            print('Opção inválida.')
if __name__ == '__main__':
    while True:
        print("\nBem vindo ao Daniel's Bank:\n\nOpções:")
        print("1. Criar Conta")
        print("2. Fazer Login")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            usuario = fazer_login()
            if usuario:
                realizar_trasacao(usuario)
        elif escolha == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")
    