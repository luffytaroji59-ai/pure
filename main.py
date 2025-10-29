#!/usr/bin/env python3
"""
Crunchyroll Login Automation with reCAPTCHA v3 Bypass
Uses Anti-Captcha service to automatically solve reCAPTCHA challenges
"""

import requests
import json
import time
import os
import sys
from datetime import datetime
from anticaptchaofficial.recaptchav3proxyless import recaptchaV3Proxyless

# ============================================================================
# CONFIGURATION
# ============================================================================

# API Key - can be set via environment variable or directly here
ANTI_CAPTCHA_API_KEY = os.getenv('ANTI_CAPTCHA_API_KEY', 'YOUR_API_KEY_HERE')

# Login credentials - can be set via environment variables
EMAIL = os.getenv('CRUNCHYROLL_EMAIL', 'luffytaroji50@gmail.com')
PASSWORD = os.getenv('CRUNCHYROLL_PASSWORD', 'luffytaroji50@gmail.com')

# reCAPTCHA settings
WEBSITE_URL = "https://sso.crunchyroll.com/login?return_url=%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover"
RECAPTCHA_SITE_KEY = "6LeQj_wUAAAAABLdMxMxFF-x3Jvyd1hkbsRV9UAk"
PAGE_ACTION = "submit"
MIN_SCORE = 0.3

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
REQUEST_TIMEOUT = 30  # seconds

# Debug settings
DEBUG_MODE = True
SAVE_RESPONSES = True
SAVE_TOKENS = True

# ============================================================================
# COOKIES AND HEADERS
# ============================================================================

cookies = {
    'SSID_GuUe': 'CQAfYB04AAAAAADLVAJpcsWFHMtUAmkBAAAAAAAAAAAAy1QCaQDzVF1dAQMllioAy1QCaQEATF4BAQmoKgDLVAJpAQCLYwEDABQrAMtUAmkBAJxPAQMSQSkAy1QCaQEA',
    'SSSC_GuUe': '972.G7566703555269477746.1|85916.2703634:89437.2790949:89676.2795529:91019.2823168',
    'device_id': 'e3339a43-50bd-4be1-ba19-6caabbf1c95c',
    'ajs_anonymous_id': '7841adf8-85a0-418b-891f-e436a91e568a',
    '_gcl_au': '1.1.1393689531.1761760486',
    'c_locale': 'en-US',
    'NEXT_LOCALE': 'en',
    'sso_client_name': 'CR Backend',
    'client_id': 'kmj7imhjt_q90lcbzzsj',
    'OptanonAlertBoxClosed': '2025-10-29T17:56:27.435Z',
    '__cf_bm': '7L7qhn00U.uFO9ooY4tQeXexU8Sm74SZiWIO7j_5mqA-1761762307-1.0.1.1-EjhJxrj5AaOOmslprQV.u9l1QBb7ThuyWuoDNQyUBYoxj_N_rTMKb7l6S26U3XPM6lawwBXF8ZqpSmDQwzaRpbgGdK9IQerj4gUCJN7Z.WxboAKsNhGrt2rBxEK5i11M',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Oct+30+2025+00%3A00%3A38+GMT%2B0530+(India+Standard+Time)&version=202311.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=44fbc14e-6b92-41b0-8b2c-a9b9c7646b05&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0&geolocation=BR%3BSP&AwaitingReconsent=false',
    'cf_clearance': '_2qwocwaWvsEqRvba2t9hYQKOQrfQ8qJ7emrdEoyZlM-1761762638-1.2.1.1-dc72WsT__uXhptLrx9LjfUlM.ybwZAO66AWOOBk8YTukKgKaPwxnW5bSHYyoHs23F30q9q_gCcIj..rt8TukCbLT.p1q.o3f0fSTKi_HUTENevbTAp22QYixjWUt6XORbe077GjhRt55FHftXgkyeAc2TsH_UIv.ZqPn3Qgf_3qqBLFPEBfcV0i6nmznJYLCG4zg0VMZauX_32bTVOAByliiCgjXwGgOfkmaDxMf9oo',
    'SSRT_GuUe': 'UV0CaQADAA',
}

