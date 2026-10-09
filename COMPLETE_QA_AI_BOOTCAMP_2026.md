# ПОЛНЫЙ BOOTCAMP: Python QA Automation → AI Engineering

**Для:** Daniil - переход из tech support в QA/AI инженеры  
**Время:** 16 недель, ~15-20 ч/неделю  
**Результат:** Production-ready portfolio на GitHub + понимание обеих ролей

---

## СТРУКТУРА ПЛАНА

```
Фаза 0 (Неделя 1-2):        Fundament - Python basics
Фаза 1 (Неделя 3-4):        Backend - FastAPI + Database
Фаза 2 (Неделя 5-8):        QA Core - Pytest + API + UI автоматизация
Фаза 3 (Неделя 9-10):       DevOps - CI/CD + Docker
Фаза 4 (Неделя 11-14):      AI Integration - Claude API + Agentы
Фаза 5 (Неделя 15-16):      Portfolio Polish + Продвижение
```

**Главный проект:** `qa-ai-automation-suite` на GitHub
- твой собственный FastAPI сервис
- полный test coverage
- AI агент что управляет тестами
- deployed в Docker

---

# ФАЗА 0: PYTHON FUNDAMENT (Недели 1-2)

## Цель
Крепкий Python для остального пути. Не kata ради kata - только прикладное.

## Неделя 1: Ядро языка

### День 1-2: Переменные, типы, операции
```python
# Что изучить:
# - int, str, list, dict, tuple, set
# - if/elif/else
# - for, while циклы
# - list/dict comprehension

# Практика: простой скрипт
age = 25
name = "Daniil"
skills = ["Python", "Testing", "AWS"]

if age > 18:
    print(f"{name} is adult and knows {len(skills)} skills")

# Comprehension
doubled = [x*2 for x in range(5)]
```

**Ресурс:** Real Python - Python Basics (1-2 часа)

---

### День 3-4: Функции + документирование
```python
# Функции - основа всех тестов
def calculate_discount(price, discount_percent=10):
    """Calculate final price after discount.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (default 10)
    
    Returns:
        Final price after discount
    """
    return price * (1 - discount_percent/100)

# Позови:
final_price = calculate_discount(100, 20)
print(final_price)  # 80
```

**Ресурс:** Real Python - Functions (1 час)

---

### День 5-6: Классы и объекты
```python
# Классы - основа Page Object Model дальше
class User:
    def __init__(self, name, email, role="user"):
        self.name = name
        self.email = email
        self.role = role
    
    def can_delete(self):
        """Check if user has permission to delete"""
        return self.role == "admin"
    
    def __str__(self):
        return f"{self.name} ({self.email})"

# Использование
admin = User("Daniil", "daniil@example.com", role="admin")
print(admin)  # Daniil (daniil@example.com)
print(admin.can_delete())  # True
```

**Ресурс:** Real Python - Object-Oriented Programming (2 часа)

---

### День 7: Практика + Code Review
**Проект:** CLI скрипт "User Manager"
```python
# users.py - полное приложение
class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, name, email):
        """Add new user"""
        user = User(name, email)
        self.users.append(user)
        return user
    
    def find_user(self, email):
        """Find user by email"""
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def list_users(self):
        """List all users"""
        return self.users

# main.py
if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Daniil", "daniil@test.com")
    manager.add_user("Maria", "maria@test.com")
    
    for user in manager.list_users():
        print(user)
```

**Deliverable:** GitHub repo `python-fundament` с этим кодом + README

---

## Неделя 2: Файлы, JSON, ошибки, модули

### День 1-2: File I/O и JSON
```python
import json

# Читать JSON
with open("users.json", "r") as f:
    data = json.load(f)

# Писать JSON
users_data = [
    {"name": "Daniil", "email": "daniil@test.com"},
    {"name": "Maria", "email": "maria@test.com"}
]

with open("users.json", "w") as f:
    json.dump(users_data, f, indent=2)

# Парсить JSON из строки
json_string = '{"name": "Test", "status": "active"}'
parsed = json.loads(json_string)
print(parsed["name"])  # Test
```

**Ресурс:** Real Python - Working with Files (1 час)

---

### День 3-4: Обработка ошибок
```python
# try/except - критично для тестов и API
def load_user_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in {filename}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Кастомные исключения
class UserError(Exception):
    """Base user error"""
    pass

class UserNotFoundError(UserError):
    """User not found"""
    pass

def get_user_or_fail(email):
    # ... search logic ...
    if not found:
        raise UserNotFoundError(f"User {email} not found")
```

**Ресурс:** Real Python - Exception Handling (1 час)

---

### День 5-6: Модули, структура проекта, requirements.txt
```
project/
├── main.py
├── models.py
├── utils.py
├── data/
│   └── users.json
├── tests/
│   ├── test_models.py
│   └── test_utils.py
├── requirements.txt
└── README.md
```

```python
# main.py
from models import User, UserManager
from utils import load_json, save_json

# models.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# utils.py
import json

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
```

```
# requirements.txt
requests==2.31.0
pytest==7.4.3
python-dotenv==1.0.0
```

**Ресурс:** Real Python - Modules and Packages (1 час)

---

### День 7: Requests библиотека - первый API запрос
```python
import requests
import json

# GET запрос
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)  # 200
data = response.json()
print(data["name"])  # Leanne Graham

# POST запрос
payload = {
    "title": "Test Post",
    "body": "This is a test",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)
print(response.status_code)  # 201
print(response.json())

# Headers и параметры
headers = {"Authorization": "Bearer token123"}
params = {"page": 1, "limit": 10}

response = requests.get(
    "https://api.example.com/users",
    headers=headers,
    params=params
)
```

**Deliverable:** Фаза 0 готова - GitHub repo с полноценным Python проектом

---

# ФАЗА 1: BACKEND - FastAPI + Database (Недели 3-4)

## Цель
Построить простой REST API который будешь потом тестировать. Понять сторону сервера.

## Неделя 3: FastAPI основы

### День 1-2: Установка и Hello World
```python
# pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Модель данных
class User(BaseModel):
    id: int
    name: str
    email: str

# GET запрос
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# GET с параметром
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "John"}

# POST запрос
@app.post("/users/")
def create_user(user: User):
    return {"created": user}

# Запустить: uvicorn main:app --reload
# http://localhost:8000/docs - автоматическая документация!
```

**Ресурс:** FastAPI official docs - First Steps (1 час)

---

### День 3-4: CRUD операции
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory database (потом заменим на реальную БД)
users_db = []

@app.get("/users", response_model=List[User])
def list_users():
    """Get all users"""
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    """Get user by ID"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/", response_model=User)
def create_user(user: User):
    """Create new user"""
    users_db.append(user.dict())
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    """Update user"""
    for i, u in enumerate(users_db):
        if u["id"] == user_id:
            users_db[i] = user.dict()
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete user"""
    global users_db
    users_db = [u for u in users_db if u["id"] != user_id]
    return {"deleted": user_id}
```

**Ресурс:** FastAPI - Creating and Reading Models (1 час)

---

### День 5-6: Валидация, ошибки, документирование
```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr  # Автоматическая валидация email
    age: int = Field(..., ge=0, le=150)
    is_active: bool = True
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "age": 25,
                "is_active": True
            }
        }

app = FastAPI(
    title="User API",
    description="API for managing users",
    version="1.0.0"
)

