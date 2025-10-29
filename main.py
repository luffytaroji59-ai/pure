#!/usr/bin/env python3
"""
Crunchyroll Login Automation - FREE METHOD
Uses undetected-chromedriver to bypass reCAPTCHA v3 without paid services
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

# Login credentials
EMAIL = "luffytaroji50@gmail.com"
PASSWORD = "luffytaroji50@gmail.com"

# URLs
LOGIN_URL = "https://sso.crunchyroll.com/login?return_url=%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover"

# Settings
HEADLESS = False  # Set to True to run without visible browser
WAIT_TIMEOUT = 30  # seconds
SAVE_COOKIES = True
SAVE_SCREENSHOTS = True

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_banner():
    """Print banner"""
    banner = f"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        Crunchyroll Login - FREE reCAPTCHA v3 Bypass             ║
║              Using Undetected ChromeDriver                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

    Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Method: Browser Automation (100% FREE)
    """
    print(banner)

def log(message, level="INFO"):
    """Enhanced logging"""
    timestamp = datetime.now().strftime('%H:%M:%S')
    symbols = {
        "INFO": "[*]",
        "SUCCESS": "[+]",
        "ERROR": "[-]",
        "WARNING": "[!]",
    }
    symbol = symbols.get(level, "[*]")
    print(f"{symbol} [{timestamp}] {message}")

def save_cookies_to_file(driver, filename='crunchyroll_cookies.json'):
    """Save browser cookies to JSON file"""
    try:
        cookies = driver.get_cookies()
        with open(filename, 'w') as f:
            json.dump(cookies, f, indent=2)
        log(f"Cookies saved to {filename}", "SUCCESS")
        return cookies
    except Exception as e:
        log(f"Failed to save cookies: {e}", "ERROR")
        return None

def load_cookies_from_file(driver, filename='crunchyroll_cookies.json'):
    """Load cookies from JSON file"""
    try:
        import os
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                cookies = json.load(f)
            
            # Navigate to domain first
            driver.get("https://sso.crunchyroll.com")
            time.sleep(2)
            
            for cookie in cookies:
                # Remove domain and expiry if present
                if 'domain' in cookie:
                    cookie.pop('domain', None)
                if 'expiry' in cookie:
                    cookie.pop('expiry', None)
                try:
                    driver.add_cookie(cookie)
                except:
                    pass
            
            log(f"Loaded cookies from {filename}", "SUCCESS")
            return True
    except Exception as e:
        log(f"Failed to load cookies: {e}", "WARNING")
    return False

def take_screenshot(driver, name="screenshot"):
    """Take screenshot"""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{name}_{timestamp}.png"
        driver.save_screenshot(filename)
        log(f"Screenshot saved: {filename}", "INFO")
    except Exception as e:
        log(f"Failed to save screenshot: {e}", "WARNING")

def setup_driver():
    """Setup undetected Chrome driver"""
    log("Setting up Chrome driver...", "INFO")
    
    # Try multiple methods to initialize driver
    methods = [
        {"version_main": None, "use_subprocess": False},
        {"version_main": 141, "use_subprocess": False},
        {"version_main": None, "use_subprocess": True},
        {"use_subprocess": True},
    ]
    
    for i, method in enumerate(methods, 1):
        try:
            # Create fresh options for each attempt
            options = uc.ChromeOptions()
            
            # Anti-detection settings
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            
            # User agent
            options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36')
            
            # Window size
            options.add_argument('--window-size=1920,1080')
            
            # Headless mode (optional)
            if HEADLESS:
                options.add_argument('--headless=new')
                log("Running in headless mode", "INFO")
            
            log(f"Attempt {i}/{len(methods)}: Initializing with {method}...", "INFO")
            driver = uc.Chrome(options=options, **method)
            log("Chrome driver initialized successfully! ✓", "SUCCESS")
            return driver
            
        except Exception as e:
            error_msg = str(e)
            log(f"Attempt {i} failed: {error_msg[:100]}...", "WARNING")
            
            # Check for specific errors
            if "version" in error_msg.lower():
                log("Version mismatch detected", "INFO")
            
            if i < len(methods):
                log("Trying alternative method...", "INFO")
            continue
    
    # All methods failed
    log("All initialization methods failed", "ERROR")
    log("", "INFO")
    log("Troubleshooting steps:", "ERROR")
    log("1. Update Chrome: https://www.google.com/chrome/", "INFO")
    log("2. Update undetected-chromedriver:", "INFO")
    log("   pip install --upgrade undetected-chromedriver", "INFO")
    log("3. Clear driver cache:", "INFO")
    log("   rm -rf ~/.local/share/undetected_chromedriver/  # Linux/Mac", "INFO")
    log("   del %APPDATA%\\undetected_chromedriver\\*  # Windows", "INFO")
    
    return None

