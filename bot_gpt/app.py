from flask import Flask, request, jsonify
from mensagens import mensagens

app = Flask(__name__)

# Configurar as credenciais do Twilio
ACCOUNT_SID = 'ACf206200b1cca65bd5008d81d14a8b670'
AUTH_TOKEN = '05f07dc8e6d7f4660aa6fd808a442afd'


@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = generate_twiml_response(incoming_msg)
    return (response, 200, {'Content-Type': 'application/xml'})


def generate_twiml_response(incoming_msg):
    resp = mensagens.atendimento(incoming_msg)

    return f"<Response><Message>{resp}</Message></Response>"


if __name__ == "__main__":
    app.run(debug=True)
