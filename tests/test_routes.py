def test_home_page_returns_200(client):
    response = client.get("/")

    assert response.status_code == 200


def test_home_page_contains_business_name(client):
    response = client.get("/")

    assert b"Claudia" in response.data


def test_home_page_contains_product_collections(client):
    response = client.get("/")

    assert b"Outdoor Shoes" in response.data
    assert b"Skirts" in response.data


def test_css_file_is_accessible(client):
    response = client.get("/static/css/style.css")

    assert response.status_code == 200


def test_javascript_file_is_accessible(client):
    response = client.get("/static/js/main.js")

    assert response.status_code == 200


def test_homepage_images_are_accessible(client):
    image_paths = [
        "/static/images/hero.jpg",
        "/static/images/outdoor-shoes.jpg",
        "/static/images/skirts.jpg",
    ]

    for path in image_paths:
        response = client.get(path)

        assert response.status_code == 200


def test_custom_404_page(client):
    response = client.get("/this-page-does-not-exist")

    assert response.status_code == 404
    assert b"Page Not Found" in response.data


def test_custom_500_page(client, app):
    app.config["PROPAGATE_EXCEPTIONS"] = False

    def trigger_server_error():
        raise RuntimeError("Test server error")

    app.add_url_rule(
        "/test-server-error",
        view_func=trigger_server_error
    )

    response = client.get("/test-server-error")

    assert response.status_code == 500
    assert b"Something Went Wrong" in response.data