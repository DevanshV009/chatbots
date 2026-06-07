from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "WhatsApp Bot Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    response = MessagingResponse()
    response.message("Hello World from WhatsApp Bot!")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)