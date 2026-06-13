user_state = {}

lead_data = {}

def get_reply(user_id, message):

    msg = message.strip()

    if user_id not in user_state:

        user_state[user_id] = "category"

        return """
🛍 Welcome to E-Commerce Store

Choose Category:

1. Electronics
2. Fashion
3. Home & Kitchen
"""

    state = user_state[user_id]

    if state == "category":

        lead_data[user_id] = {
            "category": msg
        }

        user_state[user_id] = "name"

        return "Please enter your name."

    elif state == "name":

        lead_data[user_id]["name"] = msg

        user_state[user_id] = "email"

        return "Please enter your email."

    elif state == "email":

        lead_data[user_id]["email"] = msg

        user_state[user_id] = "phone"

        return "Please enter your phone number."

    elif state == "phone":

        lead_data[user_id]["phone"] = msg

        user_state[user_id] = "completed"

        return f"""
✅ Lead Captured Successfully

Category: {lead_data[user_id]['category']}
Name: {lead_data[user_id]['name']}
Email: {lead_data[user_id]['email']}
Phone: {lead_data[user_id]['phone']}
"""

    return "Lead already captured."