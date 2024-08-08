import requests
import allure

@allure.feature('User Registration')
@allure.suite('User Management')
@allure.title('Successful User Registration')
@allure.description('This test checks if a user can successfully register with a valid email and password.')
@allure.severity(allure.severity_level.CRITICAL)
def test_register_user_success():
    url = "https://reqres.in/api/register"
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(url, json=data)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()
    assert "id" in response_data, "Response JSON does not contain 'id'"
    assert "token" in response_data, "Response JSON does not contain 'token'"
    global my_token
    my_token = response.json().get('token')


@allure.feature('User Registration')
@allure.suite('User Management')
@allure.title('User Registration Missing Password')
@allure.description('This test verifies that the registration fails if the password is missing.')
@allure.severity(allure.severity_level.NORMAL)
def test_register_user_missing_password():
    data = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post(
        "https://reqres.in/api/register",
        json=data)

    assert response.status_code == 400, f'Expected status code 400, but got {response.status_code}'
    response_data = response.json()
    assert "error" in response_data, 'Response JSON does not contain "error"'
    assert response_data["error"] == "Missing password", f'Expected error message "Missing password", but got {response_data["error"]}'


@allure.feature('User Login')
@allure.suite('User Management')
@allure.title('Successful User Login')
@allure.description('This test checks if a user can successfully log in with a valid email and password.')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_user_success():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(
        "https://reqres.in/api/login",
        json=data)

    assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'
    response_data = response.json()
    assert "token" in response_data, 'Response JSON does not contain "token"'


@allure.feature('User Login')
@allure.suite('User Management')
@allure.title('User Login Missing Password')
@allure.description('This test verifies that the login fails if the password is missing.')
@allure.severity(allure.severity_level.NORMAL)
def test_login_user_missing_password():
    data = {
        "email": "peter@klaven"
    }

    response = requests.post(
        "https://reqres.in/api/login",
        json=data)

    assert response.status_code == 400, f'Expected status code 400, but got {response.status_code}'
    response_data = response.json()
    assert "error" in response_data, 'Response JSON does not contain "error"'
    assert response_data["error"] == "Missing password", f'Expected error message "Missing password", but got {response_data["error"]}'


@allure.feature('User Creation')
@allure.suite('User Management')
@allure.title('Create User')
@allure.description('This test checks if a new user can be successfully created with a name and job.')
@allure.severity(allure.severity_level.MINOR)
def test_create_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(
        "https://reqres.in/api/users",
        json=data)

    assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'
    response_data = response.json()
    assert response_data["name"] == "morpheus", f'Expected name "morpheus", but got {response_data["name"]}'
    assert response_data["job"] == "leader", f'Expected job "leader", but got {response_data["job"]}'
