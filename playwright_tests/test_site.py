from playwright.sync_api import sync_playwright
import sys
import json
import os
import base64

def test_website(url):
    result = {
        "url": url,
        "status": "success",
        "title": None,
        "http_status": None,
        "has_title_tag": False,
        "js_errors": [],
        "screenshot_base64": None,
    }

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            js_errors = []
            page.on("pageerror", lambda e: js_errors.append(e.message))

            response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
            result["http_status"] = response.status if response else None

            result["title"] = page.title()
            result["has_title_tag"] = page.locator("title").count() > 0
            result["js_errors"] = js_errors

            # Save screenshot to memory
            screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
            page.screenshot(path=screenshot_path)

            with open(screenshot_path, "rb") as f:
                result["screenshot_base64"] = base64.b64encode(f.read()).decode("utf-8")

            browser.close()

    except Exception as e:
        result["status"] = "error"
        result["message"] = str(e)

    return result

if __name__ == "__main__":
    url = sys.argv[1]
    result = test_website(url)
    print(json.dumps(result, indent=2))
