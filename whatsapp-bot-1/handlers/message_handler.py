# Message routing logic
from handlers.lead_flow import get_products

def get_reply(message):

    msg = message.lower().strip()

    if msg in ["hi", "hello", "hey"]:
        return """
Welcome to Dev Store 🛒

1. View Products
2. Contact Support
3. Track Order

Reply with a number.
"""

    elif msg == "1":
        return get_products()

    elif msg == "2":
        return "📞 Our support team will contact you shortly."

    elif msg == "3":
        return "🚚 Please enter your Order ID."

    else:
        return "❌ Invalid option. Reply with 1, 2 or 3."