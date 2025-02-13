import shutil

chrome_path = shutil.which("google-chrome-stable") or shutil.which("google-chrome") or shutil.which("chrome")
chromedriver_path = shutil.which("chromedriver")

print("Chrome Path:", chrome_path)
print("ChromeDriver Path:", chromedriver_path)