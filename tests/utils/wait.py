# utils/wait.py
from playwright.sync_api import Page
import time


def wait_after_step(page: Page, seconds: int = 1):
    time.sleep(seconds)
