import requests
import allure

@allure.feature('User Management')
@allure.suite('User Update')
@allure.title('Update User Details')
@allure.description('Test updating user details and verifying the response')
@allure.severity(allure.severity_level.NORMAL)
def test_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(
        'https://reqres.in/api/users/2',
        json=data
    )

    assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()
    assert response_data['name'] == data['name'], f'Expected name "{data["name"]}", but got "{response_data["name"]}"'
    assert response_data['job'] == data['job'], f'Expected job "{data["job"]}", but got "{response_data["job"]}"'
    assert 'updatedAt' in response_data, 'Response JSON does not contain "updatedAt"'
