from veho.dict import select_values

current_user = {
    "id": 24,
    "name": "John Doe",
    "website": "http://mywebsite.com",
    "description": "I am an actor",
    "email": "example@example.com",
    "gender": "M",
    "phone_number": "+12345678",
    "username": "johndoe",
    "birth_date": "1991-02-23",
    "followers": 46263,
    "following": 345,
    "like": 204,
    "comments": 9
}

id, email, gender, username, other = select_values(current_user, 'id', 'email', 'gender', 'username', 'other')
print(id, email, gender, username, other)
