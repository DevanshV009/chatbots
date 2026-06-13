from models.lead import Lead
from utils.db import save_lead

current_lead = Lead()


def product_menu():

    return (
        "🛍 Welcome to E-Commerce Store\n\n"
        "Select Product Category:\n\n"
        "1️⃣ Electronics\n"
        "2️⃣ Fashion\n"
        "3️⃣ Home & Kitchen\n\n"
        "Reply with category name."
    )


def capture_name(category):

    current_lead.category = category

    return (
        f"✅ You selected {category.title()}\n\n"
        "Please enter your name."
    )


def capture_email(name):

    current_lead.name = name

    return "📧 Enter your email address."


def capture_phone(email):

    current_lead.email = email

    return "📱 Enter your phone number."


def finalize_lead(phone):

    current_lead.phone = phone

    save_lead(current_lead)

    return (
        "🎉 Thank you!\n\n"
        "Your details have been submitted.\n"
        "Our sales team will contact you shortly."
    )