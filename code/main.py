from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import threading
import random
import string
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

user_home = os.path.expanduser("~")
client_id_path = os.path.join(user_home, r'AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\clientId.txt')
if os.path.exists(client_id_path):
    os.remove(client_id_path)

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

account_count = int(input('>'))
account_index = 0

last_names = ['佐藤', '鈴木', '高橋', '田中', '伊藤', '渡辺', '山本', '中村', '小林', '加藤', '吉田', '山田', '佐々木', '山口', '松本', '井上', '木村', '林', '斎藤', '清水']
first_names = ['翔太', '拓也', '健太', '翔', '達也', '雄太', '翔平', '大樹', '亮', '健太郎', '愛', '彩', '美穂', '成美', '沙織', '麻衣', '舞', '愛美', '瞳', '彩香']

chrome_options = Options()
chrome_options.add_argument('--headless') 

account_index_lock = threading.Lock()

def generate_account():
    global account_index

    try:
        with account_index_lock:
            account_index += 1
            username_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        browser = webdriver.Chrome(options=chrome_options)
        browser.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fja-jp%2faccountcreation%3frtc%3d1%26csrf%3diRRDbBsXHWOzqJoxX9GqJOfUcAQCvJVJSNVhpu9YR0ntJtPfRjwCMjSg4qE1UQC4yx6KIvX4cVItbVhM5kW-6bAyA7o1&id=292543&aadredir=1&contextid=8369C2F0524F361B&bk=1602012918&uiflavor=web&lic=1&mkt=ja-jp&lc=1033&uaid=3ba71ae4427e4c300da204fc26106240")
        browser.implicitly_wait(20)

        switch_button = browser.find_element(By.ID, 'liveSwitch')
        switch_button.click()

        username_input = browser.find_element(By.ID, 'MemberName')
        username_input.send_keys('a' + username_suffix)

        signup_button_1 = browser.find_element(By.ID, 'iSignupAction')
        signup_button_1.click()
        browser.implicitly_wait(20)

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        password_input = browser.find_element(By.ID, 'PasswordInput')
        password_input.send_keys(password)

        signup_button_2 = browser.find_element(By.ID, 'iSignupAction')
        signup_button_2.click()

        with open(f'{account_index}pack.txt', 'a') as file:
            file.write(f'a{username_suffix}@outlook.jp\n{password}\n')

        browser.implicitly_wait(20)

        last_name_input = browser.find_element(By.ID, 'LastName')
        last_name = random.choice(last_names)
        last_name_input.send_keys(last_name)
        time.sleep(0.1)

        first_name_input = browser.find_element(By.ID, 'FirstName')
        first_name = random.choice(first_names)
        first_name_input.send_keys(first_name)

        signup_button_3 = browser.find_element(By.ID, 'iSignupAction')
        signup_button_3.click()

        browser.implicitly_wait(60)

        birth_year_input = browser.find_element(By.ID, 'BirthYear')
        birth_year = str(random.randint(1970, 1999))
        birth_year_input.send_keys(birth_year)
        time.sleep(0.1)

        birth_month_input = browser.find_element(By.ID, 'BirthMonth')
        birth_month = str(random.randint(1, 12))
        birth_month_input.send_keys(birth_month)
        time.sleep(0.1)

        birth_day_input = browser.find_element(By.ID, 'BirthDay')
        birth_day = str(random.randint(1, 25))
        birth_day_input.send_keys(birth_day)

        signup_button_4 = browser.find_element(By.ID, 'iSignupAction')
        signup_button_4.send_keys(Keys.ENTER)

        browser.implicitly_wait(60000)
        next_button = browser.find_element(By.ID, 'idSIButton9')
        next_button.click()

        browser.implicitly_wait(60)
        accept_button = browser.find_element(By.ID, 'Accept')
        accept_button.click()

    except NoSuchElementException as e:
        print(f"Error: Element not found - {str(e)}")

    except TimeoutException as e:
        print(f"Error: Timeout waiting for element - {str(e)}")

    except WebDriverException as e:
        print(f"Error: WebDriver issue - {str(e)}")

    except Exception as e:
        print(f"Unexpected error: {str(e)}")

    finally:
        if 'browser' in locals() and browser:
            browser.quit()

for _ in range(account_count):
    thread = threading.Thread(target=generate_account)
    thread.start()
    time.sleep(5)
