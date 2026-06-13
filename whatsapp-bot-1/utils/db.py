def save_lead(lead):

    with open("leads.txt", "a") as file:

        file.write(
            f"{lead.name},"
            f"{lead.email},"
            f"{lead.phone},"
            f"{lead.category}\n"
        )