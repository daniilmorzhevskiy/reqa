# user = {
#     "id": 1,
#     "name": "Alice",
#     "email": "alice@example.com",
#     "status": "active"
# }

# print(user["name"])
# print(user.get("email"))
# print(user.get("age", "Age not provided"))

# def get_user_info(user_id):
#     if user_id == user["id"]:
#         return user
#     else:
#         return {"id": user_id, "name": "Test User"}

# method = "API"
# endpoint = "https://api.example.com/users/1"
# headers = "CORS"

# def create_request(method, endpoint, headers):
#     print(f"Method: {method}, Endpoint: {endpoint}")
#     print(f"Headers: {headers}")

# # create_request("GET", "/users", authorization="Bearer token123")

# def parse_response_status(status_code):
#     if status_code == 200:
#         return "OK"
#     elif status_code == 404:
#         return "Not Found"
#     else:
#         return "Error"

# get_user_info(1)
# # create_request
# parse_response_status(200)


# def process_api_response(response_data, fields_to_extract):
#     """
#     response_data - dict с ответом API
#     fields_to_extract - list полей которые нужны
#     Вернуть: новый dict только с этими полями
#     """
#     new_dict  = {field: response_data.get(field) for field in fields_to_extract}
#     return new_dict


# users = [
#     {"id": 1, "name": "Alice", "status": "active"},
#     {"id": 2, "name": "Bob", "status": "blocked"},
#     {"id": 3, "name": "Charlie", "status": "active"}
# ]


# def user_status_checker(users):
#     active_users_name = []
#     for user in users:
#         if user['status'] == 'active':
#             active_users_name.append(user['name'])
#     return active_users_name


# users = ["Alice", "Bob", "Charlie", "David", "Eve"]


# response = {
#     "status": 200,
#     "users": [
#         {"id": 1, "name": "Alice", "active": True},
#         {"id": 2, "name": "Bob", "active": False},
#         {"id": 3, "name": "Charlie", "active": True},
#         {"id": 4, "name": "David", "active": True}
#     ]
# }

# def get_active_user_names(response):
#     active_users_name = []
#     for user in response['users']:
#         if user['active']:
#             active_users_name.append(user['name'])
#     return active_users_name

# numbers = [1, 2, 3, 4, 5]
# squared = []

# for n in numbers:
#     squared.append(n ** 2)
# print(squared)

# squared = [n ** 2 for n in numbers]
# print(squared)

# users = [{"id":1, "name":"Alice"}, {"id":2, "name":"Bob"}]
# users_by_id = {user["id"]: user["name"] for user in users}
# print(users_by_id)

# # Task 1
# test_cases = [
#     {"name": "test_login", "status": "passed"},
#     {"name": "test_logout", "status": "failed"},
#     {"name": "test_api", "status": "failed"}
# ]

# failed_tests = [test["name"] for test in test_cases if test["status"] == "failed"]
# print(failed_tests)
import json

def transform_test_data(input_file, output_file):

    with open(input_file, 'r') as f:
        data = json.load(f)
        print("data:", data)

    for item in data:
        item["status"] = item["status"].upper()

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

transform_test_data("test_input.json", "test_output.json")
