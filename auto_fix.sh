#!/bin/bash
# Automatic fix for ChromeDriver version issues

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║           Automatic ChromeDriver Fix                            ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

echo "[*] Step 1: Clearing ChromeDriver cache..."
rm -rf ~/.local/share/undetected_chromedriver/ 2>/dev/null && echo "[+] Cache cleared" || echo "[*] No cache found"
rm -rf ~/.wdm/ 2>/dev/null
rm -rf ./.wdm/ 2>/dev/null

echo ""
echo "[*] Step 2: Upgrading undetected-chromedriver..."
pip install --upgrade undetected-chromedriver

echo ""
echo "[*] Step 3: Upgrading selenium..."
pip install --upgrade selenium

echo ""
echo "[+] Done! Now try running: python main.py"
