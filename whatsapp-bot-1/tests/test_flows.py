from handlers.message_handler import get_reply

def test_welcome_message():

    response = get_reply("Hi")

    assert "E-Commerce Store" in response


def test_category_menu():

    response = get_reply("Hi")

    assert "Electronics" in response
    assert "Fashion" in response
    assert "Home & Kitchen" in response