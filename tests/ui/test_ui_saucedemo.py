def test_ui_login_add_to_cart_and_logout(page):
    page.goto("https://www.saucedemo.com/")

    # login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # assert inventory page
    page.wait_for_url("**/inventory.html")
    assert "inventory" in page.url

    # add item
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator(".shopping_cart_link").click()

    # assert cart has item
    assert page.locator(".inventory_item_name").count() >= 1

    # logout
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()
    page.wait_for_url("https://www.saucedemo.com/")
