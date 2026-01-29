import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import random
import os

BOT_URL = # your bot's token here

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_tokens(file="tokens.txt"):
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_retry_token(token):
    with open("retry.txt", "a") as f:
        f.write(token + "\n")

def login_with_token(driver, token):
    logging.info("Logging token...")
    driver.get("https://discord.com/login")
    time.sleep(3)

def handle_authorization(driver, wait):
    zoom_and_scroll_to_authorize(driver)
    scroll_modal_to_bottom(driver)

    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            auth_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Authorize')]")
            ))
            auth_button.click()
            logging.info(f"Authorization button clicked (Attempt {attempt + 1})")
            time.sleep(3)
            return True
        except Exception as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            scroll_modal_to_bottom(driver)
            time.sleep(2)

    logging.warning("Authorization button could not be clicked automatically.")
    logging.info("Waiting for manual authorization (up to 30 seconds)...")

    for _ in range(30):
        if "top.gg/bot" in driver.current_uri:
            logging.info("Manual authorization detected. Continuing...")
            return True
        time.sleep(1)

    logging.error("Manual authorization not detected. Step failed.")
    return False


def scroll_modal_to_bottom(driver):
    script = """
    let modal = document.querySelector('[class*="scroller"]');
    if (modal) {
        modal.scrollTop = modal.scrollHeight;
    }
    """
    driver.execute_script(script)
    logging.info("Scrolled OAuth modal to bottom")
    time.sleep(1)

def zoom_and_scroll_to_authorize(driver):
    driver.execute_script("document.body.style.zoom='0.5'")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    logging.info("Zoomed and scrolled to bottom to reveal authorize button")

def vote_with_token(token):
    options = uc.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    try:
        login_with_token(driver, token)

        driver.get(BOT_URL)
        time.sleep(3)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))).click()
            time.sleep(2)
        except:
            pass

        for _ in range(10):
            if "discord.com/oauth2" in driver.current_url:
                break
            time.sleep(1)

        for _ in range(20):
            if "discord.com/oauth2" in driver.current_url:
                logging.info("OAuth page detected")
                break
            time.sleep(0.5)

        if not handle_authorization(driver, wait):
            logging.error("Failed to complete authorization")
            return False

        for _ in range(10):
            if "top.gg/bot" in driver.current_url:
                break
            time.sleep(0.5)

        vote_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/vote')]")
        ))
        vote_link.click()
        time.sleep(3)
        ))
        vote_button.click()
        logging.info("Voted Successfully!")
        return True

    except Exception as e:
        logging.error(f"Error: {e}")
        return False
    finally:
        time.sleep(5)
        driver.quit()

def process_token(token, retry=False):
    logging.info(f"{'Retrying' if retry else 'Voting with'} token: {token}")
    success = vote_with_token(token)
    if not success:
        logging.warning(f"Retrying token: {token}")
        success = vote_with_token(token)
        if not success:
            logging.error(f"Failed after retry: {token}")
            save_retry_token(token)

def main():
    if os.path.exists("retry.txt"):
        os.remove("retry.txt")

    tokens = get_tokens()
    for token in tokens:
        process_token(token)
        time.sleep(random.uniform(2, 3))

    if os.path.exists("retry.txt"):
        logging.info("Processing retry tokens...")
        retry_tokens = get_tokens("retry.txt")
        os.remove("retry.txt")

if __name__ == "__main__":

    main()
