# 🔧 Troubleshooting Guide

## ❌ Error: Chrome version mismatch

```
This version of ChromeDriver only supports Chrome version 142
Current browser version is 141.0.7390.123
```

### Quick Fix (Choose your OS):

**Linux/Mac:**
```bash
bash auto_fix.sh
```

**Windows:**
```cmd
auto_fix.bat
```

**Manual Fix:**
```bash
# 1. Clear cache
rm -rf ~/.local/share/undetected_chromedriver/
rm -rf ~/.wdm/

# 2. Upgrade packages
pip install --upgrade undetected-chromedriver selenium

# 3. Try again
python main.py
```

---

## ❌ Error: Cannot reuse ChromeOptions object

**Fixed!** The updated `main.py` now creates fresh options for each attempt.

Just run:
```bash
python main.py
```

---

## ❌ Error: Chrome not found

### Windows:
1. Download: https://www.google.com/chrome/
2. Install normally
3. Restart terminal
4. Run: `python main.py`

### Mac:
```bash
brew install --cask google-chrome
```

### Linux:
```bash
# Ubuntu/Debian
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

# Or use Chromium
sudo apt install chromium-browser
```

---

## ❌ Still on login page after submit

### Cause 1: Wrong credentials
- Double-check email and password in `main.py`
- Make sure no extra spaces

### Cause 2: Account requires verification
- Check your email for verification link
- Complete any 2FA if enabled

### Cause 3: Need more time
Edit `main.py` line ~294:
```python
# Change from:
time.sleep(8)

# To:
time.sleep(15)  # Give more time for redirect
```

---

## ❌ Error: Session not created

### Full error cleanup:
```bash
# Uninstall everything
pip uninstall undetected-chromedriver selenium -y

# Clear all caches
rm -rf ~/.local/share/undetected_chromedriver/
rm -rf ~/.wdm/
rm -rf ./.wdm/

# Reinstall fresh
pip install undetected-chromedriver selenium

# Try again
python main.py
```

---

## ⚠️ Browser closes immediately

This usually means an exception occurred.

**Debug:**
1. Check the error message in terminal
2. Look at screenshots created (if any)
3. Set longer sleep time to inspect:

Edit `main.py` around line 520:
```python
# After login attempt
time.sleep(60)  # Keep open 1 minute
```

---

## 🐧 Linux Server (Headless)

### Error: No display

```bash
# Install virtual display
sudo apt-get install xvfb

# Run with virtual display
xvfb-run python main.py
```

### Or use headless mode:
Edit `main.py` line 25:
```python
HEADLESS = True
```

---

## 🔍 Debug Mode

Want more details? Edit `main.py`:

```python
# Add more logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Increase wait times
WAIT_TIMEOUT = 60  # Line 23

# Keep browser open longer
# In main() function, change sleep to:
time.sleep(120)  # 2 minutes
```

---

## 💾 Cookies not saving

### Check file permissions:
```bash
ls -la crunchyroll_cookies.json
# Should be readable/writable

# If not:
chmod 644 crunchyroll_cookies.json
```

### Check disk space:
```bash
df -h .
```

---

## 🌐 Behind a proxy?

Edit `main.py` in `setup_driver()` function, add:

```python
# Add to options (around line 137):
options.add_argument('--proxy-server=http://your-proxy:port')
```

---

## 🔐 SSL Certificate errors

Edit `main.py` in `setup_driver()` function, add:

```python
# Add to options:
options.add_argument('--ignore-certificate-errors')
```

---

## 📱 Still need help?

### Collect debug info:

1. **Your Chrome version:**
   ```bash
   # Linux/Mac
   google-chrome --version
   
   # Windows
   reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version
   ```

2. **Your Python version:**
   ```bash
   python --version
   ```

3. **Package versions:**
   ```bash
   pip list | grep -E "(selenium|undetected)"
   ```

4. **Check screenshots:**
   - Look at `*.png` files created
   - See where it fails

5. **Full error:**
   - Copy entire error message
   - Include traceback

---

## ✅ Quick Checklist

Before asking for help, verify:

- [ ] Chrome/Chromium is installed and updated
- [ ] Python 3.7+ is installed
- [ ] Requirements installed: `pip install -r requirements.txt`
- [ ] Credentials are correct in `main.py`
- [ ] Ran `auto_fix.sh` / `auto_fix.bat`
- [ ] Tried increasing sleep times
- [ ] Checked screenshot files
- [ ] Cleared cache: `rm -rf ~/.local/share/undetected_chromedriver/`

---

## 🚀 Nuclear Option (Complete Reset)

If nothing works, complete fresh start:

```bash
# 1. Uninstall packages
pip uninstall undetected-chromedriver selenium -y

# 2. Clear ALL caches
rm -rf ~/.local/share/undetected_chromedriver/
rm -rf ~/.wdm/
rm -rf ~/.cache/selenium/

# 3. Update Chrome browser
# Visit: https://www.google.com/chrome/

# 4. Reinstall from scratch
pip install --no-cache-dir undetected-chromedriver selenium

# 5. Fresh run
python main.py
```

---

**Most issues are solved by running `auto_fix.sh` / `auto_fix.bat`!**
