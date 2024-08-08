import requests
import allure

@allure.feature('Delayed Response')
@allure.suite('User Management')
@allure.title('Delayed User Data Retrieval')
@allure.description('This test checks if the API correctly handles delayed responses when retrieving user data.')
@allure.severity(allure.severity_level.MINOR)
def test_delayed_response():
    response = requests.get("https://reqres.in/api/users?delay=3")

    assert response.status_code == 200, f"Failed to retrieve data: {response.status_code}"

    response_data = response.json()
    assert "data" in response_data, 'Response JSON does not contain "data"'