def wait_for_element(driver, by, value, timeout=WAIT_TIMEOUT, description="element"):
    """Wait for element to be present"""
    try:
        log(f"Waiting for {description}...", "INFO")
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        log(f"Found {description}", "SUCCESS")
        return element
    except Exception as e:
        log(f"Timeout waiting for {description}", "ERROR")
        return None

def login_to_crunchyroll(driver):
    """Main login function"""
    log("=" * 60, "INFO")
    log("Starting Crunchyroll Login Process", "INFO")
    log("=" * 60, "INFO")
    
    try:
        # Navigate to login page
        log(f"Navigating to login page...", "INFO")
        driver.get(LOGIN_URL)
        time.sleep(5)  # Increased wait time
        
        if SAVE_SCREENSHOTS:
            take_screenshot(driver, "01_login_page")
        
        # Wait for page to load and JavaScript to execute
        log("Waiting for page to fully load (JavaScript rendering)...", "INFO")
        time.sleep(5)  # Give more time for dynamic content
        
        # Check if we need to click through any intermediate pages
        log("Checking for intermediate buttons...", "INFO")
        try:
            # Look for "Log In" or "Sign In" link/button on landing page
            intermediate_buttons = [
                (By.XPATH, "//a[contains(text(), 'Log In')]"),
                (By.XPATH, "//button[contains(text(), 'Log In')]"),
                (By.XPATH, "//a[contains(text(), 'Sign In')]"),
                (By.CSS_SELECTOR, "a[href*='login']"),
            ]
            
            for by, selector in intermediate_buttons:
                try:
                    button = driver.find_element(by, selector)
                    log(f"Found intermediate button, clicking it...", "INFO")
                    button.click()
                    time.sleep(3)
                    if SAVE_SCREENSHOTS:
                        take_screenshot(driver, "01b_after_button_click")
                    break
                except:
                    continue
        except:
            pass
        
        # Debug: Print current page info
        log(f"Current URL: {driver.current_url}", "INFO")
        log(f"Page title: {driver.title}", "INFO")
        
        # Debug: Find all input fields
        try:
            all_inputs = driver.find_elements(By.TAG_NAME, "input")
            log(f"Found {len(all_inputs)} input fields on page", "INFO")
            for i, inp in enumerate(all_inputs[:5], 1):  # Show first 5
                input_type = inp.get_attribute("type")
                input_name = inp.get_attribute("name")
                input_id = inp.get_attribute("id")
                input_placeholder = inp.get_attribute("placeholder")
                log(f"  Input {i}: type={input_type}, name={input_name}, id={input_id}, placeholder={input_placeholder}", "DEBUG")
        except Exception as e:
            log(f"Could not debug inputs: {e}", "WARNING")
        
        # Find email input field
        log("Looking for email/login input field...", "INFO")
        email_input = None
        
        # Try multiple selectors - Crunchyroll uses name="login" and type="text"!
        email_selectors = [
            (By.NAME, "login"),  # ← Crunchyroll uses this!
            (By.CSS_SELECTOR, "input[name='login']"),
            (By.XPATH, "//input[@name='login']"),
            (By.ID, "email"),
            (By.NAME, "email"),
            (By.ID, "username"),
            (By.NAME, "username"),
            (By.CSS_SELECTOR, "input[type='email']"),
            (By.CSS_SELECTOR, "input[name='email']"),
            (By.CSS_SELECTOR, "input[name='username']"),
            (By.CSS_SELECTOR, "input[autocomplete='email']"),
            (By.CSS_SELECTOR, "input[autocomplete='username']"),
            (By.XPATH, "//input[@type='email']"),
            (By.XPATH, "//input[@name='email']"),
            (By.XPATH, "//input[@name='username']"),
            (By.XPATH, "//input[contains(@placeholder, 'email')]"),
            (By.XPATH, "//input[contains(@placeholder, 'Email')]"),
            (By.XPATH, "//input[contains(@id, 'email')]"),
            (By.XPATH, "//input[contains(@id, 'user')]"),
        ]
        
        for by, selector in email_selectors:
            try:
                email_input = driver.find_element(by, selector)
                if email_input and email_input.is_displayed():
                    log(f"Found email input using {by}: {selector}", "SUCCESS")
                    break
                else:
                    email_input = None
            except:
                continue
        
        if not email_input:
            log("Could not find email input field!", "ERROR")
            log("Please check screenshots to see what's on the page", "ERROR")
            if SAVE_SCREENSHOTS:
                take_screenshot(driver, "error_no_email_field")
            
            # Try to print page source preview
            try:
                page_source = driver.page_source[:2000]
                log(f"Page source preview: {page_source}", "DEBUG")
            except:
                pass
            
            return False
        
        # Enter email
        log(f"Entering email: {EMAIL}", "INFO")
        email_input.clear()
        time.sleep(0.5)
        email_input.send_keys(EMAIL)
        time.sleep(1)
        
        # Find password input field
        log("Looking for password input field...", "INFO")
        password_input = None
        
        password_selectors = [
            (By.CSS_SELECTOR, "input[type='password']"),  # Most reliable
            (By.XPATH, "//input[@type='password']"),
            (By.ID, "password"),
            (By.NAME, "password"),
            (By.CSS_SELECTOR, "input[name='password']"),
        ]
        
        for by, selector in password_selectors:
            try:
                password_input = driver.find_element(by, selector)
                if password_input and password_input.is_displayed():
                    log(f"Found password input using {by}: {selector}", "SUCCESS")
                    break
                else:
                    password_input = None
            except:
                continue
        
        if not password_input:
            log("Could not find password input field!", "ERROR")
            if SAVE_SCREENSHOTS:
                take_screenshot(driver, "error_no_password_field")
            return False
        
        # Enter password
        log(f"Entering password: {'*' * len(PASSWORD)}", "INFO")
        password_input.clear()
        time.sleep(0.5)
        password_input.send_keys(PASSWORD)
        time.sleep(1)
        
        if SAVE_SCREENSHOTS:
            take_screenshot(driver, "02_credentials_entered")
        
        # Find submit button
        log("Looking for login/submit button...", "INFO")
        submit_button = None
        
        button_selectors = [
            (By.CSS_SELECTOR, "button[type='submit']"),
            (By.XPATH, "//button[@type='submit']"),
            (By.XPATH, "//button[contains(text(), 'Log In')]"),
            (By.XPATH, "//button[contains(text(), 'LOG IN')]"),
            (By.XPATH, "//button[contains(text(), 'Sign In')]"),
            (By.XPATH, "//button[contains(text(), 'SIGN IN')]"),
            (By.XPATH, "//button[contains(., 'Log In')]"),
            (By.XPATH, "//button[contains(., 'Sign In')]"),
            (By.CSS_SELECTOR, "button.submit"),
            (By.CSS_SELECTOR, "input[type='submit']"),
            (By.TAG_NAME, "button"),  # Fallback: any button
        ]
        
        for by, selector in button_selectors:
            try:
                if by == By.TAG_NAME:
                    # Get all buttons and find visible ones
                    buttons = driver.find_elements(by, selector)
                    for btn in buttons:
                        if btn.is_displayed() and btn.get_attribute("type") == "submit":
                            submit_button = btn
                            log(f"Found submit button (fallback method)", "SUCCESS")
                            break
                    if submit_button:
                        break
                else:
                    submit_button = driver.find_element(by, selector)
                    if submit_button and submit_button.is_displayed():
                        log(f"Found submit button using {by}: {selector}", "SUCCESS")
                        break
                    else:
                        submit_button = None
            except:
                continue
        
        if not submit_button:
            log("Could not find submit button!", "ERROR")
            if SAVE_SCREENSHOTS:
                take_screenshot(driver, "error_no_submit_button")
            return False
        
        # Click submit button
        log("Clicking login button...", "INFO")
        submit_button.click()
        
        # Wait for reCAPTCHA to be solved automatically
        log("Waiting for reCAPTCHA to be solved automatically...", "INFO")
        log("(This may take 5-15 seconds)", "INFO")
        time.sleep(8)
        
        if SAVE_SCREENSHOTS:
            take_screenshot(driver, "03_after_submit")
        
        # Wait for redirect or success
        log("Waiting for authentication to complete...", "INFO")
        time.sleep(5)
        
        # Check current URL
        current_url = driver.current_url
        log(f"Current URL: {current_url}", "INFO")
        
        # Check for success indicators
        if 'discover' in current_url or 'callback' in current_url or 'crunchyroll.com' in current_url:
            log("Login appears successful!", "SUCCESS")
            
            if SAVE_SCREENSHOTS:
                take_screenshot(driver, "04_success")
            
            # Save cookies
            if SAVE_COOKIES:
                cookies = save_cookies_to_file(driver)
                log(f"Saved {len(cookies)} cookies", "SUCCESS")
            
            # Print some cookies
            log("Session cookies obtained:", "SUCCESS")
            important_cookies = ['SSID_GuUe', 'cf_clearance', '__cf_bm', 'session_id']
            all_cookies = driver.get_cookies()
            for cookie in all_cookies:
                if cookie['name'] in important_cookies:
                    log(f"  {cookie['name']}: {cookie['value'][:50]}...", "INFO")
            
            return True
            
        elif 'login' in current_url or 'sso' in current_url:
            log("Still on login page - checking for errors...", "WARNING")
            
            if SAVE_SCREENSHOTS:
                take_screenshot(driver, "04_still_on_login")
            
            # Check for error messages
            try:
                error_selectors = [
                    (By.CSS_SELECTOR, ".error"),
                    (By.CSS_SELECTOR, ".error-message"),
                    (By.XPATH, "//*[contains(@class, 'error')]"),
                    (By.XPATH, "//*[contains(text(), 'incorrect')]"),
                    (By.XPATH, "//*[contains(text(), 'invalid')]"),
                ]
                
                for by, selector in error_selectors:
                    try:
                        error_element = driver.find_element(by, selector)
                        if error_element and error_element.text:
                            log(f"Error message: {error_element.text}", "ERROR")
                    except:
                        continue
                        
            except Exception as e:
                log(f"Could not check for error messages: {e}", "WARNING")
            
            log("Login may have failed. Possible causes:", "WARNING")
            log("  • Wrong credentials", "WARNING")
            log("  • reCAPTCHA not solved or rejected", "WARNING")
            log("  • Account locked or requires verification", "WARNING")
            log("  • Need to wait longer for page to load", "WARNING")
            
            return False
        else:
            log(f"Unexpected redirect to: {current_url}", "WARNING")
            
            if SAVE_SCREENSHOTS:
                take_screenshot(driver, "04_unexpected_redirect")
            
            return False
        
    except Exception as e:
        log(f"Exception during login: {str(e)}", "ERROR")
        
        if SAVE_SCREENSHOTS:
            take_screenshot(driver, "error_exception")
        
        return False

