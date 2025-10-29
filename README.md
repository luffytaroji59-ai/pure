# 🎯 Crunchyroll Login Automation - reCAPTCHA v3 Bypass

Automate Crunchyroll login by bypassing reCAPTCHA v3 challenges using the Anti-Captcha service. No manual token copying required!

## ✨ Features

- ✅ **Automatic reCAPTCHA v3 Solving** - Uses Anti-Captcha API workers
- ✅ **Smart Retry Logic** - Automatically retries failed attempts
- ✅ **Balance Checking** - Verifies Anti-Captcha account balance before starting
- ✅ **Environment Variables** - Support for `.env` configuration
- ✅ **Cookie Management** - Load cookies from external JSON file
- ✅ **Response Logging** - Saves all responses for debugging
- ✅ **Token Saving** - Optionally save solved tokens
- ✅ **Detailed Analysis** - Interprets response codes and suggests fixes
- ✅ **Beautiful CLI** - Colored output with timestamps and progress tracking

## 📋 Prerequisites

### 1. Anti-Captcha Account

You need an Anti-Captcha account with API access:

1. **Sign up**: https://anti-captcha.com/clients/entrance/register
2. **Get API Key**: https://anti-captcha.com/clients/settings/apisetup
3. **Add Funds**: https://anti-captcha.com/clients/finance/refill
   - reCAPTCHA v3: ~$2.00 per 1000 solves
   - Minimum deposit: $5.00

### 2. Python Environment

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Quick Start

### Step 1: Installation

```bash
# Clone or download this repository
cd /workspace

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configuration

Choose **ONE** of these configuration methods:

#### Option A: Environment Variables (Recommended)

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your credentials
nano .env
```

```bash
# .env file content
ANTI_CAPTCHA_API_KEY=your_actual_api_key_here
CRUNCHYROLL_EMAIL=your_email@example.com
CRUNCHYROLL_PASSWORD=your_password
```

Then load the environment variables:

```bash
# Linux/Mac
export $(cat .env | xargs)

# Or use a .env loader like python-dotenv
pip install python-dotenv
```

#### Option B: Direct Edit

Open `main.py` and edit these lines:

```python
ANTI_CAPTCHA_API_KEY = "your_actual_api_key_here"
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
```

### Step 3: Update Cookies (Important!)

The cookies in the script may expire. To get fresh cookies:

1. **Open Browser DevTools** (F12)
2. **Go to** https://sso.crunchyroll.com/login
3. **Copy cookies** from the Network tab
4. **Update cookies** in one of these ways:

**Method A: Update `main.py` directly**
```python
cookies = {
    'SSID_GuUe': 'your_value',
    'cf_clearance': 'your_value',
    # ... etc
}
```

**Method B: Create `cookies.json`** (recommended)
```bash
cp cookies.json.example cookies.json
# Edit cookies.json with your values
```

The script will automatically load `cookies.json` if it exists.

### Step 4: Run

```bash
python main.py
```

## 📖 Usage Examples

### Basic Usage

```bash
# Using environment variables
export ANTI_CAPTCHA_API_KEY="your_key"
python main.py
```

### With Custom Configuration

```python
# Edit main.py to customize:

# reCAPTCHA settings
MIN_SCORE = 0.3  # Options: 0.3, 0.7, 0.9 (lower = easier)
PAGE_ACTION = "submit"  # Change if needed

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Debug settings
DEBUG_MODE = True  # Show detailed logs
SAVE_RESPONSES = True  # Save responses to files
SAVE_TOKENS = True  # Save solved tokens
```

## 📊 Output Files

The script creates several output files:

- `response_YYYYMMDD_HHMMSS.txt` - Full HTTP response with headers and body
- `token_YYYYMMDD_HHMMSS.txt` - Solved reCAPTCHA token (if SAVE_TOKENS=True)
- `cookies.json` - Custom cookies (if you create it)

## 🔧 How It Works

### 1. Configuration Check
```
✓ Validates API key
✓ Checks account balance
✓ Loads custom cookies if available
```

### 2. reCAPTCHA Solving
```
→ Sends challenge to Anti-Captcha
→ Anti-Captcha workers solve it (10-30 seconds)
→ Returns solved token
→ Retries up to 3 times if failed
```

### 3. Login Request
```
→ Builds request with solved token
→ Sends POST to Crunchyroll SSO
→ Analyzes response
→ Saves response for review
```

### 4. Response Analysis
```
✓ 200/3xx = Success
✗ 403 = Token rejected / Cloudflare blocked
✗ 401 = Wrong credentials
✗ 400 = Invalid request format
```

## 🐛 Troubleshooting

### Error: "Invalid API key"

**Solution:**
```bash
# Verify your API key
curl -X POST https://api.anti-captcha.com/getBalance \
  -H "Content-Type: application/json" \
  -d '{"clientKey":"YOUR_API_KEY"}'

# Should return: {"errorId":0,"balance":X.XX}
```

### Error: "Insufficient balance"

**Solution:**
- Add funds: https://anti-captcha.com/clients/finance/refill
- Minimum: $5.00
- Cost: ~$2/1000 solves

### Error: "403 Forbidden"

**Causes & Solutions:**

1. **Expired Cookies**
   - Get fresh cookies from browser DevTools
   - Update `cookies.json` or `main.py`

2. **Cloudflare Challenge**
   - The `cf_clearance` cookie expired
   - Get new cf_clearance from browser
   - Consider using a proxy

