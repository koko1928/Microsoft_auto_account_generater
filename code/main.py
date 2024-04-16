import os
import threading
import random
import string
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def display_ascii_art():
    ascii_art = '''
    ⣿⣿⣿⠟⠉⠉⠻⣿⣿⣿
    ⣿⣿⡏⠂⠂⠂⠂⢹⣿⣿
    ⣿⣿⡇⠂⠂⠂⠂⢸⣿⣿
    ⣿⣿⣧⣾⡇⢸⣷⣼⣿⣿
    ⣿⣿⣿⠈⢠⡄⠁⣿⣿⣿
    ⣿⠅⠸⣏⠂⠂⣹⠇⠨⣿
    ⣿⣀⡀⠈⠻⠟⠁⢀⣀⣿
    ⣿⠿⡿⠂⠂⠂⠐⢿⠿⣿
    ⣿⠂⠂⣠⣾⣷⣄⠂⠂⣿
    ⣿⣄⣼⣿⣿⣿⣿⣧⣠⣿
    created by koko1928
    '''
    print('\033[35m' + ascii_art + '\033[0m')
    prompt_text = "\033[32mACC GEN \n注意:この画面は閉じないでください。\n作成するアカウントの個数を1から3の半角数字で入力してください。\n"
    for char in prompt_text:
        print(char, end='', flush=True)
        time.sleep(0.007)

def generate_account_info(last_names, first_names):
    username_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    last_name = random.choice(last_names)
    first_name = random.choice(first_names)
    birth_year = str(random.randint(1970, 1999))
    birth_month = str(random.randint(1, 12))
    birth_day = str(random.randint(1, 28))
    return username_suffix, password, last_name, first_name, birth_year, birth_month, birth_day

def setup_browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(20)
    return browser

def create_account(browser, account_info):
    username_suffix, password, last_name, first_name, birth_year, birth_month, birth_day = account_info
    try:
        browser.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fja-jp%2faccountcreation%3frtc%3d1%26csrf%3diRRDbBsXHWOzqJoxX9GqJOfUcAQCvJVJSNVhpu9YR0ntJtPfRjwCMjSg4qE1UQC4yx6KIvX4cVItbVhM5kW-6bAyA7o1&id=292543&aadredir=1&contextid=8369C2F0524F361B&bk=1602012918&uiflavor=web&lic=1&mkt=ja-jp&lc=1033&uaid=3ba71ae4427e4c300da204fc26106240")
        browser.find_element(By.ID, "liveSwitch").click()
        browser.find_element(By.ID, "MemberName").send_keys("a" + username_suffix)
        browser.find_element(By.ID, "iSignupAction").click()
        p = password
        browser.find_element(By.ID, "PasswordInput").send_keys(p)
        browser.find_element(By.ID, "iSignupAction").click()
        f = open(f"{username_suffix}_pack.txt", "a")
        f.write(f"a{username_suffix}@outlook.jp\n{p}\n")
        browser.find_element(By.ID, "LastName").send_keys(last_name)
        time.sleep(0.1)
        browser.find_element(By.ID, "FirstName").send_keys(first_name)
        browser.find_element(By.ID, "iSignupAction").click()
        browser.find_element(By.ID, "BirthYear").send_keys(birth_year)
        time.sleep(0.1)
        browser.find_element(By.ID, "BirthMonth").send_keys(birth_month)
        time.sleep(0.1)
        browser.find_element(By.ID, "BirthDay").send_keys(birth_day)
        browser.find_element(By.ID, "iSignupAction").send_keys(Keys.ENTER)
        browser.find_element(By.ID, "declineButton").click()
        browser.find_element(By.ID, "Cancel").click()
    except (NoSuchElementException, TimeoutException, WebDriverException) as e:
        logger.error(f"アカウント生成中にエラーが発生しました: {str(e)}")

def account_thread(account_index, chrome_options, last_names, first_names):
    account_info = generate_account_info(last_names, first_names)
    with setup_browser(chrome_options) as browser:
        create_account(browser, account_info)

def validate_user_input(user_input):
    try:
        account_count = int(user_input)
        if 1 <= account_count <= 3:
            return account_count
        else:
            raise ValueError("アカウントの個数は1から3の範囲で指定してください。")
    except ValueError:
        raise ValueError("有効な半角数字を入力してください。")

def main():
    user_home = os.path.expanduser("~")
    client_id_path = os.path.join(user_home, r'AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\clientId.txt')
    
    try:
        if os.path.exists(client_id_path):
            os.remove(client_id_path)

        display_ascii_art()

        user_input = input('>')
        account_count = validate_user_input(user_input)

        chrome_options = Options()
        chrome_options.add_argument('--headless')

        last_names = ['佐藤', '鈴木', '高橋', '田中', '伊藤', '渡辺', '山本', '中村', '小林', '加藤', '吉田', '山田', '佐々木', '山口', '松本', '井上', '木村', '林', '斎藤', '清水']
        first_names = ['翔太', '拓也', '健太', '翔', '達也', '雄太', '翔平', '大樹', '亮', '健太郎', '愛', '彩', '美穂', '成美', '沙織', '麻衣', '舞', '愛美', '瞳', '彩香']

        threads = []
        for i in range(account_count):
            thread = threading.Thread(target=account_thread, args=(i, chrome_options, last_names, first_names))
            threads.append(thread)
            thread.start()
            time.sleep(5)

        for thread in threads:
            thread.join()

    except Exception as e:
        logger.error(f"プログラム実行中にエラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()
