import requests

def test_get_user():
    """Тест GET запроса"""
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    # Проверки
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    user = response.json()
    assert user["id"] == 1, f"Expected id 1, got {user['id']}"
    assert "name" in user, "No name field in response"
    assert "email" in user, "No email field in response"
    
    print("✓ test_get_user passed")

def test_create_post():
    """Тест POST запроса"""
    new_post = {
        "title": "Test Post",
        "body": "This is a test",
        "userId": 1
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post
    )
    
    # Проверки
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    data = response.json()
    assert data["title"] == new_post["title"], "Title mismatch"
    assert "id" in data, "No id in response"
    
    print("✓ test_create_post passed")

def test_get_nonexistent():
    """Тест 404"""
    response = requests.get("https://jsonplaceholder.typicode.com/users/99999")
    
    # Некоторые APIs возвращают 404, некоторые пустой ответ
    # JSONPlaceholder возвращает {}
    assert response.status_code in [200, 404], f"Unexpected status: {response.status_code}"
    
    print("✓ test_get_nonexistent passed")

# Запуск тестов
if __name__ == "__main__":
    test_get_user()
    test_create_post()
    test_get_nonexistent()
    print("\n✓ All tests passed!")