def extract_session_data(driver):
    """Extract session data for use in requests"""
    log("=" * 60, "INFO")
    log("Extracting Session Data for API Use", "INFO")
    log("=" * 60, "INFO")
    
    try:
        cookies = driver.get_cookies()
        
        # Convert to requests-compatible format
        cookies_dict = {}
        for cookie in cookies:
            cookies_dict[cookie['name']] = cookie['value']
        
        log(f"Extracted {len(cookies_dict)} cookies", "SUCCESS")
        
        # Save to Python dict format
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"cookies_dict_{timestamp}.py"
        
        with open(filename, 'w') as f:
            f.write("# Crunchyroll Session Cookies\n")
            f.write(f"# Generated: {datetime.now().isoformat()}\n\n")
            f.write("cookies = ")
            f.write(json.dumps(cookies_dict, indent=4))
            f.write("\n")
        
        log(f"Cookie dict saved to: {filename}", "SUCCESS")
        log("You can now use these cookies with requests library!", "INFO")
        
        return cookies_dict
        
    except Exception as e:
        log(f"Failed to extract session data: {e}", "ERROR")
        return None

def print_summary(success, elapsed_time):
    """Print execution summary"""
    print("\n" + "=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)
    print(f"  Status: {'SUCCESS ✓' if success else 'FAILED ✗'}")
    print(f"  Total Time: {elapsed_time:.2f} seconds")
    print(f"  Method: Browser Automation (FREE)")
    print(f"  Cost: $0.00")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main execution function"""
    start_time = time.time()
    driver = None
    
    print_banner()
    
    try:
        # Setup driver
        driver = setup_driver()
        if not driver:
            log("Failed to setup Chrome driver", "ERROR")
            return 1
        
        # Perform login
        success = login_to_crunchyroll(driver)
        
        if success:
            # Extract session data
            log("\nExtracting session data for future use...", "INFO")
            extract_session_data(driver)
            
            # Keep browser open for a moment
            log("\nBrowser will remain open for 10 seconds...", "INFO")
            log("You can manually verify the login was successful", "INFO")
            time.sleep(10)
        else:
            log("\nLogin failed. Browser will remain open for 15 seconds for inspection...", "WARNING")
            time.sleep(15)
        
        elapsed_time = time.time() - start_time
        print_summary(success, elapsed_time)
        
        return 0 if success else 1
        
    except Exception as e:
        log(f"Fatal error: {e}", "ERROR")
        elapsed_time = time.time() - start_time
        print_summary(False, elapsed_time)
        return 1
        
    finally:
        # Close browser
        if driver:
            log("Closing browser...", "INFO")
            try:
                driver.quit()
                log("Browser closed", "SUCCESS")
            except:
                pass

if __name__ == "__main__":
    try:
        exit_code = main()
        exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting...")
        exit(130)
    except Exception as e:
        print(f"\n[-] Fatal error: {e}")
        exit(1)
