import pytest
from app import schemas
from jose import jwt
from app.config import settings


def test_create_user(client):
    response = client.post("/users", json={"email" : "gauga@gmail.com","password" : "gauga"})
    new_user = schemas.UserResponse(**response.json())
    assert new_user.email == "gauga@gmail.com"
    assert response.status_code == 201

def test_login_user(client, test_user):
    response = client.post("/login", data={"username" : test_user['email'] ,"password" : test_user['password']})
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(login_response.access_token, settings.secret_key, algorithms=[settings.algorithm]) 
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_response.token_type == "bearer"
    assert response.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemailxd@gmail.com", "gauga", 403),
    ("gauga@gmail.com", "wronguspasswordusamogus", 403),
    ("gauga@gmail.com", "gauga", 403),
    (None,"gauga", 422),
    ("gauga@gmail.com", None, 422)
])
def test_failed_login(email, password, status_code, client):
    response = client.post("/login", data={"username" : email ,"password" : password})
    assert response.status_code == status_code
