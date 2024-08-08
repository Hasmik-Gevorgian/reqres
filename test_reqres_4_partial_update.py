import requests
import allure

@allure.feature('User Update')
@allure.suite('User Management')
@allure.title('Partial Update User')
@allure.description('This test checks if a user can be partially updated with new name and job details.')
@allure.severity(allure.severity_level.NORMAL)
def test_partial_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(
        'https://reqres.in/api/users/2',
        json=data)

    assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()
    assert response_data['name'] == data['name'], f'Expected name "{data["name"]}", but got "{response_data["name"]}"'
    assert response_data['job'] == data['job'], f'Expected job "{data["job"]}", but got "{response_data["job"]}"'
    assert 'updatedAt' in response_data, 'Response JSON does not contain "updatedAt"'
