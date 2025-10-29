# 🎯 Crunchyroll Login - reCAPTCHA v3 Bypass

Automatically solve reCAPTCHA v3 and login to Crunchyroll using Anti-Captcha service.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Edit `main.py` and set your Anti-Captcha API key:

```python
ANTI_CAPTCHA_API_KEY = "your_api_key_here"  # Get from https://anti-captcha.com
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
```

### 3. Run

```bash
python main.py
```

## ✨ Features

- ✅ **Automatic reCAPTCHA v3 solving** using Anti-Captcha workers
- ✅ **Smart retry logic** with configurable attempts
- ✅ **Balance checking** before starting
- ✅ **Response analysis** with detailed error messages
- ✅ **Auto-save responses** and tokens to files
- ✅ **Cookie file support** (optional `cookies.json`)
- ✅ **Beautiful CLI** with timestamps and colors

## ⚙️ Configuration

All settings in `main.py`:

```python
# API & Credentials
ANTI_CAPTCHA_API_KEY = "YOUR_API_KEY_HERE"
EMAIL = "your_email@example.com"
PASSWORD = "your_password"

# reCAPTCHA Settings
MIN_SCORE = 0.3  # Options: 0.3, 0.7, 0.9
PAGE_ACTION = "submit"

# Retry Settings
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Debug Settings
DEBUG_MODE = True
SAVE_RESPONSES = True
SAVE_TOKENS = True
```

## 🔧 Cookie Management

**Option 1: Edit cookies in `main.py`** (default)

**Option 2: Create `cookies.json`** (recommended)
```json
{
  "SSID_GuUe": "your_value",
  "cf_clearance": "your_value",
  "__cf_bm": "your_value"
}
```

The script will automatically load `cookies.json` if it exists.

## 📊 Output Files

- `response_YYYYMMDD_HHMMSS.txt` - Full HTTP response
- `token_YYYYMMDD_HHMMSS.txt` - Solved reCAPTCHA token

## 🐛 Troubleshooting

### 403 Forbidden
- Update cookies (especially `cf_clearance` and `__cf_bm`)
- Get fresh cookies from browser DevTools

### Invalid API Key
- Check your API key at https://anti-captcha.com/clients/settings/apisetup

### Insufficient Balance
- Add funds at https://anti-captcha.com/clients/finance/refill
- Cost: ~$2 per 1000 solves

## 💰 Costs

- **reCAPTCHA v3**: $2.00 per 1000 solves ($0.002 each)
- **Minimum deposit**: $5.00

## 📝 How It Works

1. **Check balance** → Verify Anti-Captcha account has funds
2. **Solve reCAPTCHA** → Send challenge to workers (10-30 sec)
3. **Send login request** → POST with solved token
4. **Analyze response** → Check status and save results

## ⚠️ Important Notes

- Cloudflare cookies expire quickly (30min - 4hrs)
- Get fresh cookies from browser before each run
- Use responsibly and respect rate limits

## 📚 Links

- **Get API Key**: https://anti-captcha.com/clients/settings/apisetup
- **Add Funds**: https://anti-captcha.com/clients/finance/refill
- **API Docs**: https://anti-captcha.com/apidoc

---

**Made for educational purposes only. Use responsibly.**
