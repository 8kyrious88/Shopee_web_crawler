import os, time, random, pandas
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime

# def human_scroll(driver):
#     # Get the total height of the page
#     total_height = driver.execute_script("return document.body.scrollHeight")
#     current_pos = 0
    
#     while current_pos < total_height:
#         # Scroll down by a random amount (200 to 600 pixels)
#         step = random.randint(200, 600)
#         current_pos += step
#         driver.execute_script(f"window.scrollTo(0, {current_pos});")
        
#         # Random "thinking" pause
#         time.sleep(random.uniform(0.5, 1.5))
        
#         # Update height in case the page expanded (infinite scroll)
#         total_height = driver.execute_script("return document.body.scrollHeight")


# load_dotenv()
# username = os.getenv('USERNAME')
# password = os.getenv('PASSWORD')
# user_data_path = os.getenv('USER_DATA_PATH')
# chrome_options = uc.ChromeOptions()
# chrome_options.add_argument(f'--user-data-dir={user_data_path}')
# chrome_options.add_argument('--profile-directory=Default')
# driver = uc.Chrome(options=chrome_options, version_main=144)
# driver.get("https://shopee.sg/top_products?catId=SG_BITL0_1068%3Atop_sold")
# time.sleep(3)
# human_scroll(driver=driver)

# html_content = driver.page_source
# driver.quit()
# soup = BeautifulSoup(html_content,'html.parser')
data = {}
today_date = datetime.today().strftime('%d/%m/%Y')
# with open('scrapped_page.html','w', encoding='utf-8') as file:
#     file.write(soup.prettify())


with open('scrapped_page.html','r') as file:
    soup = BeautifulSoup(file, "html.parser")
    product_name_div_tags = soup.find_all('div', class_ = "TTpvXQ")
    data['Product Name'] = [div_tag.getText().strip() for div_tag in product_name_div_tags]
    product_price_div_tags = soup.find_all('div', class_ = "gkBW7i")
    data['Product Price'] = [float(div_tag.getText().strip().replace('$',"")) for div_tag in product_price_div_tags]
    sold_qty_div_tags = soup.find_all('div', class_='ExCLCG')
    data['Sold Qty'] = [int(div_tag.getText().split()[1]) for div_tag in sold_qty_div_tags]
    data['Ranking'] = [ranking + 1 for ranking in range (len(data['Product Name']))]
    data['Date'] = [today_date for i in range (len(data['Product Name']))]

df = pandas.DataFrame(data)
if os.path.exists('.//Shopee_Top_Sales_BN.xlsx'):
    original_df = pandas.read_excel('Shopee_Top_Sales_BN.xlsx')
    new_df = pandas.concat([df,original_df])
    new_df.to_excel('Shopee_Top_Sales_BN.xlsx',index=False)
else:
    df.to_excel('Shopee_Top_Sales_BN.xlsx',index=False)









### Normall account log in
# original_window = driver.current_window_handle
# wait = WebDriverWait(driver, 10)
# username_column = wait.until(EC.visibility_of_element_located((By.NAME,'loginKey')))
# for char in username:
#     username_column.send_keys(char)
#     time.sleep(random.uniform(0.05,0.2))
# password_column = driver.find_element(By.NAME,'password')
# for char in password:
#     password_column.send_keys(char)
#     time.sleep(random.uniform(0.05,0.2))
# time.sleep(random.uniform(1,4))

# login_button = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button')
# login_button.click()
# time.sleep(5)


### Google account log in
# button_google_login = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/button[2]')))
# time.sleep(3)
# button_google_login.click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[-1])
# email_column = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
# for char in 'chunping071141@gmail.com':
#     email_column.send_keys(char)
#     time.sleep(random.uniform(0.05,0.2))
# time.sleep(1)
# login_button = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
# login_button.click()
# driver.switch_to.window(original_window)
# time.sleep(10)
