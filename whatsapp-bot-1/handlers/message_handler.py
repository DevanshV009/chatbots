# Message routing logic
from handlers.lead_flow import (
    product_menu,
    capture_name,
    capture_email,
    capture_phone
)

step = 0

def get_reply(message):

    global step

    msg = message.lower()

    if msg == "hi" or msg == "hello":
        step = 1
        return product_menu()

    elif step == 1:
        step = 2
        return capture_name(msg)

    elif step == 2:
        step = 3
        return capture_email(msg)

    elif step == 3:
        step = 4
        return capture_phone(msg)

    elif step == 4:
        step = 0
        from handlers.lead_flow import finalize_lead
        return finalize_lead(msg)

    return (
        "👋 Welcome to E-Commerce Store\n\n"
        "Type Hi to start."
    )