3. **reCAPTCHA Token Rejected**
   - Lower MIN_SCORE: `MIN_SCORE = 0.3`
   - Change PAGE_ACTION if needed
   - Verify RECAPTCHA_SITE_KEY is correct

4. **IP Blocked / Rate Limited**
   - Wait 15-30 minutes
   - Use a different IP/proxy
   - Check if IP is blacklisted

### Error: "400 Bad Request"

**Solution:**
- Check request payload format
- Verify email/password are correct
- Ensure `next-action` header is valid
- Update `next-router-state-tree` header

### reCAPTCHA Solving Takes Too Long

**Normal:** 10-30 seconds  
**Slow:** 30-60 seconds (workers busy)

**Solutions:**
- Wait for workers to be available
- Check Anti-Captcha status: https://anti-captcha.com/
- Try again later

### Cookies Keep Expiring

**Cloudflare cookies expire quickly:**
- `__cf_bm`: ~30 minutes
- `cf_clearance`: ~2-4 hours

**Solutions:**
1. Get fresh cookies before each run
2. Use a session that maintains cookies
3. Consider browser automation (Selenium/Playwright)

## 🔐 Security Notes

- ⚠️ **Never commit your API key** to version control
- ⚠️ **Never share your `.env` file**
- ⚠️ **Keep cookies.json private**
- ⚠️ Use environment variables for sensitive data
- ⚠️ Rotate credentials regularly

Add to `.gitignore`:
```
.env
cookies.json
token_*.txt
response_*.txt
__pycache__/
*.pyc
```

## 📝 Configuration Reference

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `ANTI_CAPTCHA_API_KEY` | Yes | - | Your Anti-Captcha API key |
| `CRUNCHYROLL_EMAIL` | No | (in script) | Login email |
| `CRUNCHYROLL_PASSWORD` | No | (in script) | Login password |

### Script Settings

| Setting | Default | Options | Description |
|---------|---------|---------|-------------|
| `MIN_SCORE` | 0.3 | 0.3, 0.7, 0.9 | reCAPTCHA score threshold |
| `PAGE_ACTION` | "submit" | string | reCAPTCHA action parameter |
| `MAX_RETRIES` | 3 | 1-10 | Retry attempts for solving |
| `RETRY_DELAY` | 5 | seconds | Delay between retries |
| `DEBUG_MODE` | True | bool | Show debug messages |
| `SAVE_RESPONSES` | True | bool | Save responses to files |
| `SAVE_TOKENS` | True | bool | Save solved tokens |

## 💰 Costs

### Anti-Captcha Pricing

- **reCAPTCHA v3**: $2.00 per 1000 solves = $0.002 per solve
- **reCAPTCHA v2**: $1.00 per 1000 solves = $0.001 per solve
- **Minimum Deposit**: $5.00

### Example Calculations

```
100 logins  = $0.20
500 logins  = $1.00
1000 logins = $2.00
```

## 🎯 Advanced Usage

### Custom Page Action

Some sites use different page actions:

```python
PAGE_ACTION = "login"  # or "submit", "homepage", etc.
```

To find the correct action:
1. Inspect the site's JavaScript
2. Look for `grecaptcha.execute('site_key', {action: 'ACTION_HERE'})`

### Using Proxies

For better success with Cloudflare:

```python
proxies = {
    'http': 'http://user:pass@proxy:port',
    'https': 'http://user:pass@proxy:port'
}

response = requests.post(URL, proxies=proxies, ...)
```

### Batch Processing

Process multiple accounts:

```python
accounts = [
    ('email1@example.com', 'password1'),
    ('email2@example.com', 'password2'),
]

for email, password in accounts:
    EMAIL = email
    PASSWORD = password
    main()
    time.sleep(10)  # Delay between accounts
```

## 📚 API Documentation

- **Anti-Captcha**: https://anti-captcha.com/apidoc
- **reCAPTCHA v3**: https://developers.google.com/recaptcha/docs/v3

## 🤝 Support

### Getting Help

1. **Check this README** - Most issues are covered here
2. **Anti-Captcha Support**: https://anti-captcha.com/clients/support
3. **Check saved response files** for error details

### Common Questions

**Q: Can I use 2Captcha instead?**  
A: Yes, but you'll need to use a different Python library. The API is similar.

**Q: Why do cookies expire so fast?**  
A: Cloudflare cookies (`cf_clearance`, `__cf_bm`) expire quickly for security. This is normal.

**Q: Can this bypass Cloudflare completely?**  
A: No, you still need valid Cloudflare cookies. Consider using cloudscraper or similar tools.

**Q: Is this legal?**  
A: This is for educational purposes. Check Crunchyroll's Terms of Service before using.

**Q: Can I get banned?**  
A: Excessive automated requests may result in IP/account restrictions. Use responsibly.

## ⚖️ Legal Disclaimer

This tool is for **educational purposes only**. Users are responsible for complying with:
- Crunchyroll's Terms of Service
- Anti-Captcha's Terms of Service
- Applicable local and international laws

Automated access may violate service terms. Use at your own risk.

## 📄 License

This project is for educational purposes. Use responsibly.

## 🌟 Credits

- **Anti-Captcha**: For providing the reCAPTCHA solving service
- **Requests**: For HTTP library
- **anticaptchaofficial**: For the Python SDK

---

**Made with ❤️ for automation enthusiasts**

*Last updated: 2025-10-29*
