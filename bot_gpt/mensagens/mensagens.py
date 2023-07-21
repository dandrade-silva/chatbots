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


def familia():
    return "Opção Familia..."


def amigo():
    return "Opção Amigo..."


def colega():
    return "Opção Colega..."


def cobranca():
    return "Opção Cobranca..."


def trabalho():
    return "Opção Trabalho..."


opcoes = {
    1: familia,
    2: amigo,
    3: colega,
    4: cobranca,
    5: trabalho
}


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
