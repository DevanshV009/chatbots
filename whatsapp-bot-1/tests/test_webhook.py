from app import app

def test_home_page():

    tester = app.test_client()

    response = tester.get("/")

    assert response.status_code == 200


def test_webhook():

    tester = app.test_client()

    response = tester.post(
        "/webhook",
        data={"Body": "Hi"}
    )

    assert response.status_code == 200