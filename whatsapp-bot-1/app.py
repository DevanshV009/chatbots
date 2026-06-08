from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from handlers.message_handler import get_reply

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body", "")
    
    reply = get_reply(incoming_msg)

    response = MessagingResponse()
    response.message(reply)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)