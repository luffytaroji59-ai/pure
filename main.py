import requests
import json
from anticaptchaofficial.recaptchav3proxyless import recaptchaV3Proxyless

# Anti-Captcha configuration
ANTI_CAPTCHA_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
WEBSITE_URL = "https://sso.crunchyroll.com/login?return_url=%2Fauthorize%3Fclient_id%3Dkmj7imhjt_q90lcbzzsj%26redirect_uri%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fcallback%26response_type%3Dcookie%26state%3D%252Fdiscover"
RECAPTCHA_SITE_KEY = "6LeQj_wUAAAAABLdMxMxFF-x3Jvyd1hkbsRV9UAk"
PAGE_ACTION = "submit"  # Common action for login forms
MIN_SCORE = 0.3  # Minimum score required (0.3, 0.7, or 0.9)

# Cookies from the curl command
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

# Headers from the curl command
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

def solve_recaptcha_v3():
    """
    Solve reCAPTCHA v3 using Anti-Captcha service
    Returns the token if successful, None otherwise
    """
    print("[*] Initializing Anti-Captcha solver...")
    solver = recaptchaV3Proxyless()
    solver.set_verbose(1)
    solver.set_key(ANTI_CAPTCHA_API_KEY)
    solver.set_website_url(WEBSITE_URL)
    solver.set_website_key(RECAPTCHA_SITE_KEY)
    solver.set_page_action(PAGE_ACTION)
    solver.set_min_score(MIN_SCORE)
    
    print(f"[*] Solving reCAPTCHA v3 for {WEBSITE_URL}")
    print(f"[*] Site Key: {RECAPTCHA_SITE_KEY}")
    print(f"[*] Page Action: {PAGE_ACTION}")
    print(f"[*] Min Score: {MIN_SCORE}")
    
    try:
        g_response = solver.solve_and_return_solution()
        if g_response != 0:
            print(f"[+] reCAPTCHA solved successfully!")
            print(f"[+] Token: {g_response[:50]}...")
            return g_response
        else:
            error_code = solver.error_code
            print(f"[-] Failed to solve reCAPTCHA. Error code: {error_code}")
            return None
    except Exception as e:
        print(f"[-] Exception occurred while solving reCAPTCHA: {e}")
        return None

def send_login_request(recaptcha_token):
    """
    Send the login request with the solved reCAPTCHA token
    """
    # Prepare the request data
    data = [
        {
            "email": "luffytaroji50@gmail.com",
            "password": "luffytaroji50@gmail.com",
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
    
    print("\n[*] Sending login request to Crunchyroll...")
    
    try:
        response = requests.post(
            WEBSITE_URL,
            cookies=cookies,
            headers=headers,
            data=json.dumps(data)
        )
        
        print(f"[+] Response Status Code: {response.status_code}")
        print(f"[+] Response Headers: {dict(response.headers)}")
        print(f"[+] Response Body: {response.text[:500]}...")
        
        return response
    except Exception as e:
        print(f"[-] Exception occurred while sending request: {e}")
        return None

def main():
    print("=" * 60)
    print("Crunchyroll Login - reCAPTCHA v3 Bypass")
    print("=" * 60)
    
    # Step 1: Solve reCAPTCHA v3
    recaptcha_token = solve_recaptcha_v3()
    
    if not recaptcha_token:
        print("\n[-] Failed to obtain reCAPTCHA token. Exiting.")
        return
    
    # Step 2: Send login request with the token
    response = send_login_request(recaptcha_token)
    
    if response:
        print("\n[+] Request completed successfully!")
        
        # Check for common success indicators
        if response.status_code == 200:
            print("[+] Status code indicates success (200 OK)")
        elif 300 <= response.status_code < 400:
            print(f"[+] Redirect detected (Status: {response.status_code})")
            if 'location' in response.headers:
                print(f"[+] Redirect Location: {response.headers['location']}")
        else:
            print(f"[!] Unexpected status code: {response.status_code}")
    else:
        print("\n[-] Request failed.")

if __name__ == "__main__":
    main()
