# Crunchyroll Login - reCAPTCHA v3 Bypass

This script automates the Crunchyroll login process by bypassing reCAPTCHA v3 using the Anti-Captcha service.

## Features

- Automatically solves reCAPTCHA v3 challenges using Anti-Captcha API
- Sends authenticated login request to Crunchyroll SSO
- Maintains all necessary cookies and headers from browser session

## Prerequisites

1. **Anti-Captcha Account**: You need an API key from [Anti-Captcha](https://anti-captcha.com/)
   - Sign up at https://anti-captcha.com/clients/entrance/register
   - Get your API key from the dashboard
   - Add funds to your account (reCAPTCHA v3 costs around $2 per 1000 solves)

2. **Python 3.7+**

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Open `main.py` and replace the following:

1. **API Key**: Replace `YOUR_API_KEY_HERE` with your actual Anti-Captcha API key
   ```python
   ANTI_CAPTCHA_API_KEY = "your_actual_api_key_here"
   ```

2. **Credentials** (if different): Update the email and password in the `send_login_request()` function
   ```python
   "email": "your_email@example.com",
   "password": "your_password"
   ```

3. **Cookies**: The cookies in the script are from your browser session. They may expire, so you might need to update them with fresh ones from your browser.

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Initialize the Anti-Captcha solver
2. Solve the reCAPTCHA v3 challenge (this may take 10-30 seconds)
3. Send the login request with the solved token
4. Display the response

## How It Works

1. **reCAPTCHA v3 Solving**: The script uses Anti-Captcha's API to solve the reCAPTCHA v3 challenge. It mimics the browser behavior by:
   - Sending the website URL
   - Providing the reCAPTCHA site key (6LeQj_wUAAAAABLdMxMxFF-x3Jvyd1hkbsRV9UAk)
   - Specifying the page action ("submit")
   - Setting minimum score requirement (0.3)

2. **Login Request**: Once the token is obtained, it's inserted into the request payload and sent to Crunchyroll's SSO endpoint with all the necessary headers and cookies.

## Configuration Options

You can adjust these parameters in `main.py`:

- **MIN_SCORE**: Set to 0.3, 0.7, or 0.9 (lower is easier but may be rejected by the site)
- **PAGE_ACTION**: The action parameter for reCAPTCHA (default: "submit")

## Troubleshooting

### "Invalid API key" error
- Make sure you've replaced `YOUR_API_KEY_HERE` with your actual Anti-Captcha API key
- Verify your API key at https://anti-captcha.com/clients/settings/apisetup

### "Insufficient balance" error
- Add funds to your Anti-Captcha account

### Cookies expired
- The cookies from your browser session may have expired
- Open Crunchyroll in your browser, log out, and capture fresh cookies from the network tab
- Update the `cookies` dictionary in `main.py`

### Request fails after token is obtained
- Cookies might be invalid or expired
- Some headers might need to be updated (especially `next-action` and `__cf_bm`)
- Check if Crunchyroll has changed their API endpoint or request structure

## Important Notes

- **Cost**: Each reCAPTCHA v3 solve costs money on Anti-Captcha (approximately $2 per 1000 solves)
- **Session Cookies**: The `__cf_bm` and `cf_clearance` cookies are Cloudflare tokens that expire quickly
- **Rate Limiting**: Don't spam requests too frequently or your IP/account might get rate-limited
- **Terms of Service**: Use this responsibly and in accordance with Crunchyroll's Terms of Service

## API Key Sources

Get your API key from one of these Anti-Captcha solving services:
- [Anti-Captcha](https://anti-captcha.com/) - Recommended
- [2Captcha](https://2captcha.com/) - Alternative (requires different library)

## License

This is for educational purposes only. Use responsibly.
