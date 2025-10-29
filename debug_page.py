#!/usr/bin/env python3
"""
Debug script to see what's on the Crunchyroll login page
Run this to see all input fields and buttons
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

LOGIN_URL = "https://sso.crunchyroll.com/login?return_url=%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover"

print("""
╔══════════════════════════════════════════════════════════════════╗
║              Crunchyroll Page Debug Tool                        ║
║         Shows all input fields and buttons on page              ║
╚══════════════════════════════════════════════════════════════════╝
""")

print("[*] Initializing Chrome...")
options = uc.ChromeOptions()
options.add_argument('--window-size=1920,1080')

try:
    driver = uc.Chrome(options=options, version_main=141)
    print("[+] Chrome initialized\n")
    
    print(f"[*] Navigating to: {LOGIN_URL}")
    driver.get(LOGIN_URL)
    print("[+] Page loaded")
    
    print("\n[*] Waiting 10 seconds for JavaScript to fully load...")
    time.sleep(10)
    
    # Page info
    print("\n" + "="*60)
    print("PAGE INFORMATION")
    print("="*60)
    print(f"Current URL: {driver.current_url}")
    print(f"Page Title: {driver.title}")
    
    # Find all inputs
    print("\n" + "="*60)
    print("ALL INPUT FIELDS")
    print("="*60)
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"Found {len(inputs)} input fields:\n")
    
    for i, inp in enumerate(inputs, 1):
        try:
            visible = inp.is_displayed()
            input_type = inp.get_attribute("type") or "text"
            input_name = inp.get_attribute("name") or "(no name)"
            input_id = inp.get_attribute("id") or "(no id)"
            input_class = inp.get_attribute("class") or "(no class)"
            input_placeholder = inp.get_attribute("placeholder") or "(no placeholder)"
            
            print(f"Input #{i} {'[VISIBLE]' if visible else '[HIDDEN]'}")
            print(f"  Type: {input_type}")
            print(f"  Name: {input_name}")
            print(f"  ID: {input_id}")
            print(f"  Class: {input_class[:50]}")
            print(f"  Placeholder: {input_placeholder}")
            print()
        except:
            print(f"Input #{i} - Could not read attributes")
            print()
    
    # Find all buttons
    print("="*60)
    print("ALL BUTTONS")
    print("="*60)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"Found {len(buttons)} buttons:\n")
    
    for i, btn in enumerate(buttons, 1):
        try:
            visible = btn.is_displayed()
            btn_type = btn.get_attribute("type") or "(no type)"
            btn_text = btn.text or "(no text)"
            btn_class = btn.get_attribute("class") or "(no class)"
            btn_id = btn.get_attribute("id") or "(no id)"
            
            print(f"Button #{i} {'[VISIBLE]' if visible else '[HIDDEN]'}")
            print(f"  Type: {btn_type}")
            print(f"  Text: {btn_text}")
            print(f"  ID: {btn_id}")
            print(f"  Class: {btn_class[:50]}")
            print()
        except:
            print(f"Button #{i} - Could not read attributes")
            print()
    
    # Find all links
    print("="*60)
    print("ALL LINKS")
    print("="*60)
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Found {len(links)} links (showing first 10):\n")
    
    for i, link in enumerate(links[:10], 1):
        try:
            link_text = link.text or "(no text)"
            link_href = link.get_attribute("href") or "(no href)"
            
            print(f"Link #{i}")
            print(f"  Text: {link_text[:50]}")
            print(f"  Href: {link_href[:80]}")
            print()
        except:
            pass
    
    # Take screenshot
    screenshot_name = "page_debug.png"
    driver.save_screenshot(screenshot_name)
    print(f"\n[+] Screenshot saved: {screenshot_name}")
    
    # Page source preview
    print("\n" + "="*60)
    print("PAGE SOURCE PREVIEW (first 3000 chars)")
    print("="*60)
    print(driver.page_source[:3000])
    print("\n...")
    
    # Save full page source
    with open("page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"\n[+] Full page source saved: page_source.html")
    
    print("\n" + "="*60)
    print("Browser will stay open for 30 seconds for inspection...")
    print("="*60)
    time.sleep(30)
    
    driver.quit()
    print("\n[+] Done!")
    
except Exception as e:
    print(f"\n[-] Error: {e}")
    import traceback
    traceback.print_exc()
