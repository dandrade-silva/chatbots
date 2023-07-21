# Importando a classe ChatBot da biblioteca chatterbot
from spacy.cli import download
from chatterbot import ChatBot

# Importo a classe ListTrainer para treinar o bot
from chatterbot.trainers import ListTrainer

# Importe o nltk e baixe os pacotes de dados para o idioma português
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Isso aqui só precisa para corrigir o bug

download("en_core_web_sm")


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


# Criando uma instância do ChatBot com idioma em português
bot = ChatBot('danilo', tagger_language=ENGSM, language='portuguese')


frases_treinamento = [
    'Bom dia!',
    'Boa tarde!',
    'Boa noite!',
    'Olá, como vai?',
    'Oi, tudo bem?',
    'Caro senhor/senhora, como posso ajudá-lo(a)?',
    'Prezado(a) usuário(a), seja bem-vindo(a)!',
    'Excelentíssimo(a) senhor(a), estou à sua disposição.',
    'Saudações!',
    'Cumprimentos, como posso ser útil?',
    'Senhor(a), é uma honra tê-lo(a) aqui.',
    'Como posso servi-lo(a) hoje?',
    'Desejo-lhe um bom dia!',
    'Espero que esteja bem. Como posso ajudá-lo(a)?',
    'Com licença, posso ajudá-lo(a) em algo?',
    'Muito prazer em conhecê-lo(a).',
    'Gostaria de me apresentar, sou o ChatBot Danilo.',
    'Senhor(a), estou aqui para responder suas perguntas.',
    'Se precisar de qualquer assistência, estou à disposição.',
    'Permita-me ajudá-lo(a) com qualquer dúvida ou problema.',
    'É uma satisfação atendê-lo(a).',
    'Posso ser de ajuda em alguma questão específica?',
    'Em que posso ser útil?',
    'Estou aqui para fornecer informações e orientações.',
    'Estou ao seu dispor, senhor(a).',
    'Senhor(a), estou pronto(a) para ajudá-lo(a) em qualquer momento.',
    'Por favor, não hesite em me fazer perguntas.',
    'Como posso ser de auxílio para você hoje?',
    'Seja bem-vindo(a) ao nosso atendimento. Em que posso ajudá-lo(a)?',
    'Diga-me como posso ajudar, e farei o meu melhor para satisfazer suas necessidades.',
    'Senhor(a), saiba que estou aqui para lhe proporcionar a melhor experiência possível.',
]


# Treinando o chatbot com uma lista de frases em português
trainer = ListTrainer(bot)
trainer.train(frases_treinamento)
0

while True:
    mensagem = str(input('Mensagem para o bot (0 para sair): '))
    print(bot.get_response(mensagem))
    if mensagem == "0":
        break
