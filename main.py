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
    # 'cookie': 'fusionauth.timezone=Asia/Calcutta; fusionauth.sso=AtZzqXza-QC3NlMl30tz6RvA43eMFJ0b6H_ewRD_qzO4; fusionauth.remember-device=QkJCAdWxuNeYQX9j9U1HHgiCoacddVf6p3VgDRN-XjWljGAO',
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
    'loginId': 'bernalobezogabo@gmail.com',
    'password': 'Gabominator260188',
}

response = requests.post('https://auth.purevpn.com/oauth2/authorize', cookies=cookies, headers=headers, data=data)
