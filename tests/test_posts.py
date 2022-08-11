import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    response = authorized_client.get("/posts")

    # def validate(post):
    #     return schemas.PostOut(**post)
    # posts_map = map(validate, response.json())
    # posts_list = list(posts_map)
    # assert len(response.json()) == len(test_posts)
    assert response.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    response = client.get("/posts")
    assert response.status_code == 200

def test_unauthorized_user_get_one_post(client, test_posts):
    response = client.get(f"/posts/{test_posts[0].id}")
    print(test_posts[0])
    assert response.status_code == 200

def test_post_with_non_existing_id(authorized_client, test_posts):
    response = authorized_client.get(f"/posts/13123213")
    assert response.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    response = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**response.json())
    assert response.status_code == 200
    assert post.Post.id == test_posts[0].id

# @pytest.mark.parametrize("title, content, published", [
#     ("titoool", "contento", True),
#     ("tetil", "gauga", False),
#     ("awooga", "no biches?", True),
# ])
# def test_create_post(authorized_client, test_user, test_posts, title, content, published):
#     response = authorized_client.post("/posts", json = {"title": title, "content": content, "published": published})
#     created_post = schemas.PostBase(**response.json())
#     assert response.status_code == 201
#     assert created_post.title == title

def test_create_post_default_published_true(authorized_client, test_user):
    response = authorized_client.post("/posts", json = {"title": "arbitrary title", "content": "asdasd"})
    print(response.status_code)  
    created_post = schemas.PostBase(**response.json())  
    assert created_post.published == True
    assert response.status_code == 201

    