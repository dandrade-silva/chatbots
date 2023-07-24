menu = """
Olá, sou um bot criado pelo Danilo! 
Mas ainda estou em fase de desenvolvimento :(

Digite uma das opções abaixo (1 a 5): 
============================
[1] Sou da familia
[2] Amigo
[3] Colega/Conhecido
[4] Cobrança
[5] Oportunidade de emprego
============================
AHH, você vai ficar recebendo essa mensagem até 
digitar uma opção válida
"""
menu_familia = """
Qual seu grau de parentesco com ele? :(

Digite uma das opções abaixo (1 a 5): 
============================
[1] Mãe
[2] Irmão
[3] Primo(a)
[4] Sobrinho(a)
[5] Tio(a)
============================
AHH, você vai ficar recebendo essa mensagem até 
digitar uma opção válida
"""


def familia():
    while True:
        grau_parentesco = input(menu_familia)
        if grau_parentesco == 1:
            return "Opção Mãe..."
        elif grau_parentesco == 2:
            return "Opção Irmão..."
        elif grau_parentesco == 3:
            return "Opção Primo(a)..."
        elif grau_parentesco == 4:
            return "Opção Sobrinho..."
        elif grau_parentesco == 5:
            return "Opção Tio(a)..."


def amigo():
    return "Opção Amigo..."


def colega():
    return "Opção Colega..."


def cobranca():
    return "Opção Cobranca..."


def trabalho():
    return "Opção Trabalho..."


def atendimento(mensagem):
    print(type(mensagem))
    if mensagem not in ["1", "2", "3", "4", "5"]:
        return menu
    elif mensagem == "1":
        return familia()
    elif mensagem == "2":
        return amigo()
    elif mensagem == "3":
        return colega()
    elif mensagem == "4":
        return cobranca()
    else:
        return trabalho()
