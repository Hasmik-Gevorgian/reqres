import requests
import allure

@allure.feature('User Retrieval')
@allure.suite('User Management')
@allure.title('Get All Users on Page 2')
@allure.description('This test checks if the API returns the correct list of users for page 2.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()
    assert "data" in response_data, 'Response JSON does not contain "data"'
    assert response_data['page'] == 2, f'Expected page 2, but got {response_data["page"]}'
    assert response_data['per_page'] == 6, f'Expected per_page 6, but got {response_data["per_page"]}'
    assert response_data['total'] == 12, f'Expected total 12, but got {response_data["total"]}'
    assert response_data['total_pages'] == 2, f'Expected total_pages 2, but got {response_data["total_pages"]}'


@allure.feature('User Retrieval')
@allure.suite('User Management')
@allure.title('Get Single User')
@allure.description('This test verifies that a single user can be retrieved successfully.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_single_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()
    assert "data" in response_data, 'Response JSON does not contain "data"'
    assert response_data["data"]["id"] == 2, f'Expected user ID 2, but got {response_data["data"]["id"]}'
    # print(response_data)


@allure.feature('User Retrieval')
@allure.suite('User Management')
@allure.title('Get Single User Not Found')
@allure.description('This test checks that retrieving a non-existent user returns a 404 status.')
@allure.severity(allure.severity_level.MINOR)
def test_get_single_user_not_found():
    response = requests.get("https://reqres.in/api/users/23")
    assert response.status_code == 404, f'Expected status code 404, but got {response.status_code}'
