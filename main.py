import requests
import json
import time
import os
from anticaptchaofficial.recaptchav3proxyless import recaptchaV3Proxyless

# ============================================================================
# CONFIGURATION - Update these values
# ============================================================================

ANTI_CAPTCHA_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key

# Login credentials
EMAIL = "luffytaroji50@gmail.com"
PASSWORD = "luffytaroji50@gmail.com"

# reCAPTCHA settings
WEBSITE_URL = "https://sso.crunchyroll.com/login?return_url=%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover"
RECAPTCHA_SITE_KEY = "6LeQj_wUAAAAABLdMxMxFF-x3Jvyd1hkbsRV9UAk"
PAGE_ACTION = "submit"
MIN_SCORE = 0.3

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

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
# FUNCTIONS
# ============================================================================

def print_banner():
    """Print a nice banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║         Crunchyroll Login - reCAPTCHA v3 Bypass             ║
    ║                   Anti-Captcha Service                       ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_api_key():
    """Check if API key is configured"""
    if ANTI_CAPTCHA_API_KEY == "YOUR_API_KEY_HERE" or not ANTI_CAPTCHA_API_KEY:
        print("\n[!] ERROR: Anti-Captcha API key not configured!")
        print("[!] Please edit main.py and set your API key:")
        print("[!]   ANTI_CAPTCHA_API_KEY = 'your_actual_key_here'")
        print("\n[i] Get your API key from: https://anti-captcha.com/clients/settings/apisetup")
        return False
    return True

def check_balance():
    """Check Anti-Captcha account balance"""
    try:
        print("\n[*] Checking Anti-Captcha account balance...")
        response = requests.post(
            'https://api.anti-captcha.com/getBalance',
            json={'clientKey': ANTI_CAPTCHA_API_KEY},
            timeout=10
        )
        data = response.json()
        
        if data.get('errorId') == 0:
            balance = data.get('balance', 0)
            print(f"[+] Account Balance: ${balance:.2f}")
            if balance < 0.10:
                print("[!] WARNING: Low balance! Add funds to continue.")
                return False
            return True
        else:
            error = data.get('errorDescription', 'Unknown error')
            print(f"[-] Error checking balance: {error}")
            return False
    except Exception as e:
        print(f"[-] Exception checking balance: {e}")
        return False

def solve_recaptcha_v3(attempt=1):
    """
    Solve reCAPTCHA v3 using Anti-Captcha service
    Returns the token if successful, None otherwise
    """
    print(f"\n{'='*60}")
    print(f"[*] Attempt {attempt}/{MAX_RETRIES} - Solving reCAPTCHA v3")
    print(f"{'='*60}")
    
    solver = recaptchaV3Proxyless()
    solver.set_verbose(1)
    solver.set_key(ANTI_CAPTCHA_API_KEY)
    solver.set_website_url(WEBSITE_URL)
    solver.set_website_key(RECAPTCHA_SITE_KEY)
    solver.set_page_action(PAGE_ACTION)
    solver.set_min_score(MIN_SCORE)
    
    print(f"[*] Website: {WEBSITE_URL[:50]}...")
    print(f"[*] Site Key: {RECAPTCHA_SITE_KEY}")
    print(f"[*] Page Action: {PAGE_ACTION}")
    print(f"[*] Min Score: {MIN_SCORE}")
    print(f"[*] Submitting task to Anti-Captcha...")
    
    start_time = time.time()
    
    try:
        g_response = solver.solve_and_return_solution()
        
        elapsed_time = time.time() - start_time
        
        if g_response != 0:
            print(f"\n[+] ✓ reCAPTCHA solved successfully!")
            print(f"[+] Time taken: {elapsed_time:.2f} seconds")
            print(f"[+] Token (first 80 chars): {g_response[:80]}...")
            print(f"[+] Token length: {len(g_response)} characters")
            return g_response
        else:
            error_code = solver.error_code
            print(f"\n[-] ✗ Failed to solve reCAPTCHA")
            print(f"[-] Error code: {error_code}")
            
            # Common error codes
            error_messages = {
                'ERROR_ZERO_BALANCE': 'Insufficient balance in your Anti-Captcha account',
                'ERROR_KEY_DOES_NOT_EXIST': 'Invalid API key',
                'ERROR_NO_SLOT_AVAILABLE': 'No workers available, try again later',
                'ERROR_RECAPTCHA_INVALID_SITEKEY': 'Invalid site key',
                'ERROR_RECAPTCHA_TIMEOUT': 'Timeout while solving',
            }
            
            if error_code in error_messages:
                print(f"[-] Description: {error_messages[error_code]}")
            
            return None
            
    except Exception as e:
        elapsed_time = time.time() - start_time
        print(f"\n[-] ✗ Exception after {elapsed_time:.2f} seconds")
        print(f"[-] Exception: {str(e)}")
        return None

def send_login_request(recaptcha_token):
    """
    Send the login request with the solved reCAPTCHA token
    """
    print(f"\n{'='*60}")
    print("[*] Sending Login Request")
    print(f"{'='*60}")
    
    # Prepare the request data
    data = [
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
    
    print(f"[*] Email: {EMAIL}")
    print(f"[*] Endpoint: {WEBSITE_URL[:50]}...")
    print(f"[*] Sending POST request...")
    
    try:
        response = requests.post(
            WEBSITE_URL,
            cookies=cookies,
            headers=headers,
            data=json.dumps(data),
            timeout=30,
            allow_redirects=False
        )
        
        print(f"\n[+] Response received!")
        print(f"[+] Status Code: {response.status_code}")
        print(f"[+] Status: {response.reason}")
        
        # Print important headers
        important_headers = ['content-type', 'location', 'set-cookie', 'content-length']
        print(f"\n[*] Response Headers:")
        for header in important_headers:
            if header in response.headers:
                value = response.headers[header]
                if len(value) > 100:
                    value = value[:100] + "..."
                print(f"    {header}: {value}")
        
        # Print response body (truncated)
        print(f"\n[*] Response Body ({len(response.text)} chars):")
        if len(response.text) > 0:
            preview = response.text[:1000]
            print(f"    {preview}")
            if len(response.text) > 1000:
                print(f"    ... (truncated)")
        else:
            print("    (empty)")
        
        # Analyze response
        print(f"\n{'='*60}")
        print("[*] Response Analysis:")
        print(f"{'='*60}")
        
        if response.status_code == 200:
            print("[+] ✓ Status 200 OK - Request successful")
            
            # Check for common success indicators
            response_lower = response.text.lower()
            if 'success' in response_lower or 'redirect' in response_lower:
                print("[+] ✓ Response suggests successful login")
            elif 'error' in response_lower or 'invalid' in response_lower:
                print("[!] ⚠ Response may contain error message")
            
        elif 300 <= response.status_code < 400:
            print(f"[+] ✓ Redirect detected ({response.status_code})")
            if 'location' in response.headers:
                redirect_url = response.headers['location']
                print(f"[+] Redirect URL: {redirect_url}")
                if 'authorize' in redirect_url or 'callback' in redirect_url:
                    print("[+] ✓ Redirect suggests successful authentication!")
        
        elif response.status_code == 403:
            print("[-] ✗ 403 Forbidden - Request blocked")
            print("[!] Possible causes:")
            print("    - reCAPTCHA token rejected")
            print("    - Cloudflare protection triggered")
            print("    - Invalid cookies/session")
            
        elif response.status_code >= 400:
            print(f"[-] ✗ Error response ({response.status_code})")
            print("[!] Request failed - check credentials and cookies")
        
        # Save response to file
        save_response(response)
        
        return response
        
    except requests.exceptions.Timeout:
        print("\n[-] ✗ Request timed out after 30 seconds")
        return None
    except requests.exceptions.ConnectionError:
        print("\n[-] ✗ Connection error - check your internet connection")
        return None
    except Exception as e:
        print(f"\n[-] ✗ Exception occurred: {str(e)}")
        return None

def save_response(response):
    """Save response to file for debugging"""
    try:
        filename = f"response_{int(time.time())}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Status Code: {response.status_code}\n")
            f.write(f"Status: {response.reason}\n\n")
            f.write("Headers:\n")
            for key, value in response.headers.items():
                f.write(f"  {key}: {value}\n")
            f.write(f"\nBody:\n{response.text}\n")
        print(f"[*] Full response saved to: {filename}")
    except Exception as e:
        print(f"[-] Could not save response: {e}")

def main():
    """Main function"""
    print_banner()
    
    # Check API key
    if not check_api_key():
        return 1
    
    # Check balance
    if not check_balance():
        return 1
    
    # Try to solve captcha with retries
    recaptcha_token = None
    for attempt in range(1, MAX_RETRIES + 1):
        recaptcha_token = solve_recaptcha_v3(attempt)
        
        if recaptcha_token:
            break
        
        if attempt < MAX_RETRIES:
            print(f"\n[*] Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
    
    if not recaptcha_token:
        print(f"\n{'='*60}")
        print("[-] ✗ FAILED: Could not solve reCAPTCHA after all attempts")
        print(f"{'='*60}")
        return 1
    
    # Send login request
    response = send_login_request(recaptcha_token)
    
    if not response:
        print(f"\n{'='*60}")
        print("[-] ✗ FAILED: Could not send login request")
        print(f"{'='*60}")
        return 1
    
    # Final summary
    print(f"\n{'='*60}")
    print("[*] EXECUTION COMPLETE")
    print(f"{'='*60}")
    
    if response.status_code == 200 or (300 <= response.status_code < 400):
        print("[+] ✓ Script completed successfully!")
        print("[*] Check the response above for details")
        return 0
    else:
        print("[-] ⚠ Script completed with warnings")
        print("[*] Check the response above for details")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
