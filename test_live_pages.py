from playwright.sync_api import sync_playwright
import time

def test_live():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page(viewport={"width": 1400, "height": 950})
        
        live_url = "https://yousafology.github.io/evoautolocksmith.co.uk/"
        print(f"Navigating to {live_url}...")
        resp = page.goto(live_url, wait_until="networkidle", timeout=30000)
        print(f"HTTP Status: {resp.status}")
        time.sleep(3)
        
        # Take screenshot of live homepage
        page.screenshot(path="C:/Dev/Evo_Auto_Locksmith/snap_live_homepage.png")
        print("Captured snap_live_homepage.png")

        # Scroll down to real Google Map
        map_el = page.locator("#evoLondonGoogleMap")
        if map_el.count() > 0:
            map_el.scroll_into_view_if_needed()
            time.sleep(3)
            page.screenshot(path="C:/Dev/Evo_Auto_Locksmith/snap_live_map.png")
            print("Captured snap_live_map.png")

        # Test live Contact Page
        contact_url = "https://yousafology.github.io/evoautolocksmith.co.uk/contact.html"
        print(f"Navigating to {contact_url}...")
        resp_c = page.goto(contact_url, wait_until="networkidle", timeout=30000)
        print(f"Contact HTTP Status: {resp_c.status}")
        time.sleep(2)
        page.screenshot(path="C:/Dev/Evo_Auto_Locksmith/snap_live_contact.png")
        print("Captured snap_live_contact.png")

        browser.close()

if __name__ == "__main__":
    test_live()
