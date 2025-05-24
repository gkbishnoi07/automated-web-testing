import sys
from playwright.sync_api import sync_playwright

def test_site(target_url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(target_url, timeout=10000)
            title = page.title()
            return {"status": "success", "title": title, "url": page.url}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            browser.close()
