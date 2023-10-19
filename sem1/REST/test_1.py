from login import login, get_post, create_post
import pytest


def test_step1(login):
    res = get_post(login)
    res_list = res.get("data")
    if not res_list:
        pytest.fail("res_list пуст")
    res_id_list = [item["id"] for item in res_list]
    assert 1234 in res_id_list, "тест не пройден"


def test_create_post(login):
    # Создание нового поста
    title = "Post"
    description = "test description"
    content = "test content"
    post_response = create_post(login, title, description, content)

    assert post_response.get("status") == "success", "Failed to create post"
    posts = get_post(login).get("data", [])
    assert description in [post["description"] for post in posts], "Post not found by description"

if __name__ == '__main__':
    pytest.main(["-vv"])
