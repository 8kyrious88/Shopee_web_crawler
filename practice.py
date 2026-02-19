import undetected_chromedriver as uc
import time

def main():
    # It's better to pass headless via options in newer UC versions
    options = uc.ChromeOptions()
    options.add_argument('--headless') 
    
    driver = uc.Chrome(options=options, version_main=144)
    
    try:
        driver.get('https://nowsecure.nl')
        time_to_wait = 5 # Give it a moment to bypass the check
        time.sleep(time_to_wait)
        
        driver.save_screenshot('nowsecure.png')
        print("Screenshot saved successfully!")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()