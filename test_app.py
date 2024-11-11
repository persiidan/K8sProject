from app import app


def test_status_code():
    # Create a test client using Flask's built-in test_client
    client = app.test_client()

    # Send a GET request to the root URL
    response = client.get('/')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

    print("Tests passed!")

if __name__ == '__main__':
    test_status_code()
