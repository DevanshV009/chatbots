from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from handlers.message_handler import get_reply

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()

    response = MessagingResponse()
    reply = get_reply(incoming_msg)

    response.message(reply)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)