headers = {
    'accept': 'text/x-component',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'text/plain;charset=UTF-8',
    'next-action': '030eb0672aa9ea1bbf2657a9ef1030abedf8c2ab',
    'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22en%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22login%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22return_url%5C%22%3A%5C%22%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover%5C%22%7D%22%2C%7B%7D%2C%22%2Flogin%3Freturn_url%3D%252Fauthorize%253Fclient_id%253Dkmj7imhjt_q90lcbzzsj%2526redirect_uri%253Dhttps%25253A%25252F%25252Fwww.crunchyroll.com%25252Fcallback%2526response_type%253Dcookie%2526state%253D%25252Fdiscover%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D',
    'origin': 'https://sso.crunchyroll.com',
    'priority': 'u=1, i',
    'referer': 'https://sso.crunchyroll.com/login?return_url=%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_banner():
    """Print banner with timestamp"""
    banner = f"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        Crunchyroll Login - reCAPTCHA v3 Bypass Tool             ║
║                   Powered by Anti-Captcha                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

    Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    print(banner)

def log(message, level="INFO"):
    """Enhanced logging with timestamp and level"""
    timestamp = datetime.now().strftime('%H:%M:%S')
    symbols = {
        "INFO": "[*]",
        "SUCCESS": "[+]",
        "ERROR": "[-]",
        "WARNING": "[!]",
        "DEBUG": "[DEBUG]"
    }
    symbol = symbols.get(level, "[*]")
    
    if level == "DEBUG" and not DEBUG_MODE:
        return
    
    print(f"{symbol} [{timestamp}] {message}")

def load_cookies_from_file(filepath='cookies.json'):
    """Load cookies from JSON file if exists"""
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                loaded_cookies = json.load(f)
            log(f"Loaded cookies from {filepath}", "SUCCESS")
            return loaded_cookies
        except Exception as e:
            log(f"Failed to load cookies from file: {e}", "WARNING")
    return None

def save_cookies_to_file(cookies_dict, filepath='cookies.json'):
    """Save cookies to JSON file"""
    try:
        with open(filepath, 'w') as f:
            json.dump(cookies_dict, f, indent=2)
        log(f"Cookies saved to {filepath}", "SUCCESS")
    except Exception as e:
        log(f"Failed to save cookies: {e}", "ERROR")

def check_api_key():
    """Validate API key configuration"""
    if ANTI_CAPTCHA_API_KEY == "YOUR_API_KEY_HERE" or not ANTI_CAPTCHA_API_KEY:
        log("Anti-Captcha API key not configured!", "ERROR")
        print("\n    Configuration options:")
        print("    1. Set environment variable: export ANTI_CAPTCHA_API_KEY='your_key'")
        print("    2. Edit main.py and set: ANTI_CAPTCHA_API_KEY = 'your_key'")
        print("\n    Get your API key: https://anti-captcha.com/clients/settings/apisetup\n")
        return False
    
    log(f"API Key configured: {ANTI_CAPTCHA_API_KEY[:8]}...{ANTI_CAPTCHA_API_KEY[-4:]}", "SUCCESS")
    return True

def check_balance():
    """Check Anti-Captcha account balance"""
    try:
        log("Checking Anti-Captcha account balance...", "INFO")
        response = requests.post(
            'https://api.anti-captcha.com/getBalance',
            json={'clientKey': ANTI_CAPTCHA_API_KEY},
            timeout=10
        )
        data = response.json()
        
        if data.get('errorId') == 0:
            balance = data.get('balance', 0)
            log(f"Account Balance: ${balance:.4f}", "SUCCESS")
            
            if balance < 0.001:
                log("Insufficient balance! Add funds to continue.", "ERROR")
                log("Top up at: https://anti-captcha.com/clients/finance/refill", "INFO")
                return False
            elif balance < 0.10:
                log("Low balance warning! Consider adding funds.", "WARNING")
            
            # Calculate approximate solves remaining
            cost_per_solve = 0.002  # Approximate cost
            solves_remaining = int(balance / cost_per_solve)
            log(f"Estimated solves remaining: ~{solves_remaining}", "INFO")
            return True
        else:
            error = data.get('errorDescription', 'Unknown error')
            log(f"Balance check failed: {error}", "ERROR")
            return False
            
    except requests.exceptions.Timeout:
        log("Balance check timed out", "ERROR")
        return False
    except Exception as e:
        log(f"Exception checking balance: {e}", "ERROR")
        return False

def solve_recaptcha_v3(attempt=1):
    """Solve reCAPTCHA v3 using Anti-Captcha service"""
    log("=" * 60, "INFO")
    log(f"Solving reCAPTCHA v3 - Attempt {attempt}/{MAX_RETRIES}", "INFO")
    log("=" * 60, "INFO")
    
    solver = recaptchaV3Proxyless()
    solver.set_verbose(1 if DEBUG_MODE else 0)
    solver.set_key(ANTI_CAPTCHA_API_KEY)
    solver.set_website_url(WEBSITE_URL)
    solver.set_website_key(RECAPTCHA_SITE_KEY)
    solver.set_page_action(PAGE_ACTION)
    solver.set_min_score(MIN_SCORE)
    
    log(f"Website: {WEBSITE_URL[:60]}...", "INFO")
    log(f"Site Key: {RECAPTCHA_SITE_KEY}", "INFO")
    log(f"Page Action: {PAGE_ACTION}", "INFO")
    log(f"Min Score: {MIN_SCORE}", "INFO")
    log("Submitting task to Anti-Captcha workers...", "INFO")
    
    start_time = time.time()
    
    try:
        g_response = solver.solve_and_return_solution()
        elapsed_time = time.time() - start_time
        
        if g_response != 0:
            log(f"reCAPTCHA solved successfully! ✓", "SUCCESS")
            log(f"Time taken: {elapsed_time:.2f} seconds", "INFO")
            log(f"Token length: {len(g_response)} characters", "INFO")
            log(f"Token preview: {g_response[:80]}...", "DEBUG")
            
            # Save token if enabled
            if SAVE_TOKENS:
                save_token_to_file(g_response)
            
            return g_response
        else:
            error_code = solver.error_code
            log(f"Failed to solve reCAPTCHA ✗", "ERROR")
            log(f"Error code: {error_code}", "ERROR")
            
            # Detailed error messages
            error_messages = {
                'ERROR_ZERO_BALANCE': 'Insufficient balance - add funds to your account',
                'ERROR_KEY_DOES_NOT_EXIST': 'Invalid API key - check your configuration',
                'ERROR_NO_SLOT_AVAILABLE': 'All workers busy - try again in a moment',
                'ERROR_RECAPTCHA_INVALID_SITEKEY': 'Invalid site key - verify the key is correct',
                'ERROR_RECAPTCHA_TIMEOUT': 'Solving timeout - workers took too long',
                'ERROR_RECAPTCHA_INVALID_DOMAIN': 'Domain mismatch - check website URL',
                'ERROR_TOO_MANY_BAD_IMAGES': 'Quality issue - retry may work',
            }
            
            if error_code in error_messages:
                log(f"Details: {error_messages[error_code]}", "ERROR")
            
            return None
            
    except Exception as e:
        elapsed_time = time.time() - start_time
        log(f"Exception after {elapsed_time:.2f} seconds", "ERROR")
        log(f"Exception details: {str(e)}", "ERROR")
        return None

def save_token_to_file(token):
    """Save reCAPTCHA token to file with timestamp"""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"token_{timestamp}.txt"
        with open(filename, 'w') as f:
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write(f"Site Key: {RECAPTCHA_SITE_KEY}\n")
            f.write(f"Page Action: {PAGE_ACTION}\n")
            f.write(f"Min Score: {MIN_SCORE}\n")
            f.write(f"\nToken:\n{token}\n")
        log(f"Token saved to {filename}", "DEBUG")
    except Exception as e:
        log(f"Failed to save token: {e}", "WARNING")

def send_login_request(recaptcha_token):
    """Send login request with solved reCAPTCHA token"""
    log("=" * 60, "INFO")
    log("Sending Login Request to Crunchyroll", "INFO")
    log("=" * 60, "INFO")
    
    # Prepare payload
    payload = [
        {
            "email": EMAIL,
            "password": PASSWORD,
            "recaptchaToken": recaptcha_token
        },
        {
            "eventSource": "$undefined",
            "attributionPartner": "$undefined",
            "utmSource": "$undefined",
            "utmCampaign": "$undefined",
            "pageOrScreen": "Login - Enter Password"
        }
    ]
    
    log(f"Email: {EMAIL}", "INFO")
    log(f"Password: {'*' * len(PASSWORD)}", "INFO")
    log(f"Endpoint: {WEBSITE_URL[:60]}...", "INFO")
    log("Sending POST request...", "INFO")
    
    try:
        # Create session for better connection handling
        session = requests.Session()
        session.cookies.update(cookies)
        session.headers.update(headers)
        
        response = session.post(
            WEBSITE_URL,
            data=json.dumps(payload),
            timeout=REQUEST_TIMEOUT,
            allow_redirects=False
        )
        
        log("Response received!", "SUCCESS")
        log(f"Status Code: {response.status_code} ({response.reason})", "INFO")
        
        # Log important headers
        important_headers = ['content-type', 'location', 'set-cookie', 'content-length', 'x-request-id']
        for header in important_headers:
            if header in response.headers:
                value = response.headers[header]
                if len(str(value)) > 100:
                    value = str(value)[:100] + "..."
                log(f"Header {header}: {value}", "DEBUG")
        
        # Log response preview
        response_preview = response.text[:500] if len(response.text) > 0 else "(empty)"
        log(f"Response preview ({len(response.text)} chars): {response_preview}...", "DEBUG")
        
        # Analyze response
        analyze_response(response)
        
        # Save response if enabled
        if SAVE_RESPONSES:
            save_response_to_file(response)
        
        return response
        
    except requests.exceptions.Timeout:
        log(f"Request timed out after {REQUEST_TIMEOUT} seconds", "ERROR")
        return None
    except requests.exceptions.ConnectionError as e:
        log(f"Connection error: {e}", "ERROR")
        return None
    except Exception as e:
        log(f"Unexpected error: {str(e)}", "ERROR")
        return None

def analyze_response(response):
    """Analyze and interpret the response"""
    log("=" * 60, "INFO")
    log("Response Analysis", "INFO")
    log("=" * 60, "INFO")
    
    status_code = response.status_code
    response_text = response.text.lower()
    
    # Success indicators
    if status_code == 200:
        log("Status 200 OK - Request accepted ✓", "SUCCESS")
        
        if 'success' in response_text:
            log("Response contains 'success' keyword ✓", "SUCCESS")
        if 'token' in response_text or 'session' in response_text:
            log("Response contains authentication data ✓", "SUCCESS")
        if 'error' in response_text or 'invalid' in response_text or 'failed' in response_text:
            log("Response may contain error message ⚠", "WARNING")
            
    elif 300 <= status_code < 400:
        log(f"Redirect detected ({status_code}) ✓", "SUCCESS")
        if 'location' in response.headers:
            redirect_url = response.headers['location']
            log(f"Redirect URL: {redirect_url}", "INFO")
            if 'authorize' in redirect_url or 'callback' in redirect_url or 'discover' in redirect_url:
                log("Redirect suggests successful authentication! ✓✓", "SUCCESS")
            else:
                log("Redirect destination unclear", "WARNING")
                
    elif status_code == 400:
        log("400 Bad Request - Invalid data sent ✗", "ERROR")
        log("Possible causes: Invalid reCAPTCHA token, malformed request", "WARNING")
        
    elif status_code == 401:
        log("401 Unauthorized - Authentication failed ✗", "ERROR")
        log("Possible causes: Wrong credentials, expired session", "WARNING")
        
    elif status_code == 403:
        log("403 Forbidden - Access denied ✗", "ERROR")
        log("Possible causes:", "WARNING")
        log("  • reCAPTCHA token rejected as invalid/suspicious", "WARNING")
        log("  • Cloudflare protection triggered", "WARNING")
        log("  • IP address blocked/rate limited", "WARNING")
        log("  • Invalid or expired cookies/cf_clearance", "WARNING")
        
    elif status_code == 429:
        log("429 Too Many Requests - Rate limited ✗", "ERROR")
        log("Wait before retrying", "WARNING")
        
    elif status_code >= 500:
        log(f"{status_code} Server Error - Crunchyroll server issue ✗", "ERROR")
        log("Try again later", "WARNING")
    
    # Check for specific error messages
    if 'recaptcha' in response_text and 'invalid' in response_text:
        log("reCAPTCHA validation failed - token rejected", "ERROR")
    if 'cloudflare' in response_text or 'challenge' in response_text:
        log("Cloudflare challenge detected", "WARNING")
    if 'cookie' in response_text and 'invalid' in response_text:
        log("Cookie validation failed - update cookies", "WARNING")

def save_response_to_file(response):
    """Save full response to file for debugging"""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"response_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"Crunchyroll Login Response\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Status Code: {response.status_code}\n")
            f.write(f"Status: {response.reason}\n\n")
            
            f.write("Request URL:\n")
            f.write(f"{response.url}\n\n")
            
            f.write("Response Headers:\n")
            for key, value in response.headers.items():
                f.write(f"  {key}: {value}\n")
            
            f.write("\nResponse Cookies:\n")
            for key, value in response.cookies.items():
                f.write(f"  {key}: {value}\n")
            
            f.write(f"\nResponse Body ({len(response.text)} characters):\n")
            f.write("-" * 60 + "\n")
            f.write(response.text)
            f.write("\n" + "-" * 60 + "\n")
            
        log(f"Full response saved to {filename}", "INFO")
        
    except Exception as e:
        log(f"Failed to save response: {e}", "WARNING")

def print_summary(success, elapsed_time):
    """Print execution summary"""
    print("\n" + "=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)
    print(f"  Status: {'SUCCESS ✓' if success else 'FAILED ✗'}")
    print(f"  Total Time: {elapsed_time:.2f} seconds")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main execution function"""
    start_time = time.time()
    
    print_banner()
    
    # Configuration check
    log("Checking configuration...", "INFO")
    if not check_api_key():
        return 1
    
    # Check balance
    if not check_balance():
        return 1
    
    # Load custom cookies if available
    custom_cookies = load_cookies_from_file()
    if custom_cookies:
        cookies.update(custom_cookies)
    
    log("Starting reCAPTCHA solving process...", "INFO")
    
    # Solve reCAPTCHA with retries
    recaptcha_token = None
    for attempt in range(1, MAX_RETRIES + 1):
        recaptcha_token = solve_recaptcha_v3(attempt)
        
        if recaptcha_token:
            break
        
        if attempt < MAX_RETRIES:
            log(f"Retrying in {RETRY_DELAY} seconds...", "WARNING")
            time.sleep(RETRY_DELAY)
    
    if not recaptcha_token:
        log("Failed to solve reCAPTCHA after all attempts", "ERROR")
        elapsed_time = time.time() - start_time
        print_summary(False, elapsed_time)
        return 1
    
    # Send login request
    log("Proceeding to login request...", "INFO")
    response = send_login_request(recaptcha_token)
    
    if not response:
        log("Failed to send login request", "ERROR")
        elapsed_time = time.time() - start_time
        print_summary(False, elapsed_time)
        return 1
    
    # Determine success
    success = response.status_code == 200 or (300 <= response.status_code < 400)
    
    elapsed_time = time.time() - start_time
    print_summary(success, elapsed_time)
    
    if success:
        log("Login process completed successfully!", "SUCCESS")
        log("Check saved response file for details", "INFO")
        return 0
    else:
        log("Login process completed with errors", "WARNING")
        log("Check saved response file for troubleshooting", "INFO")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting...")
        sys.exit(130)
    except Exception as e:
        print(f"\n[-] Fatal error: {e}")
        sys.exit(1)
