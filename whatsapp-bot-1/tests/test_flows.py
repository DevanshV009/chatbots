# Conversation flow tests
from handlers.lead_flow import get_products

def test_products():

    products = get_products()

    assert "Shoes" in products