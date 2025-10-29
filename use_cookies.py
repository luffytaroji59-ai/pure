#!/usr/bin/env python3
"""
Use extracted Crunchyroll cookies with requests library
Run this after main.py has successfully logged in
"""

import requests
import json
import sys
from datetime import datetime

def load_cookies():
    """Load cookies from saved file"""
    try:
        with open('crunchyroll_cookies.json', 'r') as f:
            cookies_list = json.load(f)
        
        # Convert to dict format for requests
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        
        print(f"[+] Loaded {len(cookies_dict)} cookies from crunchyroll_cookies.json")
        return cookies_dict
    
    except FileNotFoundError:
        print("[-] Error: crunchyroll_cookies.json not found!")
        print("[!] Run main.py first to login and save cookies")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error loading cookies: {e}")
        sys.exit(1)

def test_authentication(cookies):
    """Test if cookies are valid by making an API request"""
    print("\n[*] Testing authentication...")
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'accept': 'application/json',
    }
    
    # Test endpoint - adjust based on what you need
    test_url = "https://www.crunchyroll.com"
    
    try:
        response = requests.get(test_url, cookies=cookies, headers=headers, timeout=10)
        print(f"[+] Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("[+] ✓ Cookies are valid! Authentication successful!")
            return True
        else:
            print("[!] Warning: Unexpected status code")
            print(f"    Response preview: {response.text[:200]}")
            return False
            
    except Exception as e:
        print(f"[-] Error testing authentication: {e}")
        return False

def make_sample_request(cookies):
    """Example of making an authenticated request"""
    print("\n[*] Example: Making authenticated request to Crunchyroll...")
    
    # Example: Send a request like the original curl command
    url = "https://sso.crunchyroll.com/login?return_url=%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover"
    
    headers = {
        'accept': 'text/x-component',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'text/plain;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    }
    
    try:
        response = requests.get(url, cookies=cookies, headers=headers, timeout=10)
        print(f"[+] Response Status: {response.status_code}")
        print(f"[+] Response Length: {len(response.text)} bytes")
        
        # Save response
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"api_response_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Status: {response.status_code}\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n\n")
            f.write("Response:\n")
            f.write(response.text)
        
        print(f"[+] Full response saved to: {filename}")
        
    except Exception as e:
        print(f"[-] Error making request: {e}")

def print_cookies_code(cookies):
    """Print Python code to use these cookies"""
    print("\n" + "=" * 60)
    print("HOW TO USE THESE COOKIES IN YOUR CODE")
    print("=" * 60)
    print("\n# Copy this code to use the cookies:\n")
    
    print("import requests")
    print("import json\n")
    print("# Load cookies")
    print("with open('crunchyroll_cookies.json', 'r') as f:")
    print("    cookies_list = json.load(f)")
    print("cookies = {c['name']: c['value'] for c in cookies_list}\n")
    print("# Make authenticated request")
    print("headers = {")
    print("    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'")
    print("}")
    print("response = requests.get('https://www.crunchyroll.com/api/endpoint', cookies=cookies, headers=headers)")
    print("print(response.json())\n")
    print("=" * 60)

def main():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║              Crunchyroll Cookie Usage Example                   ║
║                  Use Saved Session Cookies                       ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    # Load cookies
    cookies = load_cookies()
    
    # Print important cookies
    print("\n[*] Important cookies found:")
    important = ['SSID_GuUe', 'cf_clearance', '__cf_bm', 'session_id']
    for key in important:
        if key in cookies:
            value = cookies[key]
            preview = value[:50] + "..." if len(value) > 50 else value
            print(f"    {key}: {preview}")
    
    # Test authentication
    test_authentication(cookies)
    
    # Make sample request
    make_sample_request(cookies)
    
    # Print usage code
    print_cookies_code(cookies)
    
    print("\n[+] Done! You can now use these cookies in your own scripts.")
    print("[!] Note: Cookies may expire after a few hours. Re-run main.py if needed.\n")

if __name__ == "__main__":
    main()
