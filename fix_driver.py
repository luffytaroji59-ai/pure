#!/usr/bin/env python3
"""
Quick fix script for ChromeDriver version issues
Run this if you get version mismatch errors
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def print_header():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║           ChromeDriver Version Fix Utility                      ║
╚══════════════════════════════════════════════════════════════════╝
    """)

def run_command(cmd, description):
    """Run a shell command and print result"""
    print(f"[*] {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[+] Success!")
            if result.stdout:
                print(f"    {result.stdout.strip()}")
            return True
        else:
            print(f"[-] Failed: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

def clear_driver_cache():
    """Clear undetected-chromedriver cache"""
    print("\n[*] Clearing ChromeDriver cache...")
    
    # Possible cache locations
    cache_paths = []
    
    # Linux/Mac
    home = Path.home()
    cache_paths.append(home / ".local" / "share" / "undetected_chromedriver")
    cache_paths.append(home / ".wdm")
    
    # Windows
    if sys.platform == "win32":
        appdata = os.getenv('APPDATA')
        if appdata:
            cache_paths.append(Path(appdata) / "undetected_chromedriver")
    
    # Current directory
    cache_paths.append(Path.cwd() / ".wdm")
    
    removed_count = 0
    for cache_path in cache_paths:
        if cache_path.exists():
            try:
                shutil.rmtree(cache_path)
                print(f"[+] Removed: {cache_path}")
                removed_count += 1
            except Exception as e:
                print(f"[-] Failed to remove {cache_path}: {e}")
    
    if removed_count == 0:
        print("[*] No cache found (already clean)")
    else:
        print(f"[+] Cleared {removed_count} cache location(s)")
    
    return True

def upgrade_packages():
    """Upgrade required packages"""
    print("\n[*] Upgrading packages...")
    
    packages = [
        "undetected-chromedriver",
        "selenium",
    ]
    
    for package in packages:
        cmd = f"{sys.executable} -m pip install --upgrade {package}"
        run_command(cmd, f"Upgrading {package}")
    
    return True

def check_chrome_version():
    """Try to detect Chrome version"""
    print("\n[*] Checking Chrome installation...")
    
    commands = {
        "Linux": "google-chrome --version || chromium --version",
        "Darwin": "/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --version",
        "Windows": 'reg query "HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon" /v version',
    }
    
    platform = sys.platform
    if platform.startswith("linux"):
        cmd = commands["Linux"]
    elif platform == "darwin":
        cmd = commands["Darwin"]
    elif platform == "win32":
        cmd = commands["Windows"]
    else:
        print(f"[-] Unknown platform: {platform}")
        return
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"[+] Chrome found: {result.stdout.strip()}")
    else:
        print(f"[-] Chrome not found or not accessible")
        print(f"[!] Install Chrome from: https://www.google.com/chrome/")

def main():
    print_header()
    
    print("This script will:")
    print("  1. Clear ChromeDriver cache")
    print("  2. Upgrade undetected-chromedriver")
    print("  3. Upgrade selenium")
    print("  4. Check Chrome installation")
    print()
    
    response = input("Continue? [Y/n]: ").strip().lower()
    if response and response != 'y':
        print("Cancelled.")
        return
    
    # Step 1: Clear cache
    clear_driver_cache()
    
    # Step 2: Upgrade packages
    upgrade_packages()
    
    # Step 3: Check Chrome
    check_chrome_version()
    
    print("\n" + "=" * 60)
    print("DONE!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Make sure Chrome is updated: https://www.google.com/chrome/")
    print("  2. Run: python main.py")
    print()
    print("If still having issues, try:")
    print("  pip uninstall undetected-chromedriver")
    print("  pip install undetected-chromedriver")
    print()

if __name__ == "__main__":
    main()