@app.post("/users/", response_model=User)
def create_user(user: User):
    """
    Create a new user.
    
    - **name**: User full name (1-100 chars)
    - **email**: Valid email address
    - **age**: Age between 0 and 150
    """
    # Проверка дублей по email
    # ... логика ...
    return user

@app.get("/users/")
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    is_active: Optional[bool] = None
):
    """
    Get list of users with pagination.
    
    - **skip**: Number of users to skip (default 0)
    - **limit**: Max users to return (default 10, max 100)
    - **is_active**: Filter by active status (optional)
    """
    # Фильтрация и пагинация
    pass
```

**Ресурс:** FastAPI - Request Body, Query Parameters (2 часа)

---

### День 7: Тестирование API вручную + Postman
```python
# Запусти API: uvicorn main:app --reload

# Используй встроенный Swagger UI:
# http://localhost:8000/docs

# Или ReDoc:
# http://localhost:8000/redoc

# Или Postman (скачай и импортируй)
```

**Deliverable:** Работающий FastAPI сервис с 5+ endpoint-ами

---

## Неделя 4: Database интеграция

### День 1-2: SQLite basics (простейший вариант для старта)
```python
import sqlite3
from datetime import datetime

# Создать БД
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# Создать таблицу
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# INSERT
cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    ("Daniil", "daniil@test.com")
)
conn.commit()

# SELECT
cursor.execute("SELECT * FROM users WHERE email = ?", ("daniil@test.com",))
user = cursor.fetchone()
print(user)  # (1, 'Daniil', 'daniil@test.com', '2026-10-07 13:20:00')

# UPDATE
cursor.execute(
    "UPDATE users SET name = ? WHERE email = ?",
    ("Daniil Morzhevskyi", "daniil@test.com")
)
conn.commit()

# DELETE
cursor.execute("DELETE FROM users WHERE email = ?", ("daniil@test.com",))
conn.commit()

conn.close()
```

---

### День 3-4: SQLAlchemy ORM (лучше, чем raw SQL)
```python
# pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# База данных
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Модель
class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Создать таблицы
Base.metadata.create_all(bind=engine)

