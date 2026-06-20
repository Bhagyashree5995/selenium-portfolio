import requests

BASE_URL = "https://jsonplaceholder.typicode.com"



def test_get_list_of_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print("✅ Get users test passed!")


def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2
    print("✅ Get single user test passed!")


def test_create_new_user():
    payload = {
        "name": "Bhagyashree",
        "job": "QA Automation Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Bhagyashree"
    assert "id" in response.json()
    print("✅ Create user test passed!")


def test_update_user():
    payload = {
        "name": "Bhagyashree",
        "job": "Senior QA Engineer"
    }
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "Senior QA Engineer"
    print("✅ Update user test passed!")


def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    print("✅ Delete user test passed!")


def test_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404
    print("✅ User not found test passed!")