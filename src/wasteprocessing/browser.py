import os
import subprocess
import sys
from glob import glob
from pathlib import Path
from typing import Optional

SEARCH_PATTERNS = [
    "~/.cache/ms-playwright/*/chrome-mac-*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
    "~/Library/Caches/ms-playwright/*/chrome-mac-*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
    "~/Library/Application Support/Google/Chrome for Testing/Google Chrome for Testing",
]


def find_chrome_for_testing() -> Optional[Path]:
    for pattern in SEARCH_PATTERNS:
        for candidate in glob(os.path.expanduser(pattern)):
            path = Path(candidate)
            if path.exists() and path.is_file():
                return path
    return None


def open_url_in_chromium(url: str) -> bool:
    browser_path = find_chrome_for_testing()
    if browser_path is not None:
        try:
            subprocess.Popen([str(browser_path), url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except OSError:
            pass

    if sys.platform == "darwin":
        try:
            subprocess.Popen(["open", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except OSError:
            pass

    return False
