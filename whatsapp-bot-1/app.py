from flask import Flask, request, render_template, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from handlers.message_handler import get_reply

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_id = "web-user"

    message = data.get("message", "")

    reply = get_reply(user_id, message)

    return jsonify({
        "reply": reply
    })


@app.route("/webhook", methods=["POST"])
def webhook():

    incoming_msg = request.values.get("Body", "").strip()

    user_id = request.values.get("From", "whatsapp-user")

    response = MessagingResponse()

    reply = get_reply(user_id, incoming_msg)

    response.message(reply)

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)