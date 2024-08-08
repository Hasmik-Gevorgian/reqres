import requests
import allure

@allure.feature('User Deletion')
@allure.suite('User Management')
@allure.title('Delete User')
@allure.description('This test verifies that a user can be successfully deleted.')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204, f'Expected status code 204, but got {response.status_code}'