# CRUD операции
def create_user(name, email):
    db = SessionLocal()
    user = UserModel(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(user_id):
    db = SessionLocal()
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def list_users():
    db = SessionLocal()
    return db.query(UserModel).all()

def update_user(user_id, name):
    db = SessionLocal()
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        user.name = name
        db.commit()
    return user

def delete_user(user_id):
    db = SessionLocal()
    db.query(UserModel).filter(UserModel.id == user_id).delete()
    db.commit()
```

---

### День 5-6: Интеграция SQLAlchemy с FastAPI
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency - получить сессию БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True  # Для преобразования ORM -> Pydantic

@app.get("/users/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db.query(UserModel).filter(UserModel.id == user_id).delete()
    db.commit()
    return {"deleted": user_id}
```

---

### День 7: Project структура + полировка
```
qa-ai-automation-suite/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # DB config
│   └── crud.py              # CRUD functions
├── tests/
│   └── test_api.py          # API тесты (позже)
├── app.db                   # SQLite (git ignore)
├── requirements.txt
├── .env.example
└── README.md
```

**Deliverable:** Работающий FastAPI сервис с БД на GitHub

---

# ФАЗА 2: QA CORE - PYTEST + AUTOMATION (Недели 5-8)

## Цель
Полное покрытие API и UI тестами. Это ядро QA инженера.

## Неделя 5: Pytest основы

### День 1-2: Установка и первые тесты
```python
# pip install pytest pytest-cov

# test_simple.py
def test_addition():
    assert 2 + 2 == 4

def test_string():
    name = "Daniil"
    assert name.startswith("D")
    assert len(name) == 6

def test_list():
    items = [1, 2, 3]
    assert 2 in items
    assert len(items) == 3

# Запуск: pytest test_simple.py -v
# -v для verbose вывода
```

**Ресурс:** pytest.org - Getting Started (1 час)

---

### День 3-4: Фикстуры - основа тестов
```python
import pytest
from app.main import app, User
from fastapi.testclient import TestClient

# Фикстура - переиспользуемая подготовка
@pytest.fixture
def client():
    """Клиент для тестирования API"""
    return TestClient(app)

@pytest.fixture
def sample_user():
    """Sample user для тестов"""
    return {
        "name": "Test User",
        "email": "test@example.com"
    }

# Использование
def test_create_user(client, sample_user):
    response = client.post("/users/", json=sample_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == sample_user["name"]

def test_get_user(client, sample_user):
    # Создаём
    create_response = client.post("/users/", json=sample_user)
    user_id = create_response.json()["id"]
    
    # Получаем
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == sample_user["name"]

# Фикстуры с setup/teardown
@pytest.fixture
def db_with_users():
    """БД с предзагруженными пользователями"""
    # Setup
    db = SessionLocal()
    user1 = UserModel(name="User 1", email="user1@test.com")
    user2 = UserModel(name="User 2", email="user2@test.com")
    db.add_all([user1, user2])
    db.commit()
    
    yield db  # Тест запускается здесь
    
    # Teardown (очистка)
    db.query(UserModel).delete()
    db.commit()
    db.close()

def test_list_users(db_with_users):
    users = db_with_users.query(UserModel).all()
    assert len(users) == 2
```

**Ресурс:** pytest.org - Fixtures (2 часа)

---

### День 5-6: Параметризация и группировка
```python
# Параметризация - тестировать разные варианты
@pytest.mark.parametrize("email,expected_valid", [
    ("test@example.com", True),
    ("invalid-email", False),
    ("test@", False),
    ("@example.com", False),
])
def test_email_validation(email, expected_valid):
    result = validate_email(email)
    assert result == expected_valid

# Тестирование разных статус-кодов
@pytest.mark.parametrize("method,endpoint,status_code", [
    ("GET", "/users/", 200),
    ("GET", "/users/999", 404),
    ("POST", "/users/", 400),  # Missing fields
])
def test_api_status_codes(client, method, endpoint, status_code):
    if method == "GET":
        response = client.get(endpoint)
    elif method == "POST":
        response = client.post(endpoint, json={})
    
    assert response.status_code == status_code

# Группировка тестов в классы
class TestUserAPI:
    """Тесты для User API"""
    
    def test_create_user(self, client, sample_user):
        response = client.post("/users/", json=sample_user)
        assert response.status_code == 201
    
    def test_get_user(self, client):
        # ...
        pass
    
    def test_update_user(self, client):
        # ...
        pass
    
    def test_delete_user(self, client):
        # ...
        pass

# Запуск только одного класса:
# pytest test_api.py::TestUserAPI -v

# Или только одного теста:
# pytest test_api.py::TestUserAPI::test_create_user -v
```

---

### День 7: Assertions и сообщения об ошибках
```python
# Базовые assertions
assert value == expected
assert value != expected
assert value > expected
assert value in collection
assert callable(func)
assert isinstance(obj, SomeClass)

# Более понятные сообщения
def test_with_message():
    result = get_user(999)
    assert result is not None, f"User 999 should exist"

# pytest -vv показывает полные различия
def test_list_comparison():
    expected = [1, 2, 3, 4, 5]
    actual = [1, 2, 4, 5]
    assert actual == expected  # pytest покажет чего не хватает

# Для JSON
def test_response_structure():
    response = client.get("/users/1")
    data = response.json()
    
    assert "id" in data, "Response should contain 'id'"
    assert "name" in data, "Response should contain 'name'"
    assert "email" in data, "Response should contain 'email'"
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
```

**Deliverable:** 20+ тестов для FastAPI в repo

---

## Неделя 6: API тестирование в полном объёме

### День 1-2: Тестирование CRUD операций
```python
# conftest.py - общие фикстуры для всех тестов
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.models import Base, UserModel
from app.database import get_db

# Test DB
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def cleanup():
    """Очистить БД перед каждым тестом"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

# tests/test_users.py
class TestUserCRUD:
    """Тесты для CRUD операций"""
    
    def test_create_user(self, client):
        """POST /users/ должен создать пользователя"""
        user_data = {"name": "John", "email": "john@test.com"}
        response = client.post("/users/", json=user_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "John"
        assert data["email"] == "john@test.com"
        assert "id" in data
    
    def test_read_user(self, client):
        """GET /users/{id} должен вернуть пользователя"""
        # Create
        user_data = {"name": "Jane", "email": "jane@test.com"}
        create_response = client.post("/users/", json=user_data)
        user_id = create_response.json()["id"]
        
        # Read
        response = client.get(f"/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == user_id
        assert data["name"] == "Jane"
    
    def test_read_nonexistent_user(self, client):
        """GET /users/999 должен вернуть 404"""
        response = client.get("/users/999")
        assert response.status_code == 404
    
    def test_update_user(self, client):
        """PUT /users/{id} должен обновить пользователя"""
        # Create
        user_data = {"name": "Bob", "email": "bob@test.com"}
        create_response = client.post("/users/", json=user_data)
        user_id = create_response.json()["id"]
        
        # Update
        update_data = {"name": "Robert", "email": "robert@test.com"}
        response = client.put(f"/users/{user_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Robert"
        assert data["email"] == "robert@test.com"
    
    def test_delete_user(self, client):
        """DELETE /users/{id} должен удалить пользователя"""
        # Create
        user_data = {"name": "Alice", "email": "alice@test.com"}
        create_response = client.post("/users/", json=user_data)
        user_id = create_response.json()["id"]
        
        # Delete
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 200
        
        # Verify deleted
        get_response = client.get(f"/users/{user_id}")
        assert get_response.status_code == 404

class TestUserList:
    """Тесты для листинга пользователей"""
    
    def test_list_empty(self, client):
        """GET /users/ на пустой БД должен вернуть []"""
        response = client.get("/users/")
        assert response.status_code == 200
        assert response.json() == []
    
    def test_list_multiple(self, client):
        """GET /users/ должен вернуть всех пользователей"""
        # Create 3 users
        for i in range(3):
            user_data = {"name": f"User {i}", "email": f"user{i}@test.com"}
            client.post("/users/", json=user_data)
        
        response = client.get("/users/")
        assert response.status_code == 200
        assert len(response.json()) == 3
    
    @pytest.mark.parametrize("skip,limit,expected_count", [
        (0, 10, 3),  # Все 3
        (0, 2, 2),   # Первые 2
        (1, 10, 2),  # Пропустить 1
    ])
    def test_pagination(self, client, skip, limit, expected_count):
        """GET /users/?skip=X&limit=Y должен вернуть пагинированный список"""
        # Create 3 users
        for i in range(3):
            user_data = {"name": f"User {i}", "email": f"user{i}@test.com"}
            client.post("/users/", json=user_data)
        
        response = client.get(f"/users/?skip={skip}&limit={limit}")
        assert response.status_code == 200
        assert len(response.json()) == expected_count
```

---

### День 3-4: Негативное тестирование (error cases)
```python
class TestUserValidation:
    """Тесты на валидацию данных"""
    
    def test_create_user_missing_name(self, client):
        """POST без name должен вернуть 422"""
        user_data = {"email": "test@test.com"}
        response = client.post("/users/", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_missing_email(self, client):
        """POST без email должен вернуть 422"""
        user_data = {"name": "Test"}
        response = client.post("/users/", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_invalid_email(self, client):
        """POST с невалидным email должен вернуть 422"""
        user_data = {"name": "Test", "email": "not-an-email"}
        response = client.post("/users/", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_duplicate_email(self, client):
        """Два пользователя с одинаковым email должны вернуть ошибку"""
        user_data = {"name": "User 1", "email": "same@test.com"}
        
        # Первый - OK
        response1 = client.post("/users/", json=user_data)
        assert response1.status_code == 201
        
        # Второй - должен вернуть ошибку
        response2 = client.post("/users/", json=user_data)
        assert response2.status_code == 400  # или 409 conflict
    
    @pytest.mark.parametrize("invalid_data", [
        {},  # Empty
        {"name": ""},  # Empty name
        {"name": "Test", "email": ""},  # Empty email
        {"name": "Test", "email": None},  # None email
    ])
    def test_create_user_invalid_data(self, client, invalid_data):
        """Различные невалидные данные должны вернуть ошибку"""
        response = client.post("/users/", json=invalid_data)
        assert response.status_code in [400, 422]

class TestUserEdgeCases:
    """Граничные случаи"""
    
    def test_get_user_negative_id(self, client):
        """GET с отрицательным ID должен вернуть 404"""
        response = client.get("/users/-1")
        assert response.status_code == 404
    
    def test_get_user_zero_id(self, client):
        """GET с ID=0 должен вернуть 404"""
        response = client.get("/users/0")
        assert response.status_code == 404
    
    def test_get_user_string_id(self, client):
        """GET с строковым ID должен вернуть ошибку"""
        response = client.get("/users/abc")
        assert response.status_code in [404, 422]
    
    def test_update_nonexistent_user(self, client):
        """PUT несуществующего пользователя должен вернуть 404"""
        update_data = {"name": "Test", "email": "test@test.com"}
        response = client.put("/users/999", json=update_data)
        assert response.status_code == 404
    
    def test_delete_already_deleted_user(self, client):
        """DELETE уже удалённого пользователя должен вернуть 404"""
        # Create
        user_data = {"name": "Test", "email": "test@test.com"}
        create_response = client.post("/users/", json=user_data)
        user_id = create_response.json()["id"]
        
        # Delete once
        client.delete(f"/users/{user_id}")
        
        # Delete again - should fail
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 404
```

---

### День 5-6: Проверка response схемы и performance
```python
import time
from jsonschema import validate, ValidationError

class TestResponseSchema:
    """Проверка структуры ответа"""
    
    user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string", "format": "email"},
            "created_at": {"type": "string"}
        },
        "required": ["id", "name", "email"]
    }
    
    def test_user_response_schema(self, client):
        """Ответ должен соответствовать схеме"""
        user_data = {"name": "Test", "email": "test@test.com"}
        response = client.post("/users/", json=user_data)
        data = response.json()
        
        # Валидировать против схемы
        try:
            validate(instance=data, schema=self.user_schema)
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e.message}")

class TestPerformance:
    """Тесты на производительность"""
    
    def test_list_users_performance(self, client):
        """GET /users/ должен ответить за < 100ms"""
        # Create 100 users
        for i in range(100):
            user_data = {"name": f"User {i}", "email": f"user{i}@test.com"}
            client.post("/users/", json=user_data)
        
        # Measure
        start = time.time()
        response = client.get("/users/")
        elapsed = time.time() - start
        
        assert response.status_code == 200
        assert elapsed < 0.1, f"Request took {elapsed}s, expected < 0.1s"
    
    def test_create_user_performance(self, client):
        """POST /users/ должен создать пользователя за < 50ms"""
        user_data = {"name": "Test", "email": "test@test.com"}
        
        start = time.time()
        response = client.post("/users/", json=user_data)
        elapsed = time.time() - start
        
        assert response.status_code == 201
        assert elapsed < 0.05, f"Request took {elapsed}s, expected < 0.05s"
```

---

### День 7: Отчёты и мониторинг
```python
# requirements.txt
pytest==7.4.3
pytest-cov==4.1.0       # Coverage report
pytest-html==3.2.0      # HTML report
pytest-xdist==3.3.1     # Parallel execution

# Запуск с coverage:
# pytest tests/ --cov=app --cov-report=html

# Запуск с HTML отчётом:
# pytest tests/ --html=report.html --self-contained-html

# Запуск параллельно (на 4 CPU):
# pytest tests/ -n 4

# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = --strict-markers -v
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
```

**Deliverable:** 50+ API тестов с отчётами, 80%+ code coverage

---

## Неделя 7: UI тестирование с Playwright

### День 1-2: Playwright basics
```python
# pip install playwright pytest-playwright

# test_ui_simple.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

def test_google_search(page):
    """Простой тест поиска в Google"""
    page.goto("https://www.google.com")
    
    # Найти input
    page.fill('input[name="q"]', "Playwright")
    
    # Нажать Enter
    page.press('input[name="q"]', "Enter")
    
    # Дождаться результатов
    page.wait_for_selector(".g")
    
    # Проверить что результаты есть
    results = page.query_selector_all(".g")
    assert len(results) > 0
```

---

### День 3-4: Page Object Model (POM)
```python
# pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page
    
    def wait_for_navigation(self):
        """Дождаться загрузки страницы"""
        self.page.wait_for_load_state("networkidle")
    
    def click(self, selector):
        """Клик с ожиданием"""
        self.page.click(selector)
    
    def fill(self, selector, text):
        """Заполнить input"""
        self.page.fill(selector, text)
    
    def get_text(self, selector):
        """Получить текст"""
        return self.page.text_content(selector)
    
    def is_visible(self, selector):
        """Проверить видимость"""
        return self.page.is_visible(selector)

# pages/login_page.py
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "http://localhost:8000/login"
    
    def login(self, email, password):
        """Процесс логина"""
        self.page.goto(self.url)
        self.fill('#email', email)
        self.fill('#password', password)
        self.click('button[type="submit"]')
        self.wait_for_navigation()
    
    def get_error_message(self):
        """Получить сообщение об ошибке"""
        return self.get_text('.error-message')
    
    def is_error_visible(self):
        """Проверить видимость ошибки"""
        return self.is_visible('.error-message')

# pages/user_page.py
class UserPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def get_username(self):
        """Получить имя пользователя на странице"""
        return self.get_text('.username')
    
    def click_logout(self):
        """Клик на logout"""
        self.click('button:has-text("Logout")')
        self.wait_for_navigation()

# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.user_page import UserPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def user_page(page):
    return UserPage(page)

class TestLogin:
    def test_successful_login(self, login_page, user_page):
        """Успешный логин"""
        login_page.login("test@test.com", "password123")
        
        # На странице профиля
        assert user_page.get_username() == "Test User"
    
    def test_invalid_email(self, login_page):
        """Неверный email должен вернуть ошибку"""
        login_page.login("invalid-email", "password123")
        
        assert login_page.is_error_visible()
        assert "Invalid email" in login_page.get_error_message()
    
    def test_wrong_password(self, login_page):
        """Неверный пароль должен вернуть ошибку"""
        login_page.login("test@test.com", "wrongpassword")
        
        assert login_page.is_error_visible()
        assert "Invalid credentials" in login_page.get_error_message()
    
    @pytest.mark.parametrize("email,password", [
        ("", "password"),  # Empty email
        ("test@test.com", ""),  # Empty password
        ("", ""),  # Both empty
    ])
    def test_empty_fields(self, login_page, email, password):
        """Пустые поля должны вернуть ошибку"""
        login_page.login(email, password)
        
        assert login_page.is_error_visible()
```

---

### День 5-6: Скриншоты, видео, трассировка
```python
@pytest.fixture
def page_with_screenshots(page):
    """Автоматические скриншоты при падении"""
    yield page
    # После теста
    # Скриншоты уже сохранены

def test_with_screenshot(page):
    page.goto("https://example.com")
    
    # Сохранить скриншот
    page.screenshot(path="screenshots/example.png")
    
    # Проверить
    assert page.is_visible("body")

# conftest.py с видеозаписью
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        record_video_dir="videos/"  # Записывать видео
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()

# Трассировка для debug
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    
    context.tracing.start(sources=True, screenshots=True, snapshots=True)
    yield page
    
    context.tracing.stop(path="trace.zip")
    page.close()
    context.close()

# Просмотр трассировки: npx playwright show-trace trace.zip
```

---

### День 7: Интеграция UI + API тестов
```python
# tests/test_e2e.py
"""End-to-end тесты: API + UI"""

class TestE2E:
    def test_create_user_via_api_login_via_ui(self, page, client):
        """Создать пользователя через API, залогиниться через UI"""
        # 1. Создать пользователя через API
        user_data = {"name": "E2E Test", "email": "e2e@test.com", "password": "pass123"}
        api_response = client.post("/users/", json=user_data)
        assert api_response.status_code == 201
        user_id = api_response.json()["id"]
        
        # 2. Залогиниться через UI
        login_page = LoginPage(page)
        login_page.login("e2e@test.com", "pass123")
        
        # 3. Проверить что на странице появился правильный пользователь
        user_page = UserPage(page)
        assert user_page.get_username() == "E2E Test"
```

**Deliverable:** 20+ UI тестов с POM, скриншоты, видео, E2E примеры

---

## Неделя 8: Полировка, отчёты, структура

### День 1-2: Структура проекта как профессионал
```
qa-ai-automation-suite/
├── app/                       # FastAPI приложение
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
├── tests/                      # Тесты
│   ├── conftest.py            # Фикстуры
│   ├── unit/                  # Unit тесты
│   │   └── test_models.py
│   ├── api/                   # API тесты
│   │   ├── test_users.py
│   │   ├── test_auth.py
│   │   └── test_validation.py
│   ├── ui/                    # UI тесты
│   │   ├── pages/
│   │   │   ├── base_page.py
│   │   │   ├── login_page.py
│   │   │   └── user_page.py
│   │   ├── test_login.py
│   │   └── test_user_profile.py
│   └── e2e/                   # End-to-end тесты
│       └── test_workflows.py
├── config/
│   ├── test_config.py
│   └── settings.py
├── utils/                      # Утилиты
│   ├── logger.py
│   ├── helpers.py
│   └── constants.py
├── reports/                    # Отчёты (git ignore)
│   ├── html/
│   ├── coverage/
│   └── videos/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .github/workflows/          # CI/CD
│   └── tests.yml
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt        # Для разработки
├── .gitignore
├── .env.example
└── README.md
```

---

### День 3-4: Allure отчёты (профессиональнее чем HTML)
```python
# pip install allure-pytest

# conftest.py
import allure

@pytest.fixture
def client():
    allure.attach("Test Client Created", "Client Setup")
    return TestClient(app)

# tests/test_users.py
@allure.title("Create User")
@allure.description("Test creating a new user via API")
@allure.tag("api", "critical")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user(client, sample_user):
    """Создание пользователя"""
    with allure.step("Send POST request"):
        response = client.post("/users/", json=sample_user)
    
    with allure.step("Verify response status"):
        assert response.status_code == 201
    
    with allure.step("Verify response data"):
        data = response.json()
        assert data["name"] == sample_user["name"]
        assert data["email"] == sample_user["email"]
        
        # Прикрепить данные к отчёту
        allure.attach(
            str(data),
            "Response Data",
            allure.attachment_type.JSON
        )

# Запуск с Allure:
# pytest tests/ --alluredir=allure-results
# allure serve allure-results
```

---

### День 5-6: Логирование и debug
```python
# utils/logger.py
import logging
import sys

def get_logger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

# conftest.py
import logging
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture
def client(caplog):
    caplog.set_level(logging.INFO)
    logger.info("Creating test client")
    
    client = TestClient(app)
    yield client
    
    logger.info(f"Test logs:\n{caplog.text}")

# tests/test_users.py
def test_create_user(client, caplog):
    logger = logging.getLogger(__name__)
    logger.info("Starting test_create_user")
    
    user_data = {"name": "Test", "email": "test@test.com"}
    logger.debug(f"User data: {user_data}")
    
    response = client.post("/users/", json=user_data)
    logger.info(f"Response status: {response.status_code}")
    
    assert response.status_code == 201
```

---

### День 7: CI/CD + деплой (будет на неделе 9, но подготовим)
```yaml
# .github/workflows/tests.yml
name: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
    
    - name: Run API tests
      run: pytest tests/api -v --cov=app --cov-report=xml
    
    - name: Run UI tests
      run: pytest tests/ui -v
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

**Deliverable:** Фаза 2 готова - полное покрытие, Allure отчёты, CI/CD setup

---

# ФАЗА 3: DEVOPS - CI/CD + DOCKER (Недели 9-10)

## Неделя 9: Docker контейнеризация

### День 1-2: Dockerfile и image
```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Зависимости ОС
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Playwright browser
RUN playwright install chromium
RUN playwright install-deps

# Код
COPY app/ ./app/
COPY tests/ ./tests/
COPY pytest.ini .

# Запуск тестов
CMD ["pytest", "tests/", "-v", "--html=reports/report.html"]
```

```bash
# Построить image
docker build -t qa-automation:latest .

# Запустить тесты в контейнере
docker run --rm -v $(pwd)/reports:/app/reports qa-automation:latest

# Запустить интерактивно (bash)
docker run -it qa-automation:latest bash
```

---

### День 3-4: Docker Compose (для интеграции с БД)
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/testdb
    depends_on:
      - db
    volumes:
      - ./app:/app/app
      - ./reports:/app/reports
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
  
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: testdb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
  
  tests:
    build: .
    depends_on:
      - app
      - db
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/testdb
      - API_URL=http://app:8000
    volumes:
      - ./reports:/app/reports
    command: pytest tests/ -v --html=reports/report.html

volumes:
  postgres_data:
```

```bash
# Запустить всё (app + db + тесты)
docker-compose up

# Запустить только тесты
docker-compose run tests
```

---

### День 5-7: CI/CD с GitHub Actions
```yaml
# .github/workflows/full-test.yml
name: Full Test Suite

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15-alpine
        env:
          POSTGRES_USER: user
          POSTGRES_PASSWORD: password
          POSTGRES_DB: testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
        playwright install
    
    - name: Start FastAPI app
      run: |
        uvicorn app.main:app &
        sleep 5
      env:
        DATABASE_URL: postgresql://user:password@localhost:5432/testdb
    
    - name: Run API tests
      run: pytest tests/api -v --cov=app --cov-report=xml --html=reports/api.html
      env:
        DATABASE_URL: postgresql://user:password@localhost:5432/testdb
    
    - name: Run UI tests
      run: pytest tests/ui -v --html=reports/ui.html
    
    - name: Run E2E tests
      run: pytest tests/e2e -v --html=reports/e2e.html
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: true
    
    - name: Upload test reports
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: test-reports
        path: reports/
    
    - name: Upload coverage reports
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: coverage-reports
        path: htmlcov/
    
    - name: Comment PR with results
      if: github.event_name == 'pull_request'
      uses: actions/github-script@v6
      with:
        script: |
          github.rest.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: '✅ All tests passed! Reports available in Artifacts.'
          })
```

---

## Неделя 10: Продвинутый CI/CD и мониторинг

### День 1-3: Matrix testing (разные Python версии, браузеры)
```yaml
# .github/workflows/matrix-test.yml
name: Matrix Tests

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        browser: ['chromium', 'firefox', 'webkit']
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        pip install -r requirements-dev.txt
        playwright install ${{ matrix.browser }}
    
    - name: Run tests
      run: pytest tests/ -v --browser=${{ matrix.browser }}
    
    - name: Store results
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: test-results-py${{ matrix.python-version }}-${{ matrix.browser }}
        path: reports/
```

---

### День 4-5: Мониторинг и метрики
```python
# utils/metrics.py
import time
from dataclasses import dataclass

@dataclass
class TestMetrics:
    total_tests: int
    passed: int
    failed: int
    skipped: int
    duration: float
    success_rate: float
    
    def to_json(self):
        return {
            "total": self.total_tests,
            "passed": self.passed,
            "failed": self.failed,
            "skipped": self.skipped,
            "duration_seconds": self.duration,
            "success_rate_percent": self.success_rate * 100
        }

# conftest.py - собрать метрики
@pytest.fixture(scope="session")
def metrics():
    metrics = TestMetrics(
        total_tests=0,
        passed=0,
        failed=0,
        skipped=0,
        duration=0,
        success_rate=0
    )
    return metrics

def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is None:
            # Тест прошёл
            pass

# Отправить метрики в Grafana/Prometheus
import json
import requests

def send_metrics_to_monitoring(metrics):
    payload = metrics.to_json()
    requests.post(
        "http://prometheus:9090/api/v1/write",
        json=payload
    )
```

---

### День 6-7: Automated reporting и alerts
```python
# utils/reporting.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_test_report_email(recipient, test_results, report_html):
    """Отправить отчёт по email при падении тестов"""
    message = MIMEMultipart()
    message["From"] = "qa-bot@example.com"
    message["To"] = recipient
    message["Subject"] = f"Test Report: {test_results['status']}"
    
    body = f"""
    Test Results:
    - Total: {test_results['total']}
    - Passed: {test_results['passed']}
    - Failed: {test_results['failed']}
    - Success Rate: {test_results['success_rate']}%
    
    Full report: {report_html}
    """
    
    message.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("qa-bot@example.com", "password")
        server.send_message(message)

# Trigger на fall
if test_results['failed'] > 0:
    send_test_report_email(
        "team@example.com",
        test_results,
        "reports/report.html"
    )
```

**Deliverable:** Фаза 3 готова - Docker, CI/CD, мониторинг, 100% автоматизация

---

# ФАЗА 4: AI INTEGRATION (Недели 11-14)

## Неделя 11: Claude API основы

### День 1-3: Anthropic SDK
```python
# pip install anthropic

from anthropic import Anthropic

client = Anthropic(api_key="sk-...")

# Простой запрос
message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)
print(message.content[0].text)

# Multi-turn conversation
messages = []

def chat(user_input):
    messages.append({"role": "user", "content": user_input})
    
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=messages
    )
    
    assistant_message = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_message})
    return assistant_message

# Использование
print(chat("What is QA Automation?"))
print(chat("How is it different from manual testing?"))  # Claude помнит контекст

# System prompt
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system="You are an expert QA engineer. Provide detailed explanations.",
    messages=[
        {"role": "user", "content": "Explain test automation framework"}
    ]
)
```

**Ресурс:** docs.anthropic.com

---

### День 4-5: Tool Use (Function Calling)
```python
# AI агент может вызывать функции
tools = [
    {
        "name": "run_test",
        "description": "Run a specific test and return results",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_name": {
                    "type": "string",
                    "description": "Name of test to run"
                },
                "test_file": {
                    "type": "string",
                    "description": "Path to test file"
                }
            },
            "required": ["test_name", "test_file"]
        }
    },
    {
        "name": "get_test_results",
        "description": "Get results of last test run",
        "input_schema": {
            "type": "object",
            "properties": {}
        }
    }
]

def process_tool_use(tool_name, tool_input):
    """Выполнить инструмент"""
    if tool_name == "run_test":
        # Запустить pytest
        import subprocess
        result = subprocess.run(
            ["pytest", tool_input["test_file"], "-v"],
            capture_output=True,
            text=True
        )
        return {
            "status": "success" if result.returncode == 0 else "failed",
            "output": result.stdout + result.stderr
        }
    
    elif tool_name == "get_test_results":
        # Прочитать результаты
        with open("reports/results.json") as f:
            return json.load(f)

# Agentный loop
messages = []

def agent_run_tests(user_request):
    messages.append({"role": "user", "content": user_request})
    
    while True:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        
        # Добавить ответ агента
        messages.append({"role": "assistant", "content": response.content})
        
        # Если Claude хочет использовать tool
        tool_results = []
        for content in response.content:
            if content.type == "tool_use":
                result = process_tool_use(content.name, content.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": content.id,
                    "content": json.dumps(result)
                })
        
        # Если были tools - отправить результаты обратно
        if tool_results:
            messages.append({"role": "user", "content": tool_results})
        else:
            # Агент закончил
            break
    
    return messages[-1].content[0].text

# Использование
result = agent_run_tests("Run all API tests and tell me if they pass")
print(result)
```

---

### День 6-7: AI Test Generator (claude пишет тесты за тебя)
```python
# ai/test_generator.py
from anthropic import Anthropic

class TestGenerator:
    def __init__(self):
        self.client = Anthropic()
    
    def generate_test(self, api_endpoint, description):
        """Claude генерирует тест для API endpoint"""
        prompt = f"""
        Generate a comprehensive pytest test for this API endpoint:
        
        Endpoint: {api_endpoint}
        Description: {description}
        
        Requirements:
        1. Include positive and negative test cases
        2. Test validation and error handling
        3. Use pytest fixtures
        4. Include docstrings
        5. Follow best practices
        
        Return only the Python code, no explanations.
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    def generate_page_object(self, page_description):
        """Claude генерирует Page Object Model"""
        prompt = f"""
        Generate a Playwright Page Object Model for:
        
        {page_description}
        
        Requirements:
        1. Inherit from BasePage
        2. Include selectors as constants
        3. Create methods for user interactions
        4. Use proper waits and assertions
        5. Include docstrings
        
        Return only the Python code.
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text

# Использование
generator = TestGenerator()

# Генерировать тест
test_code = generator.generate_test(
    "POST /users/",
    "Create a new user with name, email, and age"
)
print(test_code)

# Генерировать Page Object
page_object = generator.generate_page_object(
    "Login page with email input, password input, and submit button"
)
print(page_object)

# Сохранить в файл
with open("tests/api/test_generated_users.py", "w") as f:
    f.write(test_code)
```

---

## Неделя 12: RAG система для тестирования

```python
# ai/rag_system.py
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from anthropic import Anthropic

class TestDocumentationRAG:
    def __init__(self):
        self.client = Anthropic()
        self.vectorstore = None
        self.load_documentation()
    
    def load_documentation(self):
        """Загрузить API документацию в векторную БД"""
        # Загрузить все .md файлы
        loader = DirectoryLoader("./docs", glob="**/*.md")
        documents = loader.load()
        
        # Разбить на куски
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(documents)
        
        # Векторизовать и сохранить
        embeddings = HuggingFaceEmbeddings()
        self.vectorstore = Chroma.from_documents(
            chunks,
            embeddings,
            persist_directory="./chroma_db"
        )
    
    def search_documentation(self, query):
        """Найти релевантную документацию"""
        results = self.vectorstore.similarity_search(query, k=3)
        return [doc.page_content for doc in results]
    
    def generate_test_from_docs(self, feature_name):
        """Claude генерирует тест используя документацию как context"""
        # Найти документацию
        docs = self.search_documentation(feature_name)
        
        prompt = f"""
        Based on the following API documentation:
        
        {chr(10).join(docs)}
        
        Generate comprehensive pytest tests for the {feature_name} feature.
        Include all documented requirements and edge cases.
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    def ask_about_api(self, question):
        """Спросить Claude про API используя документацию"""
        docs = self.search_documentation(question)
        
        prompt = f"""
        Based on the API documentation:
        
        {chr(10).join(docs)}
        
        Answer this question: {question}
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text

# Использование
rag = TestDocumentationRAG()

# Спросить про API
answer = rag.ask_about_api("How do I authenticate API requests?")
print(answer)

# Генерировать тесты на основе документации
tests = rag.generate_test_from_docs("User Authentication")
with open("tests/api/test_auth_generated.py", "w") as f:
    f.write(tests)
```

---

## Неделя 13: AI Agentный Test Runner

```python
# ai/test_agent.py
from anthropic import Anthropic
import json
import subprocess

class TestAgent:
    def __init__(self):
        self.client = Anthropic()
        self.messages = []
    
    def setup_tools(self):
        """Инструменты что доступны агенту"""
        return [
            {
                "name": "run_pytest",
                "description": "Run pytest tests",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "test_path": {"type": "string"},
                        "markers": {"type": "string"},
                        "verbose": {"type": "boolean"}
                    }
                }
            },
            {
                "name": "get_test_failures",
                "description": "Get details about test failures"
            },
            {
                "name": "generate_report",
                "description": "Generate test summary report"
            }
        ]
    
    def execute_tool(self, tool_name, tool_input):
        """Выполнить инструмент"""
        if tool_name == "run_pytest":
            cmd = ["pytest", tool_input.get("test_path", "tests/")]
            if tool_input.get("verbose"):
                cmd.append("-v")
            if tool_input.get("markers"):
                cmd.extend(["-m", tool_input["markers"]])
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            return {
                "status": "passed" if result.returncode == 0 else "failed",
                "output": result.stdout,
                "errors": result.stderr
            }
        
        elif tool_name == "get_test_failures":
            with open("reports/failures.json") as f:
                return json.load(f)
        
        elif tool_name == "generate_report":
            return {"report_path": "reports/summary.html"}
    
    def run_autonomous_testing(self, task):
        """Агент самостоятельно запускает тесты и принимает решения"""
        self.messages = [{
            "role": "user",
            "content": f"""
            You are a QA automation agent. Your task:
            
            {task}
            
            Steps to follow:
            1. Run relevant tests
            2. Analyze failures
            3. Generate report
            4. Suggest fixes
            
            Use available tools to complete this task.
            """
        }]
        
        tools = self.setup_tools()
        
        # Agentic loop
        while True:
            response = self.client.messages.create(
                model="claude-opus-4-5",
                max_tokens=2048,
                tools=tools,
                messages=self.messages
            )
            
            # Add response to history
            self.messages.append({"role": "assistant", "content": response.content})
            
            # Check if agent used tools
            tool_results = []
            for content in response.content:
                if content.type == "tool_use":
                    result = self.execute_tool(content.name, content.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": content.id,
                        "content": json.dumps(result)
                    })
            
            if tool_results:
                # Send tool results back
                self.messages.append({"role": "user", "content": tool_results})
            else:
                # Agent finished
                break
        
        # Return final response
        return self.messages[-1].content[0].text

# Использование
agent = TestAgent()

report = agent.run_autonomous_testing(
    "Run all API tests, identify failures, and provide summary"
)
print(report)
```

---

## Неделя 14: AI-Powered Test Optimization

```python
# ai/test_optimizer.py
from anthropic import Anthropic

class TestOptimizer:
    def __init__(self):
        self.client = Anthropic()
    
    def analyze_test_coverage(self, coverage_report):
        """Claude анализирует покрытие и предлагает улучшения"""
        prompt = f"""
        Analyze this test coverage report and suggest improvements:
        
        {coverage_report}
        
        Provide:
        1. Areas with low coverage
        2. Recommendations for new tests
        3. Potential edge cases to cover
        4. Performance optimization suggestions
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    def optimize_slow_tests(self, slow_tests_data):
        """Claude предлагает как ускорить медленные тесты"""
        prompt = f"""
        These tests are slow. Suggest optimizations:
        
        {slow_tests_data}
        
        Consider:
        1. Reducing unnecessary waits
        2. Using parallel execution
        3. Caching test data
        4. Mocking external APIs
        5. Database optimization
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    def detect_flaky_tests(self, test_history):
        """Claude анализирует историю тестов и находит flaky tests"""
        prompt = f"""
        Analyze this test execution history and identify flaky tests:
        
        {test_history}
        
        For each flaky test, explain:
        1. Why it might be flaky
        2. How to stabilize it
        3. Root cause analysis
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text

# Использование
optimizer = TestOptimizer()

# Анализ покрытия
improvements = optimizer.analyze_test_coverage(coverage_data)
print(improvements)

# Оптимизация медленных тестов
optimizations = optimizer.optimize_slow_tests(slow_tests)
print(optimizations)

# Поиск flaky tests
flaky_analysis = optimizer.detect_flaky_tests(test_history)
print(flaky_analysis)
```

**Deliverable:** Фаза 4 готова - полная AI интеграция, генерация тестов, RAG, автономные агенты

---

# ФАЗА 5: PORTFOLIO POLISH + ПРОДВИЖЕНИЕ (Недели 15-16)

## Неделя 15: Полировка проекта

### День 1-2: Идеальный README
```markdown
# QA Automation Suite with AI Integration

## Overview
Production-ready test automation framework combining:
- **API Testing:** pytest + FastAPI + SQLAlchemy
- **UI Testing:** Playwright with Page Object Model
- **AI Integration:** Claude API for test generation and optimization
- **CI/CD:** GitHub Actions + Docker + Allure Reports

## Quick Start

### Prerequisites
- Python 3.12+
- PostgreSQL (Docker recommended)
- Playwright browser drivers

### Installation
```bash
git clone https://github.com/daniil/qa-ai-automation-suite.git
cd qa-ai-automation-suite

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Install Playwright browsers
playwright install
```

### Running Tests
```bash
# All tests
pytest tests/ -v

# API tests only
pytest tests/api -v

# UI tests only
pytest tests/ui -v

# With coverage report
pytest tests/ --cov=app --cov-report=html

# With Allure report
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

### Docker Setup
```bash
docker-compose up  # Starts app + db + runs tests
```

## Project Structure
```
qa-ai-automation-suite/
├── app/              # FastAPI application
├── tests/            # Test suites (API, UI, E2E)
├── ai/               # AI agent and test generation
├── reports/          # Test reports
├── docker/           # Docker configuration
└── .github/          # CI/CD workflows
```

## Features

### API Testing
- 50+ comprehensive API tests
- CRUD operations coverage
- Error handling and validation
- Performance testing

### UI Testing  
- 20+ Playwright tests
- Page Object Model pattern
- Screenshot and video recording
- Cross-browser testing

### AI Integration
- Automatic test generation using Claude API
- RAG system for documentation search
- Autonomous test execution agent
- Test optimization recommendations

### DevOps
- GitHub Actions CI/CD
- Docker containerization
- PostgreSQL database
- Allure test reports
- Code coverage tracking

## Technology Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Testing:** pytest, Playwright, requests
- **Database:** PostgreSQL, SQLite (test)
- **AI:** Claude API, LangChain
- **DevOps:** Docker, GitHub Actions
- **Reporting:** Allure, pytest-html

## Test Coverage
- API: 90%+
- Core functions: 85%+
- Database layer: 80%+

## CI/CD Pipeline
- Automatic tests on push/PR
- Matrix testing (Python versions, browsers)
- Coverage report upload
- Automated notifications

## Performance
- API tests: <100ms per request
- UI tests: Parallel execution
- Full suite: <5 minutes

## Contributing
1. Fork the repository
2. Create feature branch
3. Add tests
4. Submit pull request

## Future Enhancements
- GraphQL API testing
- Load testing with Locust
- Kubernetes deployment
- Advanced AI features (test case generation, anomaly detection)

## License
MIT

## Author
Daniil (@daniil-morzhevskyi)
```

---

### День 3-4: Showcase документация
```markdown
# Showcase: Real-World Examples

## Example 1: Complete User Flow Testing

### API + UI Integration Test
```python
def test_user_signup_and_login_e2e():
    # 1. Create user via API
    user_data = {"name": "John", "email": "john@example.com", "password": "secure123"}
    api_response = api_client.post("/users/", json=user_data)
    assert api_response.status_code == 201
    
    # 2. Login via UI
    login_page.goto("https://app.example.com/login")
    login_page.login("john@example.com", "secure123")
    
    # 3. Verify user is logged in
    dashboard = DashboardPage(page)
    assert "John" in dashboard.get_welcome_message()
```

## Example 2: AI-Generated Tests

```python
# Claude automatically generated this test:
def test_user_profile_update():
    """Test updating user profile via API"""
    # Setup
    user = create_test_user()
    
    # Test
    update_data = {"name": "Jane Doe", "bio": "Updated bio"}
    response = client.put(f"/users/{user.id}", json=update_data)
    
    # Verify
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    
    # Verify in DB
    db_user = db.query(UserModel).filter(UserModel.id == user.id).first()
    assert db_user.name == "Jane Doe"
```

## Example 3: RAG-Powered Test Debugging

When a test fails, Claude analyzes the error using documentation:

```
User: "Why did test_create_user fail with 422?"
Claude: "Based on API documentation, 422 means validation error.
You're sending email='test' but API requires valid email format.
Fix: email='test@example.com'"
```
```

---

### День 5-7: GitHub profile polish + résumé

```markdown
# Daniil Morzhevskyi

## QA Automation Engineer | AI Integration Specialist

Based in Bratislava, Slovakia

### Key Projects

#### QA Automation Suite with AI Integration
- **GitHub:** [qa-ai-automation-suite](https://github.com/daniil/qa-ai-automation-suite)
- **Technologies:** Python, FastAPI, pytest, Playwright, Claude API, Docker
- **Highlights:**
  - 50+ API tests with 90%+ coverage
  - 20+ UI tests using Page Object Model
  - CI/CD pipeline with GitHub Actions
  - AI-powered test generation and optimization
  - 2500+ GitHub stars (hypothetical)

### Skills
- **Languages:** Python, SQL, Bash
- **Testing:** pytest, Playwright, API testing, E2E testing
- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **DevOps:** Docker, GitHub Actions, CI/CD
- **AI:** Claude API, LangChain, RAG systems
- **Cloud:** GCP, AWS (from previous role)

### Experience
- **QA Automation Engineer** (Current)
  - Built production test suite with 100+ tests
  - Integrated AI agents for test optimization
  - Achieved 90%+ code coverage

- **Technical Support & Integration Manager** (MaxBill)
  - 5+ years B2B iGaming integration experience
  - Led support team, managed partner integrations
  - Certified GCP Professional Architect

### Achievements
- Implemented CI/CD pipeline reducing test execution time by 60%
- Created AI-powered test generation saving 20 hours/month
- Trained team on test automation best practices
- Contributed to open source testing libraries

### Social
- GitHub: [@daniil](https://github.com/daniil)
- LinkedIn: [Daniil Morzhevskyi](https://linkedin.com/in/daniil-morzhevskyi)
```

---

## Неделя 16: Продвижение и Next Steps

### День 1-2: Deploy на GitHub Pages
```bash
# Создать gh-pages branch
git checkout --orphan gh-pages

# Копировать отчёты
cp -r reports/* .

# Создать index.html
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>QA Test Reports</title>
</head>
<body>
    <h1>QA Automation Suite - Test Reports</h1>
    <ul>
        <li><a href="api.html">API Tests Report</a></li>
        <li><a href="ui.html">UI Tests Report</a></li>
        <li><a href="coverage/index.html">Code Coverage</a></li>
    </ul>
</body>
</html>
```

```bash
git add .
git commit -m "Add test reports"
git push origin gh-pages

# Теперь доступно: https://daniil.github.io/qa-ai-automation-suite
```

---

### День 3-4: Open Source контрибьюция
```python
# Найти проекты: github.com/topics/pytest, github.com/topics/playwright
# Issues с меткой "good first issue"

# Пример контрибьюции:
# 1. Fork репозиторий
# 2. Создать branch: git checkout -b feature/improve-test-reporting
# 3. Сделать improvement
# 4. Push и создать Pull Request
# 5. Получить feedback от мейнтейнеров

# Это даст:
# ✓ GitHub contributions
# ✓ Feedback от опытных инженеров
# ✓ Portfolio укрепление
```

---

### День 5-7: Job hunt prep
```python
# Обновить LinkedIn
# Отправить 10+ заявок с портфолио
# Подготовить talking points:

talking_points = {
    "What's your testing framework?": """
    I built a comprehensive test automation suite using pytest for API tests
    and Playwright for UI tests. It includes CI/CD with GitHub Actions,
    Docker containerization, and generates Allure reports. The suite covers
    90%+ of the codebase.
    """,
    
    "How do you handle flaky tests?": """
    I analyze test history to identify patterns, use appropriate waits,
    and implement retry logic. I also created an AI agent using Claude API
    that automatically suggests fixes for flaky tests based on test logs.
    """,
    
    "Tell us about your AI experience": """
    I integrated Claude API into my QA automation suite for automatic test
    generation, test optimization, and RAG-powered documentation search.
    Built autonomous test agents that can analyze failures and suggest fixes.
    """,
    
    "Experience with CI/CD": """
    Configured GitHub Actions workflow with matrix testing for different
    Python versions and browsers. Implemented Docker containerization,
    automated test reports, and coverage tracking. Tests run automatically
    on every push and PR.
    """,
}

# Собеседование tips:
# - Show your GitHub portfolio
# - Demonstrate the test suite live
# - Explain AI integration choices
# - Discuss technical trade-offs
# - Show CI/CD pipeline
```

---

## ИТОГОВАЯ АРХИТЕКТУРА

```
┌─────────────────────────────────────┐
│        qa-ai-automation-suite        │
├─────────────────────────────────────┤
│                                     │
│  ┌────────────┐   ┌──────────────┐ │
│  │  FastAPI   │   │  PostgreSQL  │ │
│  │   Backend  │   │   Database   │ │
│  └────────────┘   └──────────────┘ │
│         △                  △        │
│         │                  │        │
│  ┌──────────────────────────────┐  │
│  │      pytest (API Tests)       │  │
│  │                              │  │
│  │  - 50+ comprehensive tests   │  │
│  │  - CRUD operations           │  │
│  │  - Error handling            │  │
│  │  - Performance tests         │  │
│  └──────────────────────────────┘  │
│                                     │
│  ┌──────────────────────────────┐  │
│  │   Playwright (UI Tests)       │  │
│  │                              │  │
│  │  - 20+ UI tests              │  │
│  │  - Page Object Model         │  │
│  │  - Screenshots/Videos        │  │
│  │  - E2E workflows             │  │
│  └──────────────────────────────┘  │
│                                     │
│  ┌──────────────────────────────┐  │
│  │     AI Integration (Claude)   │  │
│  │                              │  │
│  │  - Test generation           │  │
│  │  - RAG documentation search  │  │
│  │  - Autonomous agents         │  │
│  │  - Test optimization         │  │
│  └──────────────────────────────┘  │
│                                     │
├─────────────────────────────────────┤
│  ┌────────────────────────────────┐ │
│  │  GitHub Actions (CI/CD)        │ │
│  │  - Matrix testing              │ │
│  │  - Docker builds               │ │
│  │  - Allure reports              │ │
│  │  - Coverage tracking           │ │
│  └────────────────────────────────┘ │
└─────────────────────────────────────┘
```

---

## УСПЕХ METRICS

По завершении bootcamp ты будешь иметь:

✅ **80 часов вложено**
✅ **2 production-ready проекта на GitHub**
✅ **100+ тестов (API + UI)**
✅ **CI/CD pipeline работающий**
✅ **AI интеграция functioning**
✅ **90%+ code coverage**
✅ **Профессиональное портфолио**

---

## NEXT STEPS ПОСЛЕ BOOTCAMP

1. **Первый месяц:**
   - Подать 20+ заявок на вакансии
   - Получить 3-5 собеседований
   - Улучшать проекты по feedback

2. **Варианты career path:**
   - Junior QA Automation Engineer ($60-80k)
   - AI QA Engineer ($80-100k)
   - Test Architect ($100-150k)

3. **Продолжение обучения:**
   - Advanced Kubernetes (если DevOps интересует)
   - Load testing (Locust, JMeter)
   - API security testing (OWASP)
   - Mobile automation (Appium)

---

**Total time:** 16 недель × 15-20 ч/неделю = **240-320 часов**

**Result:** You're a Junior QA Automation Engineer with AI skills (top 10% of candidates